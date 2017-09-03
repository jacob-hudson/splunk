#!/usr/bin/env sh

# failing on errors and undefined variables
set -e -u

cd /home/vagrant
sudo yum -y install git
sudo mkdir /local
curl -o splunk.tgz https://download.splunk.com/products/splunk/releases/6.6.3/linux/splunk-6.6.3-e21ee54bc796-Linux-x86_64.tgz
sudo tar -xvzf splunk.tgz -C /local
sudo /local/splunk/bin/splunk start --accept-license --answer-yes
