#!/bin/bash
echo 'start_server'
cd /home/ubuntu/webapp/app/
pwd
export FLASK_APP=app.py
flask run -h 0.0.0.0 -p 5000 > /dev/null 2> /dev/null < /dev/null &