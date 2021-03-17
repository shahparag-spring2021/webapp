#!/bin/bash
cd /home/ubuntu/webapp/

# sudo kill -9 $(sudo lsof -t -i:4000);
# sudo nohup npm start > /dev/null 2> /dev/null < /dev/null &
sudo export FLASK_APP=app.py
sudo flask run -h 0.0.0.0 -p 5000
