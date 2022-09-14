# Importing flask module in the project is mandatory
# An object of Flask class is our WSGI application.
from flask import (Flask, request,render_template)

# Flask constructor takes the name of
# current module (_name_) as argument.
app = Flask(__name__)

# The route() function of the Flask class is a decorator,
# which tells the application which URL should call
# the associated function.
@app.route('/', methods = ['GET','POST'])
# ‘/’ URL is bound with hello_world() function.
def hello_world():
        return 'Hello World'

@app.route('/poster',methods = ['POST','GET'])
def postmessage():
    if request.method=="POST":
        textInput = request.form["data"]
        print(textInput)
        return render_template("text.html",text=textInput)
#Doesnt work

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
