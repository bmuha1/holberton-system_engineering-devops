# Using Puppet, create a manifest that kills a process named killmenow.

exec { 'Kill a process':
  command => 'pkill killmenow',
  path    => '/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games',
}
