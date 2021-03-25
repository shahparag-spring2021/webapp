#!/bin/bash
echo 'start_server'
cd /home/ubuntu/webapp/
pwd

sudo /opt/aws/amazon-cloudwatch-agent/bin/amazon-cloudwatch-agent-ctl \
    -a fetch-config \
    -m ec2 \
    -c file:/home/ubuntu/webapp/cloudwatch-config.json \
    -s

cd /home/ubuntu/webapp/app/
touch csye6225.log
sudo chmod 777 csye6225.log
pwd

export FLASK_APP=app.py
flask db stamp head
flask db migrate
flask db upgrade
flask run -h 0.0.0.0 -p 5000 > /dev/null 2> /dev/null < /dev/null &