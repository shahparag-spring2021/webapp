#!/bin/bash
cd /home/ubuntu/

echo 'before_install'
sudo kill $(sudo lsof -t -i:5000);
pwd
# sudo rm -rf *-cleanup
sudo rm -rf /home/ubuntu/webapp/