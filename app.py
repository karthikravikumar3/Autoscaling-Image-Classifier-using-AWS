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

'''def postmessage():
        uploaded_file = request.files['file']
        if uploaded_file.filename != '':
            uploaded_file.save(uploaded_file.filename)
        return redirect(url_for('hello_world'))
        '''
@app.route('/upload', methods=['POST','GET'])
def upload():
    if request.method == 'POST':
        #data = request.data
        #print(data)
        #return 'hi'
    #decode = base64.b64decode(data)
        file3 = request.files.getlist('myfile')
        for file2 in file3:
            filename = secure_filename(file2.filename)
            path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file2.save(path)
            with open("/home/ubuntu/savedImages/"+filename, "rb") as image2string:
                converted_string = base64.b64encode(image2string.read())
                print(converted_string)
                sqs.send_message(QueueUrl='https://sqs.us-east1.amazonaws.com/321247833586/RequestQueue',MessageBody=str(converted_string))
        #file2.save(path)

        #print(file3)
        '''
        if file1 not in request.files:
            print('No file part')
        file1 = request.files['file']
        if file1.filename == '':
            print('No selected file')
        '''

        return 'hi'
        #file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
 
        
        
