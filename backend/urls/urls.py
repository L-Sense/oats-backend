from django.urls import path
from backend.views import views
from backend.views.populate import populate

urlpatterns = [
    path('', views.hello_world, name="hello_world"),
    path('populate/', populate.populate_everything, name="populate"),
    path('truncate/', populate.truncate_everything, name="truncate")
]
