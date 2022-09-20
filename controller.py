import boto3
import time

sqs = boto3.client('sqs')
ec2 = boto3.client('ec2')

ami_id = 'ami-02393d34fa28c1110'
min_count = int(3)
max_count = int(6)
current_count = 1
instance_type = 't2.micro'
key_name = 'KP1'
security_group_id = 'sg-00f6f33eff0859497'
iam_instance_profile = 'arn:aws:iam::321247833586:instance-profile/EC2-SQS-S3-FullAccess'
instance_name = 'app_instance'
userdata = '#cloud-boothook \n#!/bin/bash \ncd /home/ubuntu \nflask run --host=0.0.0.0 --port=8080 > log2.txt 2>&1 & \n'
instance_list = []

instances = ec2.describe_instances( Filters = [{ 'Name': 'instance-state-code', 'Values': [ '0', '16' ] }, { 'Name': 'image-id', 'Values': ['ami-0ce0fa0847b8281dc'] }] )

print(instances)

current_count = int(len(instances['Reservations']))
print('Current Count: ' , current_count)

#Populating Instance Ids for App Tier Servers already running
for x in instances['Reservations']:
    instance_list.append(x['Instances'][0]['InstanceId'])

print('Instance List: \n', instance_list)

queue_url = 'https://sqs.us-east-1.amazonaws.com/321247833586/RequestQueue'

while True:
    try:
        print('Polling the Request Queue...')
        queue_attr = sqs.get_queue_attributes(QueueUrl = queue_url, AttributeNames = ['All'])
        num_visible_msg = int(queue_attr['Attributes']['ApproximateNumberOfMessages'])
        num_invisible_msg = int(queue_attr['Attributes']['ApproximateNumberOfMessagesNotVisible'])
        total_msg = int(num_visible_msg + num_invisible_msg)
        
        print('Total Messages in Queue: ', total_msg)
        print('Total EC2 Instance Running: ', current_count)
        
        #Scale Out App Tier Instances
        if total_msg > current_count and current_count < max_count:
            print('Scaling Out...')
            instances = ec2.run_instances(ImageId=ami_id, MinCount=1, MaxCount=1, InstanceType=instance_type, KeyName=key_name, SecurityGroupIds=[security_group_id,], IamInstanceProfile={'Arn' : iam_instance_profile}, TagSpecifications=[{'ResourceType': 'instance', 'Tags' : [{'Key': 'Name', 'Value': 'app-instance'+str(current_count)},]},], UserData=userdata)
            instance_list.append(instances['Instances'][0]['InstanceId'])
            current_count += 1
            
        #Scale In App Tier Instances
        elif total_msg < current_count and current_count > min_count:
            print('Scaling In...')
            ec2.terminate_instances(InstanceIds = [instance_list.pop()])
            current_count -= 1
        
        else:
            print('No Scaling Needed...')
        time.sleep(10) #10 Seconds
    except Exception as e:
        print(e)
        break
    

