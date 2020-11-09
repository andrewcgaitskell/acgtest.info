#!/bin/bash -x

sudo rm -rf /var/www/acgtest.info/server/wsgi/flaskapp1/env

python3 -m venv env

PWD=`pwd`

echo $PWD
activate () {
    . $PWD/env/bin/activate
}

activate

pip install wheel
pip install uwsgi
pip install Flask
pip install gunicorn
