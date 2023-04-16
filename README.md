## Introduction
DevSecOpsProject is a simple application developed using Django and Python that performs basic CRUD operation (to create/list/modify and delete Employee). SQLite is used for persisting data. 

### Run Server
`python3 manage.py runserver`
```
Watching for file changes with StatReloader
Performing system checks...

System check identified no issues (0 silenced).
April 16, 2023 - 22:47:45
Django version 4.2, using settings 'devsecopsproj.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.
```

### Create Django Admin User
`python manage.py createsuperuser`
```
Username (leave blank to use 'naseemsultana'): admin
Email address: admin@devopssec.project.com
Password: 
Password (again): 
Superuser created successfully.
```
### Reset Password
`python manage.py changepassword <user_name>`
```
Changing password for user 'admin'
Password: 
Password (again): 
Password changed successfully for user 'admin'
```
