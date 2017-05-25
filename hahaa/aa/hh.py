import requests
import json
import base64
import hashlib

def encode(s):
    return base64.b64encode(s).replace("\n", "").replace("M", "$").replace("D", "!").replace("2", "*").replace("=", "<")
def post(data):
    headers = {'Content-Type': 'application/json'}
    rr=requests.post('http://60.205.228.129:8080/small/user/login', data=json.dumps(data),headers=headers)
    print (data)
    print (rr.text)
def md5(s):
    m = hashlib.md5()
    m.update(s)
    return m.hexdigest()

data = [
    ["15116930341","c33367701511b4f6020ec61ded352059"],
    ["15210068901","12345678"],
    ["15210068901","c33367701511b4f6020ec61ded352059"],
    ]

for d in data:
    m = encode(d[0])
    p= md5(d[1])
    payload = {"loginType":"0","mobile":m,"passwd":p}
    post(payload)