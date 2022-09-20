#!/bin/bash
sudo apt update
sudo apt install python3
sudo apt install python3-flask -y
sudo apt install python3-boto3 -y
sudo apt install tmux -y
mkdir /home/ubuntu/savedImages
sudo apt install awscli


aws configure set region us-east-1
aws configure set aws_access_key_id AKIAUVS645XZFMMFJ27R
aws configure set aws_secret_access_key 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
