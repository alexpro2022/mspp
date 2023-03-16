#!/bin/bash

if [ "$DEBUG"==True ]; then
    python manage.py makemigrations
    python manage.py migrate
    python manage.py fill_data
    python manage.py collectstatic --noinput

    if [ "$DJANGO_SUPERUSER_USERNAME" ]; then
        python manage.py createsuperuser \
            --noinput \
            --username $DJANGO_SUPERUSER_USERNAME \
            --email $DJANGO_SUPERUSER_EMAIL
    fi
fi
uvicorn config.asgi:application --host 0.0.0.0 --port 8000