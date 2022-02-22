python3.9 manage.py migrate

gunicorn --bind 0.0.0.0:8000 --reload licensing_platform.wsgi:application --workers=4