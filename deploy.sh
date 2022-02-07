#!/bin/sh
source sandbox/bin/activate
sudo git pull origin master
sudo python -m pip install -r requirements.txt
python3.9 manage.py makemigrations
python3.9 manage.py migrate
python3.9 manage.py collectstatic
sudo systemctl restart nginx
sudo systemctl restart gunicorn