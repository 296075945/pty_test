import requests
import json

# url = "http://localhost:8080/cc/"
headers  ={'Content-Type': 'application/json'}
# print requests.post(url+"head",headers ={'name':'weiyang00'}).text
# 
# print requests.post(url+"body",data=json.dumps({'123':"123"}),
#                     headers =headers).text
#                     
# print requests.post(url+"body",data=json.dumps([{'name':'hhd'},{'name':'wy'}]),
#                     headers =headers).text
#                     
# print requests.post(url+"body",
#                     headers =headers).text
#                     
# print requests.post(url+"cookie",
#                     cookies={"JSESSIONID":'12312',"userName":"nidaye"}).text 

print requests.post("http://localhost:8090/login",data=json.dumps({'userName':'hhd','password':'wy'}),
                    headers =headers,timeout=100).text                                