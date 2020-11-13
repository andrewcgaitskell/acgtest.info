sudo systemctl stop alexa1
sudo systemctl disable alexa1

sudo cp /var/www/acgtest.info/server/gunicorn/alexa1/alexa1.service.txt /etc/systemd/system/alexa1.service

sudo systemctl daemon-reload

sudo systemctl start alexa1
sudo systemctl enable alexa1

sudo systemctl status alexa1

sudo cp /var/www/acgtest.info/server/build/acgtest.info /etc/nginx/sites-available/acgtest.info

sudo nginx -t

sudo systemctl restart nginx

sudo systemctl status nginx
