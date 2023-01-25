# Booking-System APP

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

3. Clone into Folder:
		<br> - `git clone <this repo url>`

4. change directory to project name:
		<br> - `cd Booking-System`

5. Install requirements:
		<br> - `pip install -r requirements.txt`

6. Create the database tables:
		<br> - `python manage.py makemigrations`
		<br> - `python manage.py migrate`

7. Run the development server:
		<br> - `python manage.py runserver`
8. Open website at:
		<br> - `http://127.0.0.1:8000/`

## Room for Improvement:
* Add user Login with user Authentication.
* Add background that complies with the requirements of the company or project at hand.
* Email confirmation once the room is booked.


