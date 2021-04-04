#!/bin/bash

set -e

cd "${0%/*}"

rm -rf env

python3 -m venv env

source env/bin/activate

pip install -r requirements.txt

python manage.py migrate

python manage.py loaddata ./fixtures/data.json

python manage.py sass website/static/website/scss/ website/static/website/css/
