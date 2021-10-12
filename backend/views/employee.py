#from django.http import FileResponse

from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser 

from backend.models import Attendance, Employee, Department
from backend.serializers import *


@api_view(['GET', 'POST'])
def get_all(request):
    if request.method == "GET":
        employee = Employee.objects.all()
        data = []
        for person in employee:
            print(person.employee_id)
            info = {
                "employee_id": person.employee_id,
                "employee_name": person.employee_name,
                "department_id": person.department_id,
                "department_name": Department.objects.get(pk=person.department_id).department_name,
                "avatar": "Image of the guy?"
            }
            data.append(info)

        return Response({
            "message": "all employee data retrieved",
            "data": data
        })
    elif request.method == "POST":
        employee_data = JSONParser().parse(request)
        employee_serializer = EmployeeCreateSerializer(data=employee_data)
        if employee_serializer.is_valid():
            employee_serializer.save()
            return Response({
                "message": "new employee created",
                "data": employee_serializer.data
            })
        else:
            return Response({
                "message": "invalid input"
            })

@api_view(['GET'])
def get_one(request, employee_id):
    try:
        employee = Employee.objects.get(pk=employee_id)
        return Response({
        "message": "data of employee with id " + employee_id + " retrieved.",
        "data": {
            "employee_id": employee.employee_id,
            "employee_name": employee.employee_name,
            "department_id": employee.department_id,
            "department_name": Department.objects.get(pk=employee.department_id).department_name,
            "avatar": "Image of the guy?"
        }
    })
    except Employee.DoesNotExist:
        return Response({
            "message": "Employee matching query does not exist.",
        })

    except:
        return Response({
            "message": "An error has occurred",
        })

@api_view(['POST'])
def create(request):
     #It should save it to server's localhost.
    employee_data = JSONParser().parse(request)
    employee_serializer = EmployeeCreateSerializer(data=employee_data)
    if employee_serializer.is_valid():
        employee_serializer.save()
        return Response({
            "message": "new employee created",
            "data": employee_serializer.data
        })
    else:
        return Response({
            "message": "invalid input"
        })
"""
def create(request):
     #It should save it to server's localhost.
    employee_data = JSONParser().parse(request)
    try:
        employee = Employee.objects.get(employee_id=employee_id)
        return Response({
            "message": "employee record already found"
        })
    except Employee.DoesNotExist:
        employee_serializer = EmployeeCreateSerializer(data=employee_data)
        if employee_serializer.is_valid():
            employee_serializer.save()
            return Response({
                "message": "new employee created",
                "data": employee_serializer.data
            })
        return Response({
            "message": "invalid input"
        })
"""
    
    
@api_view(['PUT'])
def update(request, employee_id):
    employee_data = JSONParser().parse(request)
    employee_serializer = EmployeeUpdateSerializer(data=employee_data)
    if employee_serializer.is_valid():
        try:
            employee = Employee.objects.get(employee_id=employee_id)
            employee.employee_name = employee_serializer.validated_data['employee_name']
            employee.department = employee_serializer.validated_data['department']
            employee.save()
            return Response({
                "message": "employee data updated",
                "data": employee.employee_id
            })
        except Employee.DoesNotExist:
            return Response({
                "message": "employee does not exist"
            })
    return Response({
            "message": "invalid input"
        })

"""
# For displaying employee image. Not complete.

@api_view(['GET'])
def get_image(request):
    employee = Employee.objects.all()
    data = []
    for person in employee:
        print(person.employee_id)
        attendance = Attendance.objects.filter(date=date.today()).get(employee=person.employee_id)
        info = {
            "employee_id": person.employee_id,
            "employee_name": person.employee_name,
            "department_id": person.department_id,
            "department_name": Department.objects.get(pk=person.department_id).department_name,
        }
        data.append(info)

    return FileResponse({person.image_1}),
"""
