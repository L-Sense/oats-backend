from rest_framework import serializers

from backend.models import *

class AttendanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attendance
        fields = ['employee', 'date', 'in_time', 'out_time', 'status'] # if want to specify manually, ['__all__']

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
    class Meta:
        model = Employee
        fields = ['employee_name', 'department', 'image_1', 'image_2', 'image_3']

class EmployeeUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ['employee_name', 'department']