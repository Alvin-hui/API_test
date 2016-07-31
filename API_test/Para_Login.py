# -*- coding: utf-8 -*-

import requests
import json
import re
pattern = re.compile(r'stutas":200')
def Para_login(url, payload, flag):

    r = requests.get(url, params=payload)
    info = json.loads(r.text)
    Msg = info["returnMsg"]
    code = info["returnCode"]
    match = pattern.match(str(info))
    if match:
        if int(code) == flag:
            if int(code) == 1:
                return "This API is OK!"
            else:
                return "This API is OK" + ';' + Msg
        else:
            if int(code) == 1:
                return "This API is Wrong!"
            else:
                return "This API is Wrong" + ';' + Msg
