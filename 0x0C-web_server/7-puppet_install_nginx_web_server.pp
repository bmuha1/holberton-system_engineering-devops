# Install and configure an Nginx server using Puppet
package { 'nginx':
  ensure => installed,
}

file { '/var/www/html/index.nginx-debian.html':
  content => 'Holberton School for the win!',
}

file_line { 'Redirect':
  ensure => 'present',
  path   => '/etc/nginx/sites-available/default',
  after  => 'listen 80 default server;',
  line   => 'rewrite ^/redirect_me https://www.youtube.com/watch?v=dQw4w9WgXcQ permanent;',
}

service { 'nginx':
  ensure  => running,
  require => Package['nginx'],
}
