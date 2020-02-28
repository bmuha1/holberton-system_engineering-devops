# Allow login with holberton user and open a file without any error message
exec { 'hard':
  command => "sed -i -e 's/5/500/g' /etc/security/limits.conf",
  path    => '/bin'
}

exec { 'soft':
  command => "sed -i -e 's/4/500/g' /etc/security/limits.conf",
  path    => '/bin'
}
