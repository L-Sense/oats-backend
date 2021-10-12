from rest_framework import serializers

from backend.models import *

import base64


class BinaryField(serializers.Field):
    def to_representation(self, value):
        print("Pases here")
        return str(value)

    def to_internal_value(self, data):
        print("Goes here")
        return bytearray(data)


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
        if validated_data['image_3'] != "null":
            employee = Employee.objects.create(
                employee_name = validated_data['employee_name'], 
                department_id = validated_data['department'].department_id, 
                image_1 = bytearray(base64.b64decode(validated_data['image_1'])),
                image_2 = bytearray(base64.b64decode(validated_data['image_2'])),
                image_3 = bytearray(base64.b64decode(validated_data['image_3']))
            )
        elif validated_data['image_2'] != "null":
            employee = Employee.objects.create(
                employee_name = validated_data['employee_name'], 
                department_id = validated_data['department'].department_id, 
                image_1 = bytearray(base64.b64decode(validated_data['image_1'])),
                image_2 = bytearray(base64.b64decode(validated_data['image_2']))
            )
        elif validated_data['image_1'] != "null":
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
