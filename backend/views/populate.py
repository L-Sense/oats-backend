import json

from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

from backend.models import Department

# Create your views here.

def populate_everything(request):
    department_one = Department.objects.create(department_name='SCSE', late_threshold=15)
    department_two = Department.objects.create(department_name='SPMS', late_threshold=15)
    return HttpResponse(json.dumps({
        'message': 'Data inserted successfully.'
    }), status=200)

# run TRUNCATE TABLE backend_department RESTART IDENTITY CASCADE; to reset the data and increment