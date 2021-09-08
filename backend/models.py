from django.db import models
from django.utils.timezone import now

# Create your models here.
class Department(models.Model):
    department_name = models.CharField(max_length=100)
    late_threshold = models.IntegerField()
    
    #ignore - testing purposes
    #def __str__(self):
    #    return self.department_name

class Employee(models.Model):
    employee_name = models.CharField(max_length=100)
    department_id = models.IntegerField()
    image_1 = models.BinaryField()
    #Allow blank values for images 2 and 3
    image_2 = models.BinaryField(blank=True)
    image_3 = models.BinaryField(blank=True)

class Admin(models.Model):
    admin_name = models.CharField(max_length=100)
    username = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=100, null=False)

class Attendance(models.Model):
    employee_id = models.ForeignKey(Employee,on_delete=models.CASCADE)
    #Deletes entries when referenced employee is deleted
    date = models.DateField(default=now)
    time = models.TimeField(default=now)
    #Or datetime = models.DateTimeField(default=now)
    flag = models.BooleanField()
    #What is flag?
    attendance_status = models.BooleanField()