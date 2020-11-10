sudo systemctl stop dashboards1
sudo systemctl disable dashboards1

sudo cp /var/www/acgtest.info/server/gunicorn/dashboards1/dashboards1.service.txt /etc/systemd/system/dashboards1.service

sudo systemctl daemon-reload

sudo systemctl start dashboards1
sudo systemctl enable dashboards1

sudo systemctl status dashboards1

sudo cp /var/www/acgtest.info/server/build/acgtest.info /etc/nginx/sites-available/acgtest.info

sudo nginx -t

sudo systemctl restart nginx

sudo systemctl status nginx
