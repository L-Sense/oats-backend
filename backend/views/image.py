from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser 

from django.core import serializers as core_serializers
import json

from backend.models import Attendance, Employee, Department
from backend.serializers import *

import os
import shutil
import base64

@api_view(['GET'])
def get_all(request):
    image = Employee.objects.all()
    serializer = ImageSerializer(image, many=True)

    shutil.rmtree('images')
    os.makedirs('images')

    '''for employee in image:
        file_name = decode_image(employee.image_1, employee.employee_id, 1)
        
        byte_data = employee.image_1.tobytes()
        print(byte_data[0:20])
        print(len(byte_data))
        print(byte_data[-20:-1])
        file_name = decode_image(byte_data, employee.employee_id, 1)
        print(file_name)
        with open("Test.jpg", 'wb') as f:
            f.write(base64.b64decode(employee.image_1))'''
    
    # Writes to a json
    with open(os.path.join("images/", "employee_images.json"), "w") as out:
        data = core_serializers.serialize("json", image)
        out.write(data)
    
    # Reads back the json...
    with open(os.path.join("images/", "employee_images.json"), 'r') as f:
        employee_json = json.load(f)
    
    # Decodes each binary to image for each employee
    for employee in employee_json:
        binary_image_1 = employee["fields"]["image_1"]
        binary_image_2 = employee["fields"]["image_2"]
        binary_image_3 = employee["fields"]["image_3"]

        decode_image(binary_image_1, employee["pk"], 1)
        
        # If images 2 and 3 aren't blank
        if binary_image_2 != "":
            decode_image(binary_image_2, employee["pk"], 2)
        if binary_image_3 != "":
            decode_image(binary_image_3, employee["pk"], 3)

    return Response({
        "message": "images retrieved",
        "data": serializer.data
    })

def decode_image(image_binary, employee_id, image_count):
    # Decodes binary string to image
    image = base64.b64decode(image_binary)
    
    '''with open("image_test_binary.json", "wb") as out:
        data = base64.b64encode(imgdata)
        out.write(data)'''

    # Can re-write file_name later to save elsewhere, e.g. some static folder
    file_name = 'employee_' + str(employee_id) + '_' + str(image_count) + '.jpg'

    with open(os.path.join("images/", file_name), 'wb') as f:
        f.write(image)

    return(file_name)