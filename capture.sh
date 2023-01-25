#!/bin/bash
# Runs on reboot, change this with "crontab -e"
cd ~/Documents/Code/senseair-s8-co2
while true
do
   python 24h_capture.py
   sleep 10
done
