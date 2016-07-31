# -*- coding: utf-8 -*-

import requests
import json
import re


def Para_get(url, payload, flag):
    s = requests.Session()
    r = s.get("http://service.youshang.com/api/simpleLogin.do?format=json&logonName=kingdeetesteshop&password=kd123456")
    r = s.get(url, params=payload)
    info = json.loads(r.text)
    print info
    Msg = info["returnMsg"]
    code = info["returnCode"]
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
