#!/bin/bash

sudo rm -rf /var/www/acgtest.info/server/wsgi/flaskapp1/env

python3 -m venv env

;source /var/www/acgtest.info/server/wsgi/flaskapp1/env/bin/activate
