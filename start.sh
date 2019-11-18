#!/bin/sh
#cd /home/python-project/wx-mini
sudo pip3 install -U cos-python-sdk-v5
sudo pip3 install django-sslserver
sudo pip3 install django-cors-headers
sudo python3 manage.py makemigrations
sudo python3 manage.py migrate
sudo kill -9 $(lsof -i:8005 |awk '{print $2}' | tail -n 2)
nohup sudo python3 manage.py runsslserver 0.0.0.0:8005 --certificate 2949114_lyf.test.link-nemo.com.pem --key 2949114_lyf.test.link-nemo.com.key &

