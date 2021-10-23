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

#### `POST /auth/register`

Request Parameter:

    {
        "admin_name": <admin_name>,
        "username": <username>,
        "password": <password>,
    }

Response Data:

    {
        "message": "admin registered",
        "data": []
    }

### Login

#### `POST /auth/login`

Request Parameter:

    {
        "username": <username>,
        "password": <password>,
    }

Response Data:

    {
        "message": "token acquired",
        "data":
            {
                "Authorization": <Token with 1 day expiry date>,
            },
    }

### Authorize User

#### `GET /auth/check`

Request Parameter:

    {}

Response Data:

    {
        "message": "authorized",
        "data":[]
    }

## Admin Dashboard

### All employee information

#### `GET /employee`

Request Parameter:

    {}

Response Data:

    {
        "message": "employees retrieved",
        "data":
            [
                {
                    "employee_id": <employee_id>,
                    "employee_name": <employee_name>,
                    "department_id": <department_id>,
                    "department_name": <department_name>
                },
            ]
    }

### Get specific employee information

#### `GET /employee/<employee id>`

Request Parameter:
    
    {}

Response Data:

    {
        "message": "employee retrieved",
        "data":
            [
                {
                    "employee_id": <employee_id>,
                    "employee_name": <employee_name>,
                    "department_id": <department_id>,
                    "department_name": <department_name>
                },
            ]
    }

### Update specific employee information

#### `PUT /employee/<employee_id>`

Request Parameter:

    {
        "employee_name": <employee_name>,
        "department_id": <department_id>
    }

Response Data:

    {
        "message": "employee data updated",
        "data": <employee_data>
    }

### Create new employee

#### `POST /employee`

Request Parameter:

    {
        "employee_id": <employee_id>,
        "employee_name": <employee_name>,
        "department_id": <department_id>
        "images": {
            "image_1": <byte64 image string>,
            "image_2": <byte64 image string>,
            "image_3": <byte64 image string>
        }
    }

Response Data:

    {
        "message": "new employee created",
        "data": <employee_data>
    }

### Check in and out count information today

#### `GET /attendance/counttoday`

Request Parameter:

    {}

Response Data:

    {
        "message": "attendance retrieved",
        "data": {
            "checked_in_today_count": 7,
            "checked_out_today_count": 8,
            "total_employees": 29
        }
    }

### Check in and out count information based on a given date

#### `GET /attendance/countdate`

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

#### `GET /attendance/gettoday`

Request Parameter:

    {}

Response Data:

    {
        "message": "attendance retrieved",
        "data":
            [
                {
                    "employee_id": <employee_id>,
                    "employee_name": <employee_name>,
                    "department_name": <department_name>,
                    "in_time": <Properly formatted time OR None>,
                    "out_time": <Properly formatted time OR None>,
                    "status": <Normal OR Abnormal OR Leave OR No Show>,
                }
            ]
    }

### Get specific date's attendance record

#### `GET /attendance/getdate`

Request Parameter:

    {
        "date": <date>,
    }

Response Data:

    {
        "message": "attendance retrieved",
        "data":
            [
                {
                    "employee_id": <employee_id>,
                    "employee_name": <employee_name>,
                    "department_name": <department_name>,
                    "in_time": <Properly formatted time OR None>,
                    "out_time": <Properly formatted time OR None>,
                    "status": <Normal OR Abnormal OR Leave OR No Show>,
                }
            ]
    }

### Update attendance status manually

#### `POST /attendance/updatestatus`

Request Parameter:

    {
        "date": <date>,
        "employee_id": <employee_id>,
        "status": <status>
    }

Response Data:

    {
        "message": "attendance retrieved",
        "data":
            [
                {
                    "employee_id": <employee_id>,
                    "employee_name": <employee_name>,
                    "department_name": <department_name>,
                    "in_time": <Properly formatted time OR None>,
                    "out_time": <Properly formatted time OR None>,
                    "status": <Normal OR Abnormal OR Leave OR No Show>,
                }
            ]
    }

### Add attendance record of employee manually

#### `POST /attendance`

Request Parameter:

    {
        "date": <date>,
        "employee": <employee_id>,
        "status": <valid_status_flag>
    }

Response Data:

    {
        "message": "attendance recorded",
        "attendance_id": <attendance_id>
    }

### Delete attendance status flag of employee manually

#### `DELETE /attendance`

Request Parameter:

    {
        "employee_id": <employee_id>,
        "date": <date>,
    }

Response Data:

    {
        "message": "attendance record deleted successfully",
        "attendance_id": <attendance_id>
    }

## Scanner Application

### Check In and Check Out employee information

#### `POST /scanner`

Request Parameter:

    {
        "image": <base64 image string>,
        "isCheckin": <boolean>,
    }

Response Data:

    {
        "message": "employee found",
        "data":
            {
                "id": <employee_id>,
                "employee_name": <employee_name>,
                "department_id": <department_id>,
                "department_name": <department_name>,
            },
    }


## Image Retrieval

### Retrieve all the images in the database to be stored locally on server

#### `GET /image`

Request Parameter:

    {}

Response Data:

    {
        "message": "images retrieved",
        "data":
            [
                {
                    "image": <base64 image string>,
                    "file_name": <file_name>
                }
            ]
    }
