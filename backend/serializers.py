from rest_framework import serializers

from backend.models import *

class AttendanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attendance
        fields = '__all__' # if want to specify manually, ['date', 'in_time', 'out_time', 'status']