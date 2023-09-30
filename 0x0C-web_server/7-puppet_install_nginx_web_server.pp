

# Install Nginx web server
package { 'nginx':
  ensure => installed,
}

# Create the Nginx configuration file for the main server block
file { '/etc/nginx/sites-available/default':
  ensure  => file,
  content => "server {
    listen 80 default_server;
    listen [::]:80 default_server;
    root /var/www/html;
    index index.html;

    location /redirect_me {
        return 301 https://www.youtube.com/watch?v=QH2-TGUlwu4;
    }

    location / {
        try_files $uri $uri/ @default;
    }

    location @default {
        return 200 'Hello World!';
        add_header Content-Type text/plain;
    }
}\n",
  require => Package['nginx'],
}

# Create the HTML file for the main server block
file { '/var/www/html/index.html':
  ensure  => file,
  content => 'Hello World!',
}

# Create a symlink for the server block to enable it
file { '/etc/nginx/sites-enabled/default':
  ensure => link,
  target => '/etc/nginx/sites-available/default',
  require => File['/etc/nginx/sites-available/default'],
}

# Remove the default server block symlink (if it exists)
file { '/etc/nginx/sites-enabled/000-default':
  ensure => absent,
}

# Ensure Nginx service is running and enabled
service { 'nginx':
  ensure  => 'running',
  enable  => true,
  require => [
    Package['nginx'],
    File['/etc/nginx/sites-enabled/default'],
  ],
}

