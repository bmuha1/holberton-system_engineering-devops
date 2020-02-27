# Increase the user limit from 15 to 4096
exec { 'limit':
  command => "sed -i -e 's/15/4096/g' /etc/default/nginx; service nginx restart",
  path    => ['/bin', '/usr/bin', '/usr/sbin']
}
