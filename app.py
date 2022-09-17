# Importing flask module in the project is mandatory
# An object of Flask class is our WSGI application.
from flask import (Flask, request,render_template)
import base64
# Flask constructor takes the name of
# current module (_name_) as argument.
app = Flask(__name__)

# The route() function of the Flask class is a decorator,
# which tells the application which URL should call
# the associated function.
@app.route('/')
# ‘/’ URL is bound with hello_world() function.
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
    data = request.data
    #decode = base64.b64decode(data)
    print(data)
    return 'hello'
#Doesnt work

'''

'''
def process_image():
    file = request.files['image']
    # Read the image via file.stream
    img = Image.open(file.stream)

    return jsonify({'msg': 'success', 'size': [img.width, img.height]})

#for multiple files
files = request.files.to_dict(flat=False) ## files is a list containing two images.
for i, file in enumerate(files):
    file.save(f'image-{i}.jpg')

def generateId():
    #ID generator logic, we can use some form of hashing
    return 'text'

def scaleUp(): #if request>x req per y milliseconds
    return 'text'

def scaleDown(): #if request<x req per y milliseconds
    return 'text' 
        
def addMessageIdAndSendtoSQS(file,messageId): #add message id with the files
    return 'text' 

def reieveOutputFromSQS():
    return 'text' 
    
def sendPutRequestToWG(output,messageId): 
    return 'text' 
'''
