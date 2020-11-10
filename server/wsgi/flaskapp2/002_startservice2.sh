sudo systemctl stop project2
sudo systemctl disable project2

sudo cp /var/www/acgtest.info/server/wsgi/flaskapp1/project2.service.txt /etc/systemd/system/project2.service

sudo systemctl daemon-reload

sudo systemctl start project2
sudo systemctl enable project2

sudo systemctl status project2

sudo cp /var/www/acgtest.info/server/build/acgtest.info /etc/nginx/sites-available/acgtest.info

sudo nginx -t

sudo systemctl restart nginx

sudo systemctl status nginx
