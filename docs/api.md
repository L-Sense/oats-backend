# API

HTTP Methods used:
| HTTP Method | CRUD equivalent |
| ------------- | --------------- |
| POST | Create |
| GET | Read |
| PUT | Update |
| DELETE | Delete |

## Login Authentication

### Login

#### `POST /user/login`

Request Parameter:

    {
        "username": "<username>",
        "password": "<password>",
    }

Response Data:

    {
        "message": "success",
        "data":
            {
                "Authorization": "Token with 1 day expiry date",
            },
    }

## Admin Dashboard

### Check in and out count information

#### `GET /checkinandoutinformation`

Request Parameter: `null`

Response Data:

    {
        "message": "success",
        "data": {
            "checked_in_today_count": 7,
            "checked_out_today_count": 8,
            "total_employees": 29
        }
    }

### All employee information

#### `GET /employees/all`

Request Parameter: `null`

Response Data:

    {
        "message": "success",
        "data":
            [
                {
                    "id": "<employee ID>",
                    "employee_name": "Generic Name",
                    "department_id": "<department ID>",
                    "department": "Dept Name",
                },
            ]
    }

### Get specific employee information

#### `GET /employees/<employee id>`

Request Parameter: `null`

Response Data:

    {
        "message": "success",
        "data":
            [
                {
                    "id": "<employee ID>",
                    "employee_name": "Generic Name",
                    "department": "Dept Name",
                },
            ]
    }

    {
        "message": "fail",
        "error": "<error message .toString()>"
    }

### Update specific employee information

#### `PUT /employees/<employee id>`

Request Parameter:

    {
        "new_id": "<Can be Original ID>",
        "new_name": "<Can be Old name>",
        "new_department": "Can be Old Department>"
    }

Response Data:

    {
        "message": "success",
    }

    {
        "message": "fail",
        "error": "<error message .toString()>"
    }

### Create new employee

#### `POST /employees/`

Request Parameter:

    {
        "id": "<Employee ID>",
        "employee_name": "<Employee name>",
        "department_id": "<Existing Department ID>"
        "images":
            [
                "DESERIALISD IMAGE",
            ]
    }

Response Data:

    {
        "message": "success",
    }

    {
        "message": "fail",
        "error": "<error message .toString()>"
    }

### Get current date's attendance record

#### `GET /attendance/`

Request Parameter:

    {
        "id": "<new Date()>",
    }

Response Data:

    {
        "message": "success",
        "data":
            [
                {
                    "id": "<Employee ID>",
                    "employee_name": "<Employee name>",
                    "department": "Dept Name",
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

#### `GET /attendance/`

Request Parameter:

    {
        "id": "<Date>",
    }

Response Data:

    {
        "message": "success",
        "data":
            [
                {
                    "id": "<Employee ID>",
                    "employee_name": "<Employee name>",
                    "department": "Dept Name",
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

### Update attendance status flag of employee

#### `PUT /attendance/`

Request Parameter:

    {
        "id": "<Date>",
        "employee_id": "<Employee's ID>",
        "new_status_flag": "<Punctual, AWOL, Late, Leave, MC>"
    }

Response Data:

    {
        "message": "success",
    }

    {
        "message": "fail",
        "error": "<error message .toString()>"
    }

## Scanner Application

### Check In and Check Out employee information

#### `POST /checkin`

Request Parameter:

    {
        "image": "<base64 image string>",
        "isCheckin": boolean,
    }

Response Data:

    {
        "message": "success",
        "data":
            {
                "id": "<employee ID>",
                "employee_name": "Generic Name",
                "department_id": "<department ID>",
                "department": "Dept Name",
            },
    }
