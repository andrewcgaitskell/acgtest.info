Step 1 — Installing Certbot

add-apt-repository ppa:certbot/certbot

apt-get update

apt install python-certbot-nginx

sudo systemctl reload nginx

Ebsure HTTPS allowed through the Firewall

The Nginx plugin will take care of reconfiguring Nginx and reloading the config whenever necessary:

sudo certbot --nginx -d acgtest.info -d www.acgtest.info

This runs certbot with the --nginx plugin, using -d to specify the names we’d like the certificate to be valid for.



- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
Select the appropriate number [1-2] then [enter] (press 'c' to cancel): 2
Redirecting all traffic on port 80 to ssl in /etc/nginx/sites-enabled/acgtest.info
Redirecting all traffic on port 80 to ssl in /etc/nginx/sites-enabled/acgtest.info
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
Congratulations! You have successfully enabled https://acgtest.info and
https://www.acgtest.info

You should test your configuration at:

https://www.ssllabs.com/ssltest/analyze.html?d=acgtest.info

https://www.ssllabs.com/ssltest/analyze.html?d=www.acgtest.info
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
IMPORTANT NOTES:                                                                                                                                                                                                               
 - Congratulations! Your certificate and chain have been saved at:                                                                                                                                                             
   /etc/letsencrypt/live/acgtest.info/fullchain.pem

Your key file has been saved at:
   /etc/letsencrypt/live/acgtest.info/privkey.pem

Your cert will expire on 2021-02-08. To obtain a new or tweaked
   version of this certificate in the future, simply run certbot again
   with the "certonly" option. To non-interactively renew *all* of
   your certificates, run "certbot renew"

- Your account credentials have been saved in your Certbot
   configuration directory at /etc/letsencrypt. You should make a
   secure backup of this folder now. This configuration directory will
   also contain certificates and private keys obtained by Certbot so
   making regular backups of this folder is ideal.

- If you like Certbot, please consider supporting our work by:
   Donating to ISRG / Let's Encrypt:   https://letsencrypt.org/donate
   Donating to EFF:                    https://eff.org/donate-le

- We were unable to subscribe you the EFF mailing list because your
   e-mail address appears to be invalid. You can try again later by
   visiting https://act.eff.org.
   
   
