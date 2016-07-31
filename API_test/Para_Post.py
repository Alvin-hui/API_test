# coding=utf-8
import requests
import json
# def Para_post(url, payload, flag):
#     payload = json.dumps(payload)
#     s = requests.Session()
#     r = s.get("http://service.youshang.com/api/simpleLogin.do?format=json&password=888888&logonName=kingdee_jinghui")
#     t = s.post(url, params=payload)
#     data = eval(t.text)
#     data = data["returnCode"]
#
#     if int(data) == flag:
#         return "This API is OK"
#     else:
#         return "This API is Wrong!"
def Para_post(url, payload, flag):
    s = requests.Session()
    r = s.get("http://service.youshang.com/api/simpleLogin.do?format=json&logonName=kingdeetesteshop&password=kd123456")
    r = s.post(url, params=payload)
    info = json.loads(r.text)
    Msg = info["returnMsg"]
    code = info["returnCode"]
    #print r.text
    if int(code) == flag:
        if int(code)== 1:
            return "This API is OK!"
        else:
            return "This API is OK" +';' + Msg
    else:
        if int(code) == 1:
            return "This API is Wrong!"
        else:
            return "This API is Wrong" + ';' + Msg
