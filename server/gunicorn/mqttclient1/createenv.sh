#!/usr/bin/env bash
PROJECT_NAME='mqttclient1'
FRAMEWORK='gunicorn'

sudo rm -rf /var/www/acgtest.info/server/$FRAMEWORK/$PROJECT_NAME/env

python3 -m venv env
set -e
source $PWD/env/bin/activate
pip install pandas
deactivate
