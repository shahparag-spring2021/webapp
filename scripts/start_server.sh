#!/bin/bash
cd /home/ubuntu/webapp/

# sudo kill $(sudo lsof -t -i:5000)
cd app/
sudo export FLASK_APP=app.py
sudo flask run -h 0.0.0.0 -p 5000