#!/bin/bash
echo 'install_dependencies'
cd /home/ubuntu/webapp/
pip3 install --upgrade -r requirements.txt
cd app/
pwd
ls -al
export FLASK_APP=app.py
pwd
sudo rm -rf migrations/
flask db init
flask db stamp head
flask db migrate
flask db upgrade
pwd