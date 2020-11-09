sudo cp project1.service /etc/systemd/system/project1.service

sudo systemctl start project1
sudo systemctl enable project1

sudo ln -s /etc/nginx/sites-available/project1 /etc/nginx/sites-enabled

sudo nginx -t

sudo systemctl restart nginx