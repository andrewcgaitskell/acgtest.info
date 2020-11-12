PROJECT_NAME='mqttclient1'
FRAMEWORK='gunicorn'

sudo systemctl stop mqttclient1
sudo systemctl disable mqttclient1

sudo cp /var/www/acgtest.info/server/gunicorn/mqttclient1/mqttclient1.service.txt /etc/systemd/system/mqttclient1.service

sudo systemctl daemon-reload

sudo systemctl start $PROJECT_NAME
sudo systemctl enable $PROJECT_NAME

sudo systemctl status $PROJECT_NAME

sudo cp /var/www/acgtest.info/server/build/acgtest.info /etc/nginx/sites-available/acgtest.info

sudo nginx -t

sudo systemctl restart nginx

sudo systemctl status nginx
