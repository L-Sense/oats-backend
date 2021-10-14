from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser 

from backend.models import Attendance, Employee, Department
from backend.serializers import *

from datetime import datetime, date
from time import strftime

@api_view(['GET', 'POST', 'DELETE'])
def get_all(request):
    if request.method == 'GET':
        attendance = Attendance.objects.all()
        serializer = AttendanceSerializer(attendance, many=True)
        return Response({
            "message": "attendance retrieved",
            "data": serializer.data
        })
    elif request.method == 'POST':
        attendance_data = JSONParser().parse(request)
        attendance_data['date'] = datetime.strptime(attendance_data['date'], "%d/%m/%Y").date()
        attendance_serializer = AttendanceSerializer(data=attendance_data)
        if attendance_serializer.is_valid():
            attendance_serializer.save()
            return Response({
                    "message": "attendance posted",
                    "data": attendance_serializer.data
                })
        else:
            return Response({
                    "message": "invalid input"
                })
    elif request.method == 'DELETE':
        attendance_data = JSONParser().parse(request)
        attendance_serializer = AttendanceSelectSerializer(data=attendance_data)
        if attendance_serializer.is_valid():
            try:
                attendance = Attendance.objects.filter(date=attendance_serializer.validated_data['date']).get(employee=attendance_serializer.validated_data['employee'])
                attendance.delete()
                return Response({
                    "message": "attendance record deleted successfully"
                })
            except Attendance.DoesNotExist:
                return Response({
                    "message": "record not found"
                })
        return Response({
                "message": "invalid input"
            })

@api_view(['GET'])
def count_today(request):
    len_in = Attendance.objects.filter(date=date.today()).filter(in_time__isnull=False).count()
    len_out = Attendance.objects.filter(date=date.today()).filter(in_time__isnull=False).filter(out_time__isnull=False).count()
    employee_count = Employee.objects.all().count()
    return Response({
        "message": "attendance retrieved",
        "data": {
            "checked_in_today_count": len_in, 
            "checked_out_today_count": len_out,
            "total_employees": employee_count
        }
        })

@api_view(['GET'])
def count_date(request):
    date = request.query_params['date']
    parsed_date = datetime.strptime(date, "%d/%m/%Y").date()
    len_in = Attendance.objects.filter(date=parsed_date).filter(in_time__isnull=False).count()
    len_out = Attendance.objects.filter(date=parsed_date).filter(in_time__isnull=False).filter(out_time__isnull=False).count()
    employee_count = Employee.objects.all().count()
    return Response({
        "message": "attendance retrieved",
        "data": {
            "checked_in_today_count": len_in, 
            "checked_out_today_count": len_out,
            "total_employees": employee_count
        }
        })

@api_view(['GET'])
def get_today(request):
    employee = Employee.objects.all()
    data = []
    for person in employee:
        try:
            attendance = Attendance.objects.filter(date=date.today()).get(employee=person.employee_id)
            info = {
                "employee_id": person.employee_id,
                "employee_name": person.employee_name,
                "department_name": Department.objects.get(pk=person.department_id).department_name,
                "in_time": attendance.in_time.strftime("%H:%M:%S") if attendance.in_time else attendance.in_time,
                "out_time": attendance.out_time.strftime("%H:%M:%S") if attendance.out_time else attendance.out_time,
                "status": attendance.status
            }
        except Attendance.DoesNotExist:
            info = {
                "employee_id": person.employee_id,
                "employee_name": person.employee_name,
                "department_name": Department.objects.get(pk=person.department_id).department_name,
                "in_time": None,
                "out_time": None,
                "status": "Leave"
            }
        data.append(info)
    return Response({
        "message": "attendance retrieved",
        "data": data
    })

@api_view(['GET'])
def get_date(request):
    date = request.query_params['date']
    parsed_date = datetime.strptime(date, "%d/%m/%Y").date()
    employee = Employee.objects.all()
    data = []
    for person in employee:
        try:
            attendance = Attendance.objects.filter(date=parsed_date).get(employee=person.employee_id)
            info = {
                "employee_id": person.employee_id,
                "employee_name": person.employee_name,
                "department_name": Department.objects.get(pk=person.department_id).department_name,
                "in_time": attendance.in_time.strftime("%H:%M:%S") if attendance.in_time else attendance.in_time,
                "out_time": attendance.out_time.strftime("%H:%M:%S") if attendance.out_time else attendance.out_time,
                "status": attendance.status
            }
        except:
            info = {
                "employee_id": person.employee_id,
                "employee_name": person.employee_name,
                "department_name": Department.objects.get(pk=person.department_id).department_name,
                "in_time": None,
                "out_time": None,
                "status": "No Show"
            }
        data.append(info)
    return Response({
        "message": "attendance retrieved",
        "data": data
    })

@api_view(['POST'])
def update_status(request):
    attendance_data = JSONParser().parse(request)
    attendance_data['date'] = datetime.strptime(attendance_data['date'], "%d/%m/%Y").date()
    attendance_serializer = AttendanceStatusSerializer(data=attendance_data)
    if attendance_serializer.is_valid():
        try:
            attendance = Attendance.objects.filter(date=attendance_serializer.validated_data['date']).get(employee=attendance_serializer.validated_data['employee'])
            attendance.status = attendance_serializer.validated_data['status']
            attendance.save()
            return Response({
                "message": "status changed",
                "data": attendance.employee_id
            })
        except Attendance.DoesNotExist:
            attendance_serializer.save()
            return Response({
                "message": "status recorded",
                "data": attendance_serializer.data
            })
    return Response({
            "message": "invalid input"
        })