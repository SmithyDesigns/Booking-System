Bookings System App

A basic HTML, CSS template using Bootstrap and Django Form templating.

## Table of Contents
* [General Info](#general-information)
* [Technologies Used](#technologies-used)
* [Features](#features)
* [Setup](#setup)
* [Usage](#usage)
* [Room for Improvement](#room-for-improvement)
* [Acknowledgements](#acknowledgements)
* [Contact](#contact)

## General Information:

This is a basic html template for a website using Bootstrap and Django templating. 

It includes a navigation bar with links to the home page and reservation and rental creation pages, as well as Django template tags for loading static files and linking to specific views within a Django app.
 
  This template can be used as a starting point for a website using Bootstrap and Django. The template tags and file paths will need to be adjusted to match the specific project's file structure and views.
All html pages inherit from Base.html

## Technologies Used:
* Bootstrap CSS - 4.5.2
* Django templating

## Features:
* Navigation bar with links to the home page and reservation and rental creation pages
* Django template tags for loading static files and linking to specific views within a Django app

## Setup:
This template does not require any specific setup, as it is a basic HTML template. 

However, the template tags and file paths will need to be adjusted to match the specific project's file structure and views.

## Usage:
To start a Django project from scratch, you can use the following commands:

VS code setup. 
1. Create a new directory for your project and navigate into it:
		<br> - `mkdir myproject`
		<br> - `cd myproject`

2. Create a virtual environment and activate it:
		<br> - `python3 -m venv venv`
		<br> - `source venv/bin/activate`

3. Install Django in your virtual environment:
		<br> - `pip install Django`

4. Install Dependencies:
		<br> - `pip install requirements.txt`

5. Create a new Django project:
		<br> - `django-admin startproject myproject .`

6. Create a new Django app within your project:
		<br> - `python manage.py startapp myapp`

7. Run the development server:
		<br> - `python manage.py runserver`

8. Create the database tables:
		<br> - `python manage.py makemigrations`
		<br> - `python manage.py migrate`

9. Create a superuser account:
		<br> - `python manage.py createsuperuser`


After you run these commands, you should have a new Django project set up and ready to go. You can start creating models, views, and templates to build your application.

 
Also, you can use the command django-admin startproject <project_name> to create a new project, and python manage.py startapp <app_name> to create a new app inside a project.

10. Make migrations to make changes to apply changes to the database:
		<br> - `python3 manage.py migrate`
11. Then run Django server:
 		<br> - `python3 manage.py runserver`


## Room for Improvement:
* Add user Login with user Authentication.
* Add background that complies with the requirements of the company or project at hand.
* Email confirmation once the room is booked.

