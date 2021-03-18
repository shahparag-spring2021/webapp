#!/bin/bash
echo 'start_server'
cd /home/ubuntu/webapp/
pwd
export FLASK_APP=app.py
flask run -h 0.0.0.0 -p 5000
pwd