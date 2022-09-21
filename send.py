import boto3
import base64
import os
import time
from flask import Flask, flash, request
from werkzeug.utils import secure_filename

UPLOAD_FOLDER = '/home/ubuntu/savedImages'
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

sqs=boto3.client('sqs')
s3=boto3.client('s3')
request_queue_url = 'https://sqs.us-east-1.amazonaws.com/477824770261/RequestQueue'
response_queue_url = 'https://sqs.us-east-1.amazonaws.com/477824770261/ResponseQueue'
input_bucket_name = 'ccinput'
output_bucket_name = 'ccoutput1'



while True:
    try:
        msg = sqs.receive_message(QueueUrl=response_queue_url)
        test = msg['Messages'][0]['Body']
        print(test.split(',')[0]+"-"+test.split(',')[1])
       #del_responce = sqs.delete_message(QueueUrl=response_queue_url , ReceiptHandle=msg['Messages'][0]['ReceiptHandle'])
    except:
        print("sleeping for 5 secs")
        time.sleep(5)

