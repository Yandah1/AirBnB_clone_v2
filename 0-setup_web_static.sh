#!/usr/bin/env bash
# script that sets up your web servers for the deployment of web_static

if ! command -v nginx &> /dev/null; then
    sudo apt-get update
    sudo apt-get install -y nginx
    sudo ufw allow 'Nginx HTTP'
fi

sudo mkdir -p /data/web_static/releases/test /data/web_static/shared
echo "<html>
 <head>
 </head>
 <body>
  Holberton School
 </body>
</html>" | sudo tee /data/web_static/releases/test/index.html > /dev/null
if [ -d "/data/web_static/current" ];
then
    echo "path /data/web_static/current exists"
    sudo rm -rf /data/web_static/current;
fi;
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current

sudo chown -R ubuntu:ubuntu /data/

sudo sed -i '/listen 80 default_server/a  location /hbnb_static{ alias /data/web_static/current;}' /etc/nginx/sites-enabled/default

sudo service nginx restart
