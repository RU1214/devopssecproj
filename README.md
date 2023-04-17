## Introduction
DevOpsSec Project is a simple application developed using Django and Python that performs basic CRUD operation (to create/list/modify and delete Employee). SQLite is used for persisting data. 

### Run Server
`python3 manage.py runserver`
```
Watching for file changes with StatReloader
Performing system checks...

System check identified no issues (0 silenced).
April 16, 2023 - 22:47:45
Django version 4.2, using settings 'devopssecproj.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.
```

## Navigating the Application
Create an Employee Record: http://127.0.0.1:8000/emp
<img width="1514" alt="image" src="https://user-images.githubusercontent.com/124355591/232349032-a80b4acd-70a8-4393-aae4-a9d357c2ac17.png">

Retrieve Employees: http://127.0.0.1:8000/ or http://127.0.0.1:8000/show

Delete an Employee Record: Click `Delete` button next to the Employee on `Retrieve Employees` screen
<img width="1507" alt="image" src="https://user-images.githubusercontent.com/124355591/232348894-f99c908e-6328-4cbc-aaa5-939b8f0b8b3e.png">

Update an Employee Record: http://127.0.0.1:8000/edit/1
<img width="1510" alt="image" src="https://user-images.githubusercontent.com/124355591/232348953-1c0affaf-14ac-4fe2-beff-1038bf2d5e3b.png">

Django administration: http://127.0.0.1:8000/admin/
<img width="1570" alt="image" src="https://user-images.githubusercontent.com/124355591/232349108-4148d268-4895-410a-9b45-46f16d34273d.png">

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
