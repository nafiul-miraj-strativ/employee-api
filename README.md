# DRF Employee Name and Email API

This is a RESTful API built using Django REST Framework (DRF) for managing employee names and email addresses.

## Features

Create, list, retrieve, update and delete employee records


## To run this locally
### 1. Clone the repository

```bash
git clone https://github.com/nafiul-miraj-strativ/employee-api
```

### 2. Create a virtual environment

```bash
    python3 -m venv venv
```
### 3. For macos/linux

```bash
    source venv/bin/activate
```
or for windows

```bash
    venv/scripts/activate
```
### 4. Install the dependencies
```bash
pip install -r requirements.txt
```

## PostgreSQL Database Configuration

This project uses **PostgreSQL** as the default database. Follow the steps below to configure it properly.

### Prerequisites

- PostgreSQL installed and running
- A database and user created ( `myproject`)

###  Fix the database according to your credentials

```bash
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'myproject',
        'USER': 'myuser',
        'PASSWORD': 'password',
        'HOST': 'localhost',
        'PORT': '',
    }
}
```
### 5. Apply migrations
```bash
python manage.py makemigrations
python manage.py migrate
```
### 6. Run server
```bash
python manage.py runserver
```
### 7. Go to this url and other simillar ones 
```bash
http://127.0.0.1:8000/api/
```



