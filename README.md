# Autoscaling Image Classifier using AWS

## CSE 546: Cloud Computing Project 

Group members:
 - Deval Pandya - 1225424200
 - Karthik Ravi Kumar - 1225910467
 - Tirth Hihoriya - 1225413475 
 
AWS IAM user credentials:
Accound id: 477824770261

IAM user name: Faculty

Password: ccprojectfaculty#1

2.3 Member Tasks
Deval Pandya - (ASU ID: 1225424200)
	- I have designed the end to end flow of this project, like determining the AWS components to be used and setting them up like SQS Queues, S3 Buckets, Security Groups, EC2 instances and their user data, IAM Instance profiles. I also played a part in designing the logic for Web Tier, App Tier, and Controller. I implemented the code for the controller which is used for Autoscaling of App Tier instances as per the number of messages in the Request Queue. I did the testing for the whole application which involved sending several requests (Single/Concurrent) from the workload generators provided to us and optimized the algorithms of App Tier and Web Tier in order to showcase the features of autoscaling in our project. 

Karthik – (ASU ID: 1225910467).
 	 -I have designed the Web tier. The listener part of the web tier includes receiving messages from the user, storing it and encoding the images. Other parts include setting up and sending messages to the request queue,testing the request queue, receiving messages from the response queue and printing the output.

Tirth Hihoriya  -  (ASU ID: 1225413475 ). 
 - I have designed the App-Tier. The app-tier includes basic image classification program. It receives a task from the RequestQueue and processes it. Once it is done with processing, it sends the output to the Response Queue. It also stores the input in input-bucket and output in output-bucket. If no new task comes to it, it waits for 5 seconds. I have tested the app-tier code rigorously and updated it to have more robust code. 


