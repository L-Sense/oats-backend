from django.urls import path
from . import views

urlpatterns = [
    path('', views.hello_world, name="hello_world"),
    path("<name>/", views.hello_world_name, name="hello_world_name"),
]
