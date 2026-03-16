#!/bin/bash
sleep 30

# Log startup
echo "Starting setup..." > /home/ubuntu/install-logs.txt
pwd >> /home/ubuntu/install-logs.txt

# Install Git, Python, and venv
sudo apt-get update -y
sudo apt-get install git python3 python3-pip python3-venv python3-full -y

# Clone your repo
cd /home/ubuntu
git clone https://github.com/umarfarouk16/Flask-Portfolio-AWS-ASG-ALB-HTTPS.git >> /home/ubuntu/install-logs.txt 2>&1

# Make run script executable and run
cd Flask-Portfolio-AWS-ASG-ALB-HTTPS
chmod u+x run.sh
./run.sh >> /home/ubuntu/install-logs.txt 2>&1

echo "Setup complete" >> /home/ubuntu/install-logs.txt
