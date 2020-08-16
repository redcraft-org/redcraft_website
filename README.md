# Redcraft Website

Django (Python) website for RedCraft

### Setup the project

First, creates the `.env` file with the help of `.env.example`.

Create a DB `redcraft` in your mysql server.

Create your virtual env: `python3 -m venv env`
And start your venv:
    Window: `"env/Scripts/activate"`
    Linux: `source env/bin/activate`

Install  requirements: `pip install -r requirement.txt`

Migrate DB: `python manage.py migrate`

Compile sass: `python manage.py sass website/static/website/scss/ website/static/website/css/`

Start server: `python manage.py runserver`
