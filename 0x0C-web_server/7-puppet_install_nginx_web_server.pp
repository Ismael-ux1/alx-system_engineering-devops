# Install Nginx
package { 'nginx':
  ensure => 'installed',
}

# Create an Nginx virtual host configuration
file { '/etc/nginx/sites-available/default':
  ensure => 'file',
  content => template('nginx/default.erb'),
  require => Package['nginx'],
}

# Enable the default site
file { '/etc/nginx/sites-enabled/default':
  ensure => 'link',
  target => '/etc/nginx/sites-available/default',
  require => File['/etc/nginx/sites-available/default'],
}

# Ensure Nginx is running and enabled
service { 'nginx':
  ensure => 'running',
  enable => true,
  require => [Package['nginx'], File['/etc/nginx/sites-enabled/default']],
}
