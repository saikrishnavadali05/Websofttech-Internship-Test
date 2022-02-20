import os
import json
import requests
from requests import api,post,sessions
from urllib.parse import urlparse

f = open("first_json.json")
json_data = json.load(f)

print(json_data["apiJson"])
temp = "'"+str(json_data["apiJson"])+"'"

for i in json_data["object"]["assetPropertyList"] :
    temp = temp.replace('[[obj.prop.'+i["assetTypePropertyName"]+']]',str(i["assetPropertyValue"]))
    temp = temp.replace('[[obj.assetName]]',json_data["object"]["assetName"])
    temp = temp.replace('"[[obj.asitis]]"', str(json.dumps(json_data["object"])))
    temp = temp.replace('[[obj.assetId]]', str(json_data["object"]["assetId"]))
print(temp)
raw_data = str(temp)

