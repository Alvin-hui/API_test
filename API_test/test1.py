# coding=utf-8

import json
import requests
#payload = {"format":"json","password":"kd123456","logonName":"kingdeetesteshop"}

s = requests.Session()
r = s.post("http://service.youshang.com/api/simpleLogin.do?format=json&logonName=kingdeetesteshop&password=kd123456")

url = u'http://service.youshang.com/api/loginApi.do?format=json&action=queryData&siId=79409641912&businessType=allcustomerEx'

payload = {"paras":
                   [
                       {
                           "lasttag": "",
                           "lastIds": "",
                           "start": "0",
                           "length": "100"
                       }
                   ]
           }

r = s.post(url, params=json.dumps(payload))

print r.status_code
print r.text
print type(json.dumps(r.text))

