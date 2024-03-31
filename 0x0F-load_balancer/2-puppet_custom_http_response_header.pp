#!/usr/bin/env bash
#Creating a custom HTTP header response, but with Puppet
#The name of the custom HTTP header must be X-Served-By
#The value of the custom HTTP header must be the hostname of
#the server Nginx is running on
#Define a class for Nginx configuration

exec { 'configure_nginx':
  # Update package lists and install Nginx
  command => 'apt-get update && apt-get install -y nginx',
  # Explain the purpose of this command
  # (consider splitting these into separate exec resources for clarity)
  # Adds the custom header to the default server block using sed
  command => '/bin/bash -c "apt-get update && apt-get install -y nginx;
              sudo sed -i \"/listen 80 default_server;/a add_header X-Served-By $HOSTNAME;\" /etc/nginx/sites-available/default"',
  # Use provider => shell to execute the command as a shell script
  provider => shell,
}

# Restart Nginx service after configuration changes
exec { 'restart_nginx':
  command => 'service nginx restart',
  # Explain the purpose of restarting Nginx
  provider => shell,
}
