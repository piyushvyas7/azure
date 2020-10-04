import requests

BASE = "http://localhost:5000"
data = [
    # nothing mention in requirement to have ignoreCase
    {"replace" : "should not convert google GooGle gooGle"},
    #requirement values as per requirement
    {"replace" : "conversation for all values Oracle Google Microsoft Amazon Deloitte is possible"},
    {"replace" : "Oracle Google"},
    #empty string should have empty response
    {"replace" : ''},
    #other cases
    {"replace" : "test"}
]

for i in range(len(data)):
    response = requests.post(BASE + "/api/replace" , data[i])
    print(response.content)

#response = requests.post(BASE + "/api" , )
#response = requests.post(BASE + "/api" , {'replace' : "test"})
#print(response.json())