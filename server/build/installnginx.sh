sudo su

apt update

apt upgrade

apt install nginx

check server

systemctl status nginx

if you get an error

mkdir /etc/systemd/system/nginx.service.d

printf "[Service]\nExecStartPost=/bin/sleep 0.1\n" > /etc/systemd/system/nginx.service.d/override.conf

systemctl daemon-reload

systemctl restart nginx

systemctl status nginx