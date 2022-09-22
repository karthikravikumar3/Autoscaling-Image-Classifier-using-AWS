import boto3
import time
import base64
import os
import random
from flask import Flask, flash, request
from werkzeug.utils import secure_filename

UPLOAD_FOLDER = '/home/ubuntu/savedImages'
application = Flask(__name__)
application.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
sqs=boto3.client('sqs')

request_queue_url = 'https://sqs.us-east-1.amazonaws.com/477824770261/RequestQueue'
response_queue_url = 'https://sqs.us-east-1.amazonaws.com/477824770261/ResponseQueue'

@application.route('/')
def hello_world():
        return 'Hello World'

@application.route('/upload', methods=['POST','GET'])
def upload():
    if request.method == 'POST':
        file3 = request.files.getlist('myfile')
        for file2 in file3:
            filename = secure_filename(file2.filename)
            path = os.path.join(application.config['UPLOAD_FOLDER'], filename)
            file2.save(path)
            with open("/home/ubuntu/savedImages/"+filename, "rb") as image2string:
                bytes = base64.b64encode(image2string.read())
                sqs.send_message(QueueUrl=request_queue_url,
                        MessageAttributes={
        'ImageName': {
            'DataType': 'String',
            'StringValue': filename
        }},MessageBody=bytes.decode('ascii'))
                print(filename)
        
        while True:
            try:
                print('Checking for response...')
                queue_attr = sqs.get_queue_attributes(QueueUrl = response_queue_url, AttributeNames = ['All'])
                num_visible_msg = int(queue_attr['Attributes']['ApproximateNumberOfMessages'])
                print('Visible msg: ', num_visible_msg)
                if num_visible_msg > 0:
                    msg = sqs.receive_message(QueueUrl=response_queue_url, AttributeNames=['All'], MessageAttributeNames=['All'])
                    body = msg['Messages'][0]['Body']
                    resp_filename, result = body.split(',')
                    if filename == resp_filename:
                        print("File Name: ", filename)
                        print("Classification Result: ", result)
                        
                        sqs.delete_message(QueueUrl=response_queue_url, ReceiptHandle=msg['Messages'][0]['ReceiptHandle'])
                        return result
                else:
                    time.sleep(random.random()*3+1)
                    continue
                    
            except Exception as e:
                print("Exception Occured...")
                print(e)
            
            time.sleep(random.random()*3+1)
        #return 'hi'
        
if __name__ == "__main__":
        application.run(host='0.0.0.0', port='8080')