#!/usr/bin/env bash
set -o errexit

export DJANGO_SETTINGS_MODULE=config.prod

pip install -r requirements/prod.txt

python manage.py collectstatic --no-input

python manage.py migrate