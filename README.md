--- 
Assignment:
Build an API that will use a string as input and does a find and replace for certain words and outputs the result. For example: replace GoogleforGoogle©. 
Example input: 	  “We really like the new security features of Google Cloud”. 
Expected output:  “We really like the new security features of Google© Cloud”.
The words that need to be replaced are provided below the description of this assignment.

--- 
Rules:
You may deploy this solution on any cloud (e.g. AWS, GCP, Heroku) and use any technology you want. You can build it for example in Golang, and deploy it on AWS EKS or build it in .NET and deploy it as a webapp on Microsoft. Bonus points if you’re able to surprise us.
It’s important that you are be able to explain the choices made during this assignment. Rather try to build something that doesn’t work and we have a good discussion on what you have learned then copying something of Google and not being able to explain the innerworking or the choices made.

---
List of word that need to be replaced:
- Oracle -> Oracle©
- Google -> Google©
- Microsoft -> Microsoft©
- Amazon -> Amazon©
- Deloitte -> Deloitte©

---
description: 
- "This is an endpoint which facilates the conversion of below mapping tables
A minimal sample app that can be used to demonstrate deploying Flask apps to Azure App Service on Linux."

---
languages:
- python

---
products:
- azure
- azure-app-service
- deployment center


---
# How to setup application:
- 
For local:
-
Run the below mention command after taking the checkout of the code
- python3 -m venv antenv [if you get an error you need sudo apt-get install python3-venv]
- source antenv/bin/activate	[if you get an error you need sudo apt install python-pip]
- sudo api install python-pip
- pip install -r requirements.txt [if you get an error you need sudo apt install python3-flask]

	note: if you face a problem you might need to run sudo apt-get update if you have older dependency
	
	once done execute the command 'flask run' [Local]
	http://localhost:5000

- 
For cloud:
-
- connect the git hub with the WebApp already in cloud(Azure for this project) 
- https://assignmentwebapp.azurewebsites.net


# Python Flask sample for Azure App Service (Linux)
For instructions on running and deploying the code, see [Quickstart: Create a Python app in Azure App Service on Linux](https://docs.microsoft.com/azure/app-service/quickstart-python)