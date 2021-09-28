from datetime import datetime
from os import error
import jwt
from rest_framework.response import Response
from oats.settings import SECRET_KEY


def token_required(func):
    def inner(request, *args, **kwargs):
        try:
            token = request.headers.get('Authorization')
            payload = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
            payload_exp = datetime.fromtimestamp(payload.get('exp'))
            if (payload and datetime.now() < payload_exp):
                return func(request, *args, **kwargs)
            return Response({
                "message": "invalid token",
                "data": []
            }, 401)
        except:
            return Response({
                "message": "token not found",
                "data": []
            }, 401)
    return inner
