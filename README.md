
# ROME(Records Management System)

The Records Storage System is a Django-based web application designed to streamline records storage, management, and retrieval across multiple departments.


## Features
- User authentication and role-based access control.
- Department-specific record management.
- Secure document uploads and downloads.
- Email verification and two-factor authentication.
- Activity logs for monitoring record interactions.
- Responsive design for desktop and mobile usage.



## Technologies Used
- Backend: Django 5.1
- Frontend: HTML, CSS, JavaScript
- Database: MySQL
- Server: Waitress (for production serving)
- Additional Libraries:
     - django-allauth for authentication.
     - django-otp for two-factor authentication.

## Getting Started
#### Prerequisites
Before you begin, ensure you have the following installed:

- Python 3.8 or higher
- MySQL Server
- Git
- Virtualenv (recommended)

## Setup Instructions
#### 1. Clone the Repository:
``` git clone https://github.com/your-username/application-records-storage.git```

``` cd application-records-storage```

#### 2. Set Up a Virtual Environment:
```python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```
#### 3. Install Dependencies
```pip install -r requirements.txt
```

#### 4. Configure Database:

Update the DATABASES section in settings.py with your MySQL credentials:
```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'your_database_name',
        'USER': 'your_database_user',
        'PASSWORD': 'your_database_password',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}
```
#### 5. Apply Migrations:

```
python manage.py migrate
```

#### 6. Collect Static Files:
```
python manage.py collectstatic 
```

#### 7. Run the Development Server:
```
python manage.py runserver
```
Alternatively, for production:
```
waitress-serve --port=8000 records_storage.wsgi:application
```

#### 8. Access the Application:

Development: `http://127.0.0.1:8000`

Production: Replace `127.0.0.1` with your server's IP

## Usage

#### 1. Admin Panel:
- URL: ```/admin```
- Default login: Update via Django admin interface.

#### 2. User Authentication:
- Register and verify email.
- Enable two-factor authentication for added security.

#### 3. Record Management:
- Upload, categorize, and manage department-specific files.
## Static Files
- Static files (CSS, JS) are managed using Django's `collectstatic`.
- Ensure that a web server (e.g., Nginx) is configured to serve static files in production.
## License
This project is licensed under
[MIT](https://choosealicense.com/licenses/mit/)


## Contact

For questions or support:

Email: erickochieng830@gmail.com

GitHub:[Erick-Ochieng56](https://github.com/Erick-Ochieng56)
