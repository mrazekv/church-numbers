#!/bin/bash

GATEWAY=192.168.4.1

# Function to ping the gateway
ping_gateway() {
  ping -c 1 $GATEWAY > /dev/null 2>&1
  return $?
}

# Function to restart the network interface
restart_network() {
  sudo systemctl restart networking
}

# Function to reboot the system
reboot_system() {
  sudo reboot
}

# Main script
if ping_gateway; then
  echo "Gateway is reachable"
else
  echo "Gateway is not reachable, restarting network interface"
  restart_network
  sleep 10
  if ping_gateway; then
    echo "Gateway is reachable after restarting network"
  else
    echo "Gateway is still not reachable, rebooting system"
    reboot_system
  fi 
fi