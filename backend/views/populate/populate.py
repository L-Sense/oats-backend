from django.http import JsonResponse
from django.db import connection
from datetime import datetime

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
    return

def populate_everything(request):
    department_one = Department.objects.create(department_name='SCSE', late_threshold=15)
    department_two = Department.objects.create(department_name='SPMS', late_threshold=15)
    employee_one = Employee.objects.create(employee_name='Ting Zhi Ying', department_id=2, image_1=image_to_bytea("backend/views/populate/U1922086G_1.jpg"))
    employee_two = Employee.objects.create(employee_name='Leonardo Irvin Pratama', department_id=1, image_1=image_to_bytea("backend/views/populate/U1920301J_1.jpg"))
    employee_three = Employee.objects.create(employee_name='Lim Zheng Xian', department_id=1, image_1=image_to_bytea("backend/views/populate/U1923211H_1.jpg"))
    employee_four = Employee.objects.create(employee_name='Luke Chin Peng Hao', department_id=1, image_1=image_to_bytea("backend/views/populate/U1921936J_3.jpg"))
    employee_five = Employee.objects.create(employee_name='Ferlita Halim', department_id=2, image_1=image_to_bytea("backend/views/populate/U1920961A_1.jpg"))
    employee_six = Employee.objects.create(employee_name='Lim Cheng Yun', department_id=2, image_1=image_to_bytea("backend/views/populate/U1921703D_1.jpg"))
    attendance_one = Attendance.objects.create(employee_id=1, in_time=datetime.strptime("08:00", "%H:%M").time())
    attendance_two = Attendance.objects.create(employee_id=5, in_time=datetime.strptime("08:00", "%H:%M").time(), out_time=datetime.strptime("17:00", "%H:%M").time())
    attendance_three = Attendance.objects.create(employee_id=3, in_time=datetime.strptime("08:30", "%H:%M").time(), out_time=datetime.strptime("17:00", "%H:%M").time(), status="Abnormal")
    attendance_four = Attendance.objects.create(employee_id=4, out_time=datetime.strptime("17:00", "%H:%M").time())
    return JsonResponse({
        'message': 'Data inserted successfully.'
    }, status=200)

def truncate_everything(request):
    truncate = reset_index()
    return JsonResponse({
        'message': 'Tables truncated successfully.'
    }, status=200)