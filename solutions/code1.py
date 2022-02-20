#!/usr/bin/env python
# coding: utf-8

# In[3]:



# CRUD - create,read,update,delete
# HTTP Methods - POST,GET,PUT,DELETE
# Representational State TRansfer (REST)


import os
import json
import requests
from requests import api,post,sessions
from urllib.parse import urlparse

f = open("first_json.json")
json_data = json.load(f)

# print(json_data)

myurl1 = str("http://127.0.0.1:5000/api/createOTP/[[obj.prop.bookingId]]")

a = urlparse(myurl1)
print(a.path)                    # Output: /kyle/09-09-201315-47-571378756077.jpg
print(os.path.basename(a.path))  # Output: 09-09-201315-47-571378756077.jpg

myurl2 = str("http://127.0.0.1:5000/api/[[obj.prop.bookingId]]/createOTP")
a2 = urlparse(myurl2)
print(a2.path)                    # Output: /kyle/09-09-201315-47-571378756077.jpg
print(os.path.basename(a2.path))  # Output: 09-09-201315-47-571378756077.jpg


keys = []
Values = []

for i in range(len(json_data['object']['assetPropertyList'])):
    v = json_data['object']['assetPropertyList'][i]['assetPropertyValue']
    k = json_data['object']['assetPropertyList'][i]['assetTypePropertyName']
    keys.append(k)
    Values.append(v)

#     print(keys)
#     print(Values)
#     print("------------------------")
    
#         dict["keys"] = Values    
kv_pairs = dict(zip(keys,Values))
# print(kv_pairs)

key_list = list(kv_pairs.keys())
# print("Lists of keys :",key_list)

# print("key for the requested value:",request_value)

for keys in key_list:
#     print(keys)
    if(request_value.find(keys) > 0):
        print("key provided :",keys)
        print("The value requested is: ",kv_pairs[keys])
        break
#     print(json_data['object']['assetPropertyList'])

#response  = sessions.post( )

# print(json_data)
# print(myurl)


# In[17]:


import requests

# post(url, data=None, json=None, **kwargs)[source]

LOGIN_URL = "http://139.59.90.214/connect-user/user/login"

payload = {
    'inUserName': 'websofttech',
    'inUserPass': 'password'
}

# Use 'with' to ensure the session context is closed after use.
with requests.Session() as s:
    p = s.post(LOGIN_URL, data=payload)
    print(type(p.content))
    # print the html returned or something more intelligent to see if it's a successful login page.
#     print(p.text)

    # An authorised request.
#     r = s.get('A protected web page url')
#     print(r.text)
        # etc...


# In[ ]:



# import requests module 
import requests 
  
# create a session object 
s = requests.Session() 
  
# set username and password 
s.auth = ('user', 'pass') 

print(s) 


# In[ ]:


#GET request

import requests

url = "http://139.59.90.214/connect-everything/assettype/getforuser"
headers = {projectId: '12345',
           apiKey: 'PUBLIC',
           Accept: 'application/json'}

r = requests.get(url=url,headers = headers)

import urllib.parse as urlparse
from urllib.parse import parse_qs
url = 'http://127.0.0.1:5000/api/createOTP/[[obj.prop.bookingId]]'
parsed = urlparse.urlparse(url)
print(parsed.path)

key = "obj.prop.bookingId"



# print(parse_qs(parsed.query)[''])


# In[10]:


import requests

url = 'http://139.59.90.214/connect-user/user/login'
myobj = {'bookingId': '99999',
        'accept' : 'application/json'
}
#use the 'auth' parameter to send requests with HTTP Basic Auth:
x = requests.post(url, data = myobj, header = headers, auth = ('websofttech', 'password'))

print(x.status_code)

