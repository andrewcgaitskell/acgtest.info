#!/usr/bin/env bash
PROJECT_NAME='api1'
FRAMEWORK='gunicorn'

sudo rm -rf /var/www/acgtest.info/server/$FRAMEWORK/$PROJECT_NAME/env

python3 -m venv env
set -e
source $PWD/env/bin/activate

pip install eventlet

pip install configparser

pip install pandas
pip install wheel
pip install Flask
pip install gunicorn
pip install flask_mqtt
pip install eventlet

deactivate
