Step 1 — Installing Certbot

add-apt-repository ppa:certbot/certbot

apt-get update

apt install python-certbot-nginx

sudo systemctl reload nginx

Ebsure HTTPS allowed through the Firewall

The Nginx plugin will take care of reconfiguring Nginx and reloading the config whenever necessary:

sudo certbot --nginx -d acgtest.info -d www.acgtest.info

This runs certbot with the --nginx plugin, using -d to specify the names we’d like the certificate to be valid for.
