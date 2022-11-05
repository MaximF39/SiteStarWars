apt-get update
sudo apt-get install certbot
apt-get install python-certbot-nginx
nginx -t && nginx -s reload

certbot --nginx -d serverstarwars.site -d www.serverstarwars.site
