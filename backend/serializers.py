from rest_framework import serializers

from backend.models import *

class AttendanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attendance
        fields = ['employee', 'date', 'in_time', 'out_time', 'status'] # if want to specify manually, ['__all__']

class AttendanceDeleteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attendance
        fields = ['employee', 'date']