from os import X_OK
from django.urls import path
from backend.views import views, attendance, employee, admin, image, scanner
from backend.views.populate import populate

urlpatterns = [
    path('', views.hello_world, name="hello_world"),
    path('populate/', populate.populate_everything, name="populate"),
    path('truncate/', populate.truncate_everything, name="truncate"),

    path('auth/check', admin.check, name="check"),
    path('auth/register', admin.register_admin, name="register_admin"),
    path('auth/login', admin.login_admin, name="login_admin"),

    path('employee', employee.get_all, name="view_employees"),
    path('employee/<str:employee_id>', employee.get_one, name="get_one"),
    path('employee/update/<str:employee_id>',
         employee.update, name="update_employee"),
    #path('employee/getimage', employee.get_image, name="view_image")

    path('attendance', attendance.get_all, name="view_attendance"),
    path('attendance/counttoday', attendance.count_today, name="count_today"),
    path('attendance/countdate', attendance.count_date, name="count_date"),
    path('attendance/gettoday', attendance.get_today, name="get_today"),
    path('attendance/getdate', attendance.get_date, name="get_date"),
    path('attendance/updatestatus',
         attendance.update_status, name="update_status"),

    path('image/', image.get_all, name="view_images"),
    path('scanner/', scanner.scanner_photo, name="scanner_photo"),
]
