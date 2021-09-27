from datetime import date

from django.contrib.auth.models import User
from django.urls import reverse
from django.test import TestCase

from rest_framework.test import APIClient

from backend.models import *

class CreateUserTestCase(TestCase):

    def setup(self):
        client = APIClient()
        response = client.get("/populate/")
        self.assertEqual(response.status_code, 200)

class AdminTestCase(TestCase):

    def test_register(self):
        data = {"admin_name": "test", "username": "admin", "password": "password123"}
        response = self.client.post("/auth/register", data, format='json')
        self.assertEqual(response.status_code, 200)

    def test_login(self):
        data = {"username": "admin", "password": "password123"}
        response = self.client.post("/auth/login", data)
        self.assertEqual(response.status_code, 400)

class EmployeeTestCase(TestCase):

    def test_get_all(self):
        response = self.client.get("/employee")
        self.assertEqual(response.status_code, 200)

    def test_get_one(self):
        response = self.client.get("/employee/1")
        self.assertEqual(response.status_code, 200)

class AttendanceTestCase(TestCase):

    def test_get_all(self):
        response = self.client.get("/attendance")
        self.assertEqual(response.status_code, 200)

    def test_get_count_today(self):
        response = self.client.get("/attendance/counttoday")
        self.assertEqual(response.status_code, 200)

    def test_get_count_date(self):
        today = date.today().strftime("%d/%m/%Y")
        response = self.client.get("/attendance/countdate?date=" + today)
        self.assertEqual(response.status_code, 200)

    def test_get_today(self):
        response = self.client.get("/attendance/gettoday")
        self.assertEqual(response.status_code, 200)

    def test_get_date(self):
        today = date.today().strftime("%d/%m/%Y")
        response = self.client.get("/attendance/getdate?date=" + today)
        self.assertEqual(response.status_code, 200)

    def test_update_status(self):
        today = date.today().strftime("%d/%m/%Y")
        data = {"status": "Normal", "employee": 1, "date": today}
        response = self.client.post("/attendance/updatestatus", data, format='json')
        self.assertEqual(response.status_code, 400)