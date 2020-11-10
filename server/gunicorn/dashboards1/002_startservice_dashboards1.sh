sudo systemctl stop project3
sudo systemctl disable project3

sudo cp /var/www/acgtest.info/server/gunicorn/flaskapp3/project3.service.txt /etc/systemd/system/project3.service

sudo systemctl daemon-reload

sudo systemctl start project3
sudo systemctl enable project3

sudo systemctl status project3

sudo cp /var/www/acgtest.info/server/build/acgtest.info /etc/nginx/sites-available/acgtest.info

sudo nginx -t

sudo systemctl restart nginx

sudo systemctl status nginx
