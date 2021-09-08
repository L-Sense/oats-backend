# List of APIs required by front-end

HTTP Methods used:
First Header  | Second Header
------------- | -------------
POST | Create
GET | Content Cell
PUT | Content Cell
DELETE | Content Cell

## Login Authentication


## Admin Dashboard

### Check In and Out Count information
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
#### `GET /employees/:id`
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
#### `PUT /employees/:id`
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


## Scanner Application
