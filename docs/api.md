# API

HTTP Methods used:
| HTTP Method | CRUD equivalent |
| ------------- | --------------- |
| POST | Create |
| GET | Read |
| PUT | Update |
| DELETE | Delete |

## Authentication

### Register

#### `POST /admin/register`

Request Parameter:

    {
        "admin_name": "<admin_name>",
        "username": "<username>",
        "password": "<password>",
    }

Response Data:

    {
        "message": "admin registered",
        "data": []
    }

### Login

#### `POST /admin/login`

Request Parameter:

    {
        "username": "<username>",
        "password": "<password>",
    }

Response Data:

    {
        "message": "token acquired",
        "data":
            {
                "Authorization": "Token with 1 day expiry date",
            },
    }

## Admin Dashboard

### All employee information

#### `GET /employee`

Request Parameter: `null`

Response Data:

    {
        "message": "employees retrieved",
        "data":
            [
                {
                    "employee_id": "<employee_id>",
                    "employee_name": "<employee_name>",
                    "department_id": "<department_id>",
                    "department_name": "<department_name>"
                },
            ]
    }

### Get specific employee information

#### `GET /employee/<employee id>`

Request Parameter: `null`

Response Data:

    {
        "message": "employee retrieved",
        "data":
            [
                {
                    "employee_id": "<employee_id>",
                    "employee_name": "<employee_name>",
                    "department_id": "<department_id>",
                    "department_name": "<department_name>"
                },
            ]
    }

    {
        "message": "fail",
        "error": "<error message .toString()>"
    }

### Update specific employee information

#### `PUT /employee/<employee_id>`

Request Parameter:

    {
        "employee_name": "<employee_name>",
        "department_id": "<department_id>"
    }

Response Data:

    {
        "message": "employee updated",
    }

    {
        "message": "fail",
        "error": "<error message .toString()>"
    }

### Create new employee

#### `POST /employee`

Request Parameter:

    {
        "employee_id": "<employee_id>",
        "employee_name": "<employee_name>",
        "department_id": "<department_id>"
        "images": {
            "image_1": "<byte64 image string>",
            "image_2": "<byte64 image string>",
            "image_3": "<byte64 image string>"
        }
    }

Response Data:

    {
        "message": "employee added",
    }

    {
        "message": "fail",
        "error": "<error message .toString()>"
    }

### Check in and out count information

#### `GET /attendance/checkinout`

Request Parameter:

    {
        "date": "<date>",
    }

Response Data:

    {
        "message": "attendance retrieved",
        "data": {
            "checked_in_today_count": 7,
            "checked_out_today_count": 8,
            "total_employees": 29
        }
    }

### Get current date's attendance record

#### `GET /attendance/aggregate`

Request Parameter:

    {
        "date": "<date>",
    }

Response Data:

    {
        "message": "attendance retrieved",
        "data":
            [
                {
                    "employee_id": "<employee_id>",
                    "employee_name": "<employee_name>",
                    "department_id": "<department_id>",
                    "department_name": "<department_name>",
                    "check_in_time": "<Properly formatted time OR - >",
                    "check_out_time": "<Properly formatted time OR - >",
                    "status_flag": "<Punctual, AWOL, Late, Leave, MC>",
                }
            ]
    }

    {
        "message": "fail",
        "error": "<error message .toString()>"
    }

### Get specific date's attendance record

#### `GET /attendance/date`

Request Parameter:

    {
        "date": "<date>",
    }

Response Data:

    {
        "message": "attendance retrieved",
        "data":
            [
                {
                    "attendance_id": "<attendance_id>,
                    "employee_id": "<employee_id>",
                    "employee_name": "<employee_name>",
                    "department_id": "<department_id>",
                    "department_name": "<department_name>",
                    "check_in_out": "<boolean>",
                    "status_flag": "<Punctual, AWOL, Late, Leave, MC>",
                }
            ]
    }

    {
        "message": "fail",
        "error": "<error message .toString()>"
    }

### Update attendance status flag of employee manually

#### `POST /attendance`

Request Parameter:

    {
        "date": "<date>",
        "employee_id": "<employee_id>",
        "date": "<date>",
        "time": "<time>",
        "check_in_out": "<boolean>",
        "status_flag": "<boolean>"
    }

Response Data:

    {
        "message": "attendance successfully added",
        "attendance_id": "<attendance_id>"
    }

    {
        "message": "fail",
        "error": "<error message .toString()>"
    }

### Delete attendance status flag of employee manually

#### `DELETE /attendance`

Request Parameter:

    {
        "attendance_id": "<attendance_id>"
    }

Response Data:

    {
        "message": "success",
        "attendance_id": "<attendance_id>"
    }

    {
        "message": "fail",
        "error": "<error message .toString()>"
    }

## Scanner Application

### Check In and Check Out employee information

#### `POST /scanner`

Request Parameter:

    {
        "image": "<base64 image string>",
        "isCheckin": "<boolean>",
    }

Response Data:

    {
        "message": "employee found",
        "data":
            {
                "id": "<employee_id>",
                "employee_name": "<employee_name>",
                "department_id": "<department_id>",
                "department_name": "<department_name>",
            },
    }

    {
        "message": "attendance already recorded",
        "status": 500
    }

## Image Retrieval

### Retrieve all the images in the database to be stored locally

#### `GET /image`

Request Parameter: `null`

Response Data:

    {
        "message": "images retrieved",
        "data":
            [
                {
                    "image": "<base64 image string>",
                    "file_name": <file_name>
                }
            ]
    }