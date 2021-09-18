from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser 

from backend.models import Attendance, Employee, Department
from backend.serializers import *

import os
import base64

@api_view(['GET'])
def get_all(request):
    image = Employee.objects.all()
    serializer = ImageSerializer(image, many=True)
    for employee in image:
        file_name = dl_2(employee.image_1, employee.employee_id, 1)
        
        '''byte_data = employee.image_1.tobytes()
        print(byte_data[0:20])
        print(len(byte_data))
        print(byte_data[-20:-1])
        file_name = dl_2(byte_data, employee.employee_id, 1)
        print(file_name)
        with open("Test.jpg", 'wb') as f:
            f.write(base64.b64decode(employee.image_1))'''
        
    return Response({
        "message": "images retrieved",
        "data": serializer.data
    })

def dl_2(image, employee_id, image_count):
    #image = ""
    imgdata = base64.b64decode(image)
    file_name = 'employee_' + str(employee_id) + '_' + str(image_count) + '.jpg'
    with open(file_name, 'wb') as f:
        f.write(imgdata)
    return(file_name)
    # f gets closed when you exit the with statement
    # Now save the value of filename to your database