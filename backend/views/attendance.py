from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser 

from backend.models import Attendance, Employee
from backend.serializers import *

from datetime import datetime, date

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
        try:
            attendance = Attendance.objects.filter(date=date.today()).get(employee=attendance_data['employee'])
            return Response({
                "message": "attendance record already found"
            })
        except Attendance.DoesNotExist:
            attendance_serializer = AttendanceSerializer(data=attendance_data)
            if attendance_serializer.is_valid():
                attendance_serializer.save()
                return Response({
                    "message": "attendance recorded",
                    "data": attendance_serializer.data
                })
            return Response({
                "message": "invalid input"
            })
    elif request.method == 'DELETE':
        attendance_data = JSONParser().parse(request)
        attendance_serializer = AttendanceDeleteSerializer(data=attendance_data)
        if attendance_serializer.is_valid():
            try:
                attendance = Attendance.objects.filter(date=attendance_data['date']).get(employee=attendance_data['employee'])
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
    date_strip = datetime.strptime(date, "%d/%m/%Y").date()
    len_in = Attendance.objects.filter(date=date_strip).filter(in_time__isnull=False).count()
    len_out = Attendance.objects.filter(date=date_strip).filter(in_time__isnull=False).filter(out_time__isnull=False).count()
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
    attendance = Attendance.objects.filter(date=date.today())
    print(attendance.query) #left join employee to attendance 
    #serializer = AttendanceSerializer(attendance, many=True)
    return Response({
        "message": "attendance retrieved",
        #"data": serializer.data
    })

# https://www.bezkoder.com/django-rest-api/