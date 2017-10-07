#!/usr/bin/env sh

# failing on errors and undefined variables
set -e -u

cd /home/vagrant
curl -o splunk.rpm https://download.splunk.com/products/splunk/releases/7.0.0/linux/splunk-7.0.0-c8a78efdd40f-linux-2.6-x86_64.rpm
chmod 744 splunk.rpm
yes | sudo rpm -i splunk.rpm
sudo /opt/splunk/bin/splunk start --accept-license --answer-yes
