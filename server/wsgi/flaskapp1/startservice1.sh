sudo cp /var/www/acgtest.info/server/wsgi/flaskapp1/project1.service.txt /etc/systemd/system/project1.service

sudo systemctl start project1
sudo systemctl enable project1

sudo cp /var/www/acgtest.info/server/wsgi/flaskapp1/project1-sites-available.txt /etc/nginx/sites-available/project1

sudo ln -s /etc/nginx/sites-available/project1 /etc/nginx/sites-enabled

sudo nginx -t

sudo systemctl restart nginx

sudo systemctl status nginx
