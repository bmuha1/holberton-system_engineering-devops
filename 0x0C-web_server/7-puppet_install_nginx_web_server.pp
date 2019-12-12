# Install and configure an Nginx server using Puppet
exec {'/usr/bin/env apt-get -y update':}
exec {'/usr/bin/env apt-get -y install nginx':}
exec {'/usr/bin/env ufw allow \'Nginx HTTP\'':}
exec {'/usr/bin/env echo "Holberton School for the win!" > /var/www/html/index.nginx-debian.html':}
exec {'/usr/bin/env sed -i "/listen 80 default_server/a rewrite ^/redirect_me https://www.youtube.com/watch?v=dQw4w9WgXcQ permanent;" /etc/nginx/sites-available/default':}
exec {'/usr/bin/env service nginx restart':}
