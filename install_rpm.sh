#!/usr/bin/env sh

# failing on errors and undefined variables
set -e -u

cd /home/vagrant
sudo yum -y install java git
curl https://download.splunk.com/products/splunk/releases/6.6.3/linux/splunk-6.6.3-4b804538c686-linux-2.6-x86_64.rpm -o splunk.rpm
chmod 744 splunk.rpm
yes | sudo rpm -i splunk.rpm
sudo /opt/splunk/bin/splunk start --accept-license --answer-yes
