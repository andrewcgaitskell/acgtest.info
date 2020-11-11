#!/bin/bash
PROJECT_NAME = 'mqttclient1'
FRAMEWORK = 'gunicorn'

sudo rm -rf /var/www/acgtest.info/server/$FRAMEWORK/$PROJECT_NAME/env

python3 -m venv env
