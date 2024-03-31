#!/usr/bin/env bash
#Creating a custom HTTP header response, but with Puppet
#The name of the custom HTTP header must be X-Served-By
#The value of the custom HTTP header must be the hostname of
#the server Nginx is running on
#Define a class for Nginx configuration

class nginx_custom_header {

  # Retrieve the server's hostname using Facter
  $server_hostname = Facter['fqdn']

  # Include the standard Nginx module
  include nginx

  # Configure the default server block
  nginx::resource { 'server':
    name   => 'default',
    ensure => present,
    listen => ['80 default_server'],
    
    location => {
      '/' => {
        # ... other configuration options (if needed)
        add_header => { 'X-Served-By' => $server_hostname },
      },
    },
  }

  # Ensure the Nginx service is restarted after configuration changes
  nginx::service {
    ensure => running,
    enable => true,
  }
}
