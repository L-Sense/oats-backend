from django.urls import path
from backend.views import views, attendance
from backend.views.populate import populate

urlpatterns = [
    path('', views.hello_world, name="hello_world"),
    path('populate/', populate.populate_everything, name="populate"),
    path('truncate/', populate.truncate_everything, name="truncate"),
    path('attendance/', attendance.get_all, name="view_attendance"),
    path('attendance/counttoday/', attendance.count_today, name="count_today"),
    path('attendance/countdate/', attendance.count_date, name="count_date"),
    path('attendance/gettoday/', attendance.get_today, name="get_today")
]
