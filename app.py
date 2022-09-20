import boto3
import base64
import os
from flask import Flask, flash, request
from werkzeug.utils import secure_filename

UPLOAD_FOLDER = '/home/ubuntu/savedImages'
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
sqs=boto3.client('sqs')

@app.route('/')
def hello_world():
        return 'Hello World'

@app.route('/upload', methods=['POST','GET'])
def upload():
    if request.method == 'POST':
        file3 = request.files.getlist('myfile')
        for file2 in file3:
            filename = secure_filename(file2.filename)
            path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file2.save(path)
            with open("/home/ubuntu/savedImages/"+filename, "rb") as image2string:
                bytes = base64.b64encode(image2string.read())
                sqs.send_message(QueueUrl='https://sqs.us-east2.amazonaws.com/321247833586/RequestQueue',
                        MessageAttributes={
        'ImageName': {
            'DataType': 'String',
            'StringValue': filename
        }},MessageBody=bytes.decode('ascii'))
                print('filename')
        return 'hi'

