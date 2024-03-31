#!/usr/bin/env bash
#Creating a custom HTTP header response, but with Puppet
#The name of the custom HTTP header must be X-Served-By
#The value of the custom HTTP header must be the hostname of
#the server Nginx is running on
#Define a class for Nginx configuration

class nginx_header {

  # Get the server's hostname using a fact
  $server_hostname = Facter['fqdn']

  # Include the standard Nginx module
  include nginx

  # Define a resource to add the custom header
  nginx::header { 'X-Served-By':
    value => $server_hostname,
  }

  # Ensure the Nginx service is restarted after configuration changes
  nginx::service {
    ensure => running,
    enable => true,
  }
}
