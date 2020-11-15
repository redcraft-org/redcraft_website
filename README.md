# Redcraft Website

Django (Python) website for RedCraft

## Setup the project

First, copy `.env.example` to `.env` and change the configuration as necessary in `.env`

Make sure the directory specified in `FILE_CACHE_PATH` exists

Create a DB named `redcraft` on your MySQL server.

### Linux

Run `./setup.sh`

### Windows

Create your virtual env: `python3 -m venv env`
And start your venv: `"env/Scripts/activate"`
Install  requirements: `pip install -r requirements.txt`
Make migration: `python manage.py makemigrations`
Migrate DB: `python manage.py migrate`
Compile sass: `python manage.py sass website/static/website/scss/ website/static/website/css/`

## Start development

Start the process to automatically compile assets: `python manage.py staticdev`

Start server: `python manage.py runserver`
