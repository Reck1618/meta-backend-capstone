Meta Backend Capstone
This is a capstone project for the Meta Back-End Development course

# Commands

First, go to the project directory.

If using VENV:
python -m venv env
for linux - env\bin\activate
for windows - env\Scripts\activate
pip install django

If using PIPENV:
pipenv install

# Create SuperUser
python3 manage.py migrate 
python3 manage.py makemigrations
python manage.py createsuperuser

# Set up the database
create database reservations;
use reservations;
CREATE USER 'root_user'@'localhost' IDENTIFIED BY 'root';
GRANT ALL PRIVILEGES ON littlelemon.* TO 'root_user'@'localhost';

If you already have a database set up, change the setting in the settings.py file in the project folder.

# Run development server
python manage.py runserver

# Endpoints
For html page:
-> /api/

For API: 
-> /api/menu/
-> /api/menu/<int>
-> /api/bookings/

For Auth:
-> /api-token-auth/

Djoser endpoints:
-> /auth/

