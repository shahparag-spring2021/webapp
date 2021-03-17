#!/bin/bash
cd /home/ubuntu/webapp/

sudo apt-get install python3-setuptools
sudo python3 -m easy_install install pip
sudo apt install python3-flask -y
sudo pip3 install --upgrade -r requirements.txt
