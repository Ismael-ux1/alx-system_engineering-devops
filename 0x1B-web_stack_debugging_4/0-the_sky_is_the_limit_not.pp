# Puppet manifest to increase file descriptor limit for Nginx

# Increase the ULIMIT of the default file
exec { 'increase_file_descriptor_limit':
  command => 'sed -i "s/15/5000/" /etc/default/nginx',
  path    => '/usr/local/bin/:/bin/',
  notify  => Exec['restart_nginx'],  # Notify the restart exec when this one changes
}

# Restart Nginx only when the file descriptor limit is increased
exec { 'restart_nginx':
  command     => '/etc/init.d/nginx restart',
  path        => '/etc/init.d/',
  refreshonly => true,  # This ensures that the restart only occurs when notified
}
