from os import error
import jwt
from rest_framework.response import Response
from oats.settings import SECRET_KEY


def token_required(func):
    def inner(request, *args, **kwargs):
        try:
            token = request.headers.get('Authorization')
            payload = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
            if (payload and payload.get('exp')):
                return func(request, *args, **kwargs)
            return Response({
                "message": "invalid token",
                "data": []
            })
        except:
            return Response({
                "message": "invalid token",
                "data": []
            })
    return inner
