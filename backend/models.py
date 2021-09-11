from django.db import models
from django.utils.timezone import now

# Create your models here.
# IDs are commented as they need a default
# see https://stackoverflow.com/questions/25205228/django-autofield-with-primary-key-vs-default-pk
# and https://stackoverflow.com/questions/21128899/how-do-i-make-an-auto-increment-integer-field-in-django

class Department(models.Model):
    department_id = models.AutoField(primary_key=True)
    department_name = models.CharField(max_length=100)
    late_threshold = models.IntegerField()
    
    #ignore - testing purposes
    #def __str__(self):
    #    return self.department_name

class Employee(models.Model):
    employee_id = models.AutoField(primary_key=True)
    employee_name = models.CharField(max_length=100)
    department = models.ForeignKey(Department, on_delete=models.CASCADE) # deletes entries when referenced department is deleted
    image_1 = models.BinaryField() # allow blank values for images 2 and 3
    image_2 = models.BinaryField(blank=True)
    image_3 = models.BinaryField(blank=True)

class Admin(models.Model):
    admin_id = models.AutoField(primary_key=True)
    admin_name = models.CharField(max_length=100)
    username = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=100, null=False)

class Attendance(models.Model):
    STATUS = (
        ('Normal', 'Normal'),
        ('Abnormal', 'Abnormal'),
        ('Leave', 'Leave')
    )
    attendance_id = models.AutoField(primary_key=True)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE) # deletes entries when referenced employee is deleted
    date = models.DateField(default=now)
    in_time = models.TimeField(null=True)
    out_time = models.TimeField(null=True)
    status = models.CharField(max_length=100, choices=STATUS, default="Normal")