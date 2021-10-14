from backend.decorators import token_required
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser

from backend.decorators import token_required
from backend.models import Attendance, Employee, Department
from backend.serializers import *

import base64
import os
import shutil
import re
import pytz
from datetime import datetime, date, time

from deepface import DeepFace


def parse(dir):
    return int(re.findall(r"_\w+_", dir)[0][1:-1])


@api_view(['POST'])
@token_required
def scanner_photo(request):
    try:
        image_parse = JSONParser().parse(request)
        image_string = image_parse['image']
        check = image_parse['isCheckin']
        image = base64.b64decode(image_string)
        tz = pytz.timezone('Singapore')

        if os.path.exists("input"):
            shutil.rmtree('input')
        os.makedirs('input')

        test_dir = os.path.join("input/", "test.jpg")
        with open(test_dir, 'wb') as f:
            f.write(image)
    except:
        return Response({
            "message": "server error, please contact the administrator",
            "data": [],
        }, 500)

    try:
        DeepFace.detectFace(test_dir)
    except ValueError:
        shutil.rmtree('input')
        return Response({
            "message": "face not detected",
            "data": [],
        }, 500)
    except:
        return Response({
            "message": "server error, please contact the administrator",
            "data": [],
        }, 500)

    try:
        results = DeepFace.find(
            test_dir,
            db_path="images",
            distance_metric='euclidean_l2'
        )
        employee = parse(results["identity"][0])
        employee_info = Employee.objects.get(pk=employee)
        shutil.rmtree('input')

        if len(results) == 0:
            return Response({
                "message": "face does not exist in our database",
                "data": [],
            }, 500)

        try:
            attendance = Attendance.objects.filter(
                date=date.today()).get(employee=employee)
            if check:
                if attendance.in_time:
                    return Response({
                        "message": "attendance already recorded",
                        "data":
                        {
                            "id": employee,
                            "employee_name": employee_info.employee_name,
                            "department_id": employee_info.department_id,
                            "department_name": Department.objects.get(pk=employee_info.department_id).department_name
                        },
                    }, 200)
                else:
                    attendance.in_time = datetime.now(tz).time()
                    threshold = datetime.combine(date.today(), time(8, 0, 0))
                    diff = datetime.now(tz) - threshold
                    late = abs(diff.total_seconds()) > 900
                    if late:
                        attendance.status = "Abnormal"
                    attendance.save()
                    return Response({
                        "message": "attendance saved",
                        "data":
                        {
                            "id": employee,
                            "employee_name": employee_info.employee_name,
                            "department_id": employee_info.department_id,
                            "department_name": Department.objects.get(pk=employee_info.department_id).department_name
                        },
                    }, 200)
            else:
                if attendance.out_time:
                    return Response({
                        "message": "attendance already recorded",
                        "data":
                        {
                            "id": employee,
                            "employee_name": employee_info.employee_name,
                            "department_id": employee_info.department_id,
                            "department_name": Department.objects.get(pk=employee_info.department_id).department_name
                        },
                    }, 200)
                else:
                    attendance.out_time = datetime.now(tz).time()
                    threshold = datetime.combine(date.today(), time(17, 0, 0))
                    diff = datetime.now(tz) - threshold
                    late = abs(diff.total_seconds()) > 900
                    if late:
                        attendance.status = "Abnormal"
                    attendance.save()
                    return Response({
                        "message": "attendance saved",
                        "data":
                        {
                            "id": employee,
                            "employee_name": employee_info.employee_name,
                            "department_id": employee_info.department_id,
                            "department_name": Department.objects.get(pk=employee_info.department_id).department_name
                        },
                    }, 200)

        except Attendance.DoesNotExist:
            if check:
                threshold = datetime.combine(date.today(), time(8, 0, 0))
                diff = datetime.now(tz) - threshold
                late = abs(diff.total_seconds()) > 900
                status = "Abnormal" if late else "Normal"
                attendance_data = {
                    "date": date.today(),
                    "employee": employee,
                    "in_time": datetime.now(tz).time(),
                    "status": status
                }
                attendance_serializer = AttendanceSerializer(
                    data=attendance_data)
                if attendance_serializer.is_valid():
                    attendance_serializer.save()
                    return Response({
                        "message": "attendance saved",
                        "data":
                        {
                            "id": employee,
                            "employee_name": employee_info.employee_name,
                            "department_id": employee_info.department_id,
                            "department_name": Department.objects.get(pk=employee_info.department_id).department_name
                        },
                    }, 200)
                else:
                    return Response({
                        "message": "server error",
                        "data": [],
                    }, 500)

            else:
                threshold = datetime.combine(date.today(), time(17, 0, 0))
                diff = datetime.now(tz) - threshold
                late = abs(diff.total_seconds()) > 900
                status = "Abnormal" if late else "Normal"
                attendance_data = {
                    "date": date.today(),
                    "employee": employee,
                    "out_time": datetime.now(tz).time(),
                    "status": status
                }
                attendance_serializer = AttendanceSerializer(
                    data=attendance_data)
                if attendance_serializer.is_valid():
                    attendance_serializer.save()
                    return Response({
                        "message": "attendance saved",
                        "data":
                            {
                                "id": employee,
                                "employee_name": employee_info.employee_name,
                                "department_id": employee_info.department_id,
                                "department_name": Department.objects.get(pk=employee_info.department_id).department_name
                            },
                    }, 200)
                else:
                    return Response({
                        "message": "server error",
                        "data": []
                    }, 500)

        except:
            return Response({
                "message": "server error, please contact the administrator",
                "data": [],
            }, 500)

    except ValueError:
        shutil.rmtree('input')
        return Response({
            "message": "server fails to detect the image database, ask the admin to reload the database",
            "data": [],
        }, 500)

    except:
        return Response({
            "message": "server error, please contact the administrator",
            "data": [],
        }, 500)
