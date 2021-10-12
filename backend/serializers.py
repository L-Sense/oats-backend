from rest_framework import serializers
from rest_framework.response import Response

from backend.models import *

import base64
import os
import shutil

from deepface import DeepFace


class AttendanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attendance
        # if want to specify manually, ['__all__']
        fields = ['employee', 'date', 'in_time', 'out_time', 'status']


class AttendanceStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attendance
        fields = ['status', 'employee', 'date']


class AttendanceSelectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attendance
        fields = ['employee', 'date']


class AttendanceDateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attendance
        fields = ['date']


class EmployeeCreateSerializer(serializers.ModelSerializer):
    image_1 = serializers.CharField()
    image_2 = serializers.CharField()
    image_3 = serializers.CharField()
    
    def create(self, validated_data):
        if os.path.exists("input"):
            shutil.rmtree('input')
        os.makedirs('input')

        test_dir = os.path.join("input/", "test.jpg")

        if validated_data['image_3'] != "null":
            image_1 = base64.b64decode(validated_data['image_1'])
            image_2 = base64.b64decode(validated_data['image_2'])
            image_3 = base64.b64decode(validated_data['image_3'])

            with open(test_dir, 'wb') as f:
                f.write(image_1)
                f.write(image_2)
                f.write(image_3)

            try:
                DeepFace.detectFace(test_dir)
                shutil.rmtree('input')
            except ValueError:
                shutil.rmtree('input')
                # give sign to the serializer that it does not have face

            employee = Employee.objects.create(
                employee_name = validated_data['employee_name'], 
                department_id = validated_data['department'].department_id, 
                image_1 = bytearray(base64.b64decode(validated_data['image_1'])),
                image_2 = bytearray(base64.b64decode(validated_data['image_2'])),
                image_3 = bytearray(base64.b64decode(validated_data['image_3']))
            )

        elif validated_data['image_2'] != "null":
            image_1 = base64.b64decode(validated_data['image_1'])
            image_2 = base64.b64decode(validated_data['image_2'])

            with open(test_dir, 'wb') as f:
                f.write(image_1)
                f.write(image_2)

            try:
                DeepFace.detectFace(test_dir)
                shutil.rmtree('input')
            except ValueError:
                shutil.rmtree('input')
                # give sign to the serializer that it does not have face

            employee = Employee.objects.create(
                employee_name = validated_data['employee_name'], 
                department_id = validated_data['department'].department_id, 
                image_1 = bytearray(base64.b64decode(validated_data['image_1'])),
                image_2 = bytearray(base64.b64decode(validated_data['image_2']))
            )

        elif validated_data['image_1'] != "null":
            image_1 = base64.b64decode(validated_data['image_1'])

            with open(test_dir, 'wb') as f:
                f.write(image_1)

            try:
                DeepFace.detectFace(test_dir)
                shutil.rmtree('input')
            except ValueError:
                shutil.rmtree('input')
                # give sign to the serializer that it does not have face

            employee = Employee.objects.create(
                employee_name = validated_data['employee_name'], 
                department_id = validated_data['department'].department_id, 
                image_1 = bytearray(base64.b64decode(validated_data['image_1']))
            )
        employee.save()

        return employee

    class Meta:
        model = Employee
        fields = ['employee_name', 'department', 'image_1', 'image_2', 'image_3']

class EmployeeUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ['employee_name', 'department']


class AdminRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Admin
        fields = ['admin_name', 'username', 'password']


class AdminLoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = Admin
        fields = ['username', 'password']
        extra_kwargs = {'username': {'validators': []}, }


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ['employee_id', 'image_1', 'image_2', 'image_3']
