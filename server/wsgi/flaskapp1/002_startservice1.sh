sudo systemctl stop project1
sudo systemctl disable project1

sudo cp /var/www/acgtest.info/server/wsgi/flaskapp1/project1.service.txt /etc/systemd/system/project1.service

sudo systemctl start project1
sudo systemctl enable project1

sudo cp /var/www/acgtest.info/server/build/acgtest.info /etc/nginx/sites-available/acgtest.info

sudo nginx -t

sudo systemctl restart nginx

sudo systemctl status nginx
