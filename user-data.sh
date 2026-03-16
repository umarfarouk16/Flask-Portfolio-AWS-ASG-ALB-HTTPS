#!/bin/bash
sleep 30

# Log startup
echo "Starting setup..." > /home/ec2-user/install-logs.txt
pwd >> /home/ec2-user/install-logs.txt

# Install Git and Python
sudo yum install git python3 python3-pip -y

# Clone your repo
cd /home/ec2-user
git clone https://github.com/umarfarouk16/Flask-Portfolio-AWS-ASG-ALB-HTTPS.git >> /home/ec2-user/install-logs.txt 2>&1

# Install dependencies
cd Flask-Portfolio-AWS-ASG-ALB-HTTPS
pip3 install flask >> /home/ec2-user/install-logs.txt 2>&1

# Make run script executable and run
chmod u+x run.sh
./run.sh >> /home/ec2-user/install-logs.txt 2>&1

echo "Setup complete" >> /home/ec2-user/install-logs.txt
