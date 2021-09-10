from django.http import JsonResponse
from django.db import connection

from backend.models import *

def image_to_bytea(image):
    with open(image, "rb") as img:
        f = img.read()
        b = bytearray(f)
        return b

def reset_index():
    with connection.cursor() as cursor:
        cursor.execute("TRUNCATE TABLE backend_department RESTART IDENTITY CASCADE")
        cursor.execute("TRUNCATE TABLE backend_employee RESTART IDENTITY CASCADE")
        cursor.execute("TRUNCATE TABLE backend_attendance RESTART IDENTITY CASCADE")
        cursor.execute("TRUNCATE TABLE backend_admin RESTART IDENTITY CASCADE")
    return

def populate_everything(request):
    department_one = Department.objects.create(department_name='SCSE', late_threshold=15)
    department_two = Department.objects.create(department_name='SPMS', late_threshold=15)
    employee_one = Employee.objects.create(employee_name='Koh Boon Juey', department_id=1, image_1=image_to_bytea("backend/views/U1921258H_2.jpg"))
    employee_two = Employee.objects.create(employee_name='Leonardo Irvin Pratama', department_id=1, image_1=image_to_bytea("backend/views/U1920301J_1.jpg"))
    attendance_one = Attendance.objects.create(flag=False, type=True, employee_id=1)
    # TO-DO: I'm not sure what type of hashing you would want to implement here
    return JsonResponse({
        'message': 'Data inserted successfully.'
    }, status=200)

def truncate_everything(request):
    truncate = reset_index()
    return JsonResponse({
        'message': 'Tables truncated successfully.'
    }, status=200)