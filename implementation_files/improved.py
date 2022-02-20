


import os
import json
import requests
from requests import api,post,sessions
from urllib.parse import urlparse

f = open("first_json.json")
json_data = json.load(f)

# print(json_data)
key = "[[obj.prop.bookingId]]"

myurl1 = "http://127.0.0.1:5000/[[obj.prop.bookingId]]/api/createOTP/"
print(myurl1)

index = myurl1.find(key)

request_value = myurl1[index:index+len(key)]
print("request value :",request_value)

print("starting index of the key :",index)
a = urlparse(myurl1)
# print(a.path)                    


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
