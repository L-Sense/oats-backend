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
            })
        except:
            return Response({
                "message": "server error",
                "data": []
            })
    return inner
