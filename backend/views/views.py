from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

# Create your views here.


def hello_world(request):
    return JsonResponse({'message': f'hello'}, status=200)
    # return "hello world"

def hello_world_name(request, name):
    return JsonResponse({'message': f'hello, {name}'}, status=200)
    # return "hello world" + name
