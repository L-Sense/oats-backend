from rest_framework.response import Response
from rest_framework.decorators import api_view

from backend.models import Attendance, Employee
from backend.serializers import AttendanceSerializer

@api_view(['GET'])
def get_all(request):
    attendance = Attendance.objects.all()
    serializer = AttendanceSerializer(attendance, many=True)
    return Response({
        "message": "attendance retrieved",
        "data": serializer.data
    })

@api_view(['GET'])
def check_in_out(request):
    len_in = Attendance.objects.filter(in_time__isnull=False).count()
    len_out = Attendance.objects.filter(in_time__isnull=False).filter(out_time__isnull=False).count()
    employee_count = Employee.objects.all().count()
    return Response({
        "message": "attendance retrieved",
        "data": {
            "checked_in_today_count": len_in, 
            "checked_out_today_count": len_out,
            "total_employees": employee_count
        }
        })