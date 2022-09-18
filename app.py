import torch
import torchvision
import torchvision.transforms as transforms
import torch.nn as nn
import torch.nn.functional as F
import torchvision.models as models
from urllib.request import urlopen
from PIL import Image
import numpy as np
import json
import sys
import time
import boto3
import base64

model = models.resnet18(pretrained=True)
model.eval()

sqs = boto3.client('sqs')
s3 = boto3.client('s3')
request_queue_url = 'https://sqs.us-east-1.amazonaws.com/321247833586/RequestQueue'
response_queue_url = 'https://sqs.us-east-1.amazonaws.com/321247833586/ResponseQueue'
input_bucket_name = 'ccinput'
out_bucket_name = 'ccoutput1'


def upload_file(file_name, bucket):
    try:
        response = s3.upload_file(file_name, bucket)
    except:
        return False
    return True

while True:
    msg = sqs.receive_message(QueueUrl=request_queue_url)
    bytes = str.encode(msg['Messages'][0]['Body'])

    img_name = 'abcd.JPEG'  #need to update as per changes in web tier


    file = open('abc.JPEG', 'wb')
    file.write(base64.b64decode((bytes)))
    file.close()
    img = Image.open('abc.JPEG')


    img_tensor = transforms.ToTensor()(img).unsqueeze_(0)
    outputs = model(img_tensor)
    _, predicted = torch.max(outputs.data, 1)

    with open('./classifier/imagenet-labels.json') as f:
        labels = json.load(f)
    result = labels[np.array(predicted)[0]]

    save_name = f"{img_name},{result}"
    
    upload_file(img_name, input_bucket_name)

    msg_response = 0
    while msg_response!=200:
        msg_response  = sqs.send_message(QueueUrl=response_queue_url, MessageBody=save_name)


    
   

    del_responce = 0
    while del_responce!=200:
        del_responce = sqs.delete_message(QueueUrl=request_queue_url , ReceiptHandle=['Messages'][0]['ReceiptHandle'])
    
        

    print(f"{save_name}")

    time.sleep(5)


