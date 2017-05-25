#encode = utf-8
import requests


req = requests.get("https://www.baidu.com",encoding='utf-8')
print req.text