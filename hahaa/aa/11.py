import requests
import json
import base64

def encodeUid(uid):
    return base64.b64encode(uid).replace("M", "$").replace("D", "!").replace("2", "*")

print encodeUid('50131')
headers = {'Content-Type': 'application/json','ukey':encodeUid('50131')}
data={}
rr=requests.post('http://60.205.228.129:8080/small/question/problemList/0',data=json.dumps(data),headers=headers)
print (rr.text)
print (rr.json()['code'])
