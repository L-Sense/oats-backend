from backend.decorators import token_required
import datetime
from os import error
from oats.settings import SECRET_KEY
import jwt
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from django.contrib.auth.hashers import make_password, check_password

from backend.serializers import AdminRegisterSerializer, AdminLoginSerializer
from backend.models import Admin


@api_view(['GET'])
@token_required
def check(request):
    obj = Admin.objects.all()
    obj = AdminRegisterSerializer(obj, many=True)
    return Response({
        "message": "attendance retrieved",
        "data": obj.data
    })


@api_view(['POST'])
@token_required
def register_admin(request):
    admin_data = JSONParser().parse(request)
    admin_serializer = AdminRegisterSerializer(data=admin_data)
    if not admin_serializer.is_valid():
        return Response({
            "message": "username already exist",
            "data": [],
        })
    try:
        if len(Admin.objects.filter(username=admin_serializer.validated_data["username"])):
            return Response({
                "message": "username already exist",
                "data": [],
            })
        admin_serializer.validated_data["password"] = make_password(
            admin_serializer.validated_data["password"])
        admin_serializer.save()
        return Response({
            "message": "admin registered",
            "data": [],
        })
    except:
        return Response({
            "message": "server error",
            "data": [],
        })


@api_view(['POST'])
def login_admin(request):
    admin_data = JSONParser().parse(request)
    admin_serializer = AdminLoginSerializer(data=admin_data)
    if not admin_serializer.is_valid():
        return Response({
            "message": "invalid input",
            "data": [],
        })
    try:
        hashed_password = Admin.objects.get(
            username=admin_serializer.data["username"]).password
        valid = check_password(
            admin_serializer.data["password"], hashed_password)
        if valid:
            payload = {
                'user_id': admin_serializer.data["username"],
                'exp': datetime.datetime.now() + datetime.timedelta(days=1),
                'token_type': 'access'
            }
            token = jwt.encode(payload, SECRET_KEY)
            return Response({
                "message": "token acquired",
                "data": {
                    "Authorization": token
                }
            })

        return Response({
            "message": "login failed",
            "data": [],
        })

    except Admin.DoesNotExist:
        admin_serializer.save()
        return Response({
            "message": "login failed",
            "data": [],
        })
