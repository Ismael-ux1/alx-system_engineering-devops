# Create a Puppet manifest to kill a process named "killmenow"

exec { 'killmenow':
  command => 'pkill killmenow',
  path    => ['/usr/bin', '/usr/sbin'],
  onlyif  => 'pgrep -x killmenow',
}
