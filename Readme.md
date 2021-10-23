# CZ3002 L-SENSE's Office Attendance Taking System Repository

## How to run locally

Run `python manage.py runserver`

## libraries used

```
pip install deepface
pip install psycopg2-binary
pip install Django
pip install pyjwt
pip install django-cors-headers
pip install djangorestframework
pip install markdown
pip install django-filter
```

## Others

Protect login-required API:

- use `@token_required` wrapper before function to check if user is authorized before accessing th page.


Admin account:
- username: admin
- password: password1234
