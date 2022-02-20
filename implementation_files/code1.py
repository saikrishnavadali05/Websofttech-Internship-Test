#!/usr/bin/env python
# coding: utf-8

# In[63]:



# CRUD - create,read,update,delete
# HTTP Methods - POST,GET,PUT,DELETE
# Representational State TRansfer (REST)



import json
import requests
from requests import api,post,sessions

f = open("first_json.json")
json_data = json.load(f)

myurl = str("http://127.0.0.1:5000/api/createOTP/")

request_value = str("[[obj.prop.bookingId]]")

# search_key = 

# print(json_data.keys())

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


# In[3]:




