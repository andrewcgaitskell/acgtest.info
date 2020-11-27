#!/usr/bin/env bash
PROJECT_NAME='mqttclient1'
FRAMEWORK='gunicorn'

sudo rm -rf /var/www/acgtest.info/server/$FRAMEWORK/$PROJECT_NAME/env

python3 -m venv env
set -e
source $PWD/env/bin/activate

pip install wheel

pip install dash
pip install dash_core_components
pip install dash_html_components
pip install plotly

pip install configparser

pip install pandas

pip install uwsgi
pip install Flask
pip install gunicorn
pip install pandas
pip install flask_mqtt
pip install flask_socketio
pip install flask_bootstrap
pip install eventlet

pip install paho-mqtt

deactivate
