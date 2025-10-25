#!/bin/bash
cd /home/ec2-user/PROJECT-GIT-TO-AWS
nohup python3 app.py > app.log 2>&1 &
