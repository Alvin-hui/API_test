# coding=utf-8

import json
import requests
#payload = {"format":"json","password":"kd123456","logonName":"kingdeetesteshop"}

s = requests.Session()
r = s.get("http://service.youshang.com/api/simpleLogin.do?format=json&logonName=kingdeetesteshop&password=kd123456")
#print r.text
url = u'http://service.youshang.com/api/loginApi.do?format=json&action=queryData&siId=79409641912&businessType=commit_unit'
payload = {"paras":
    [
        {
            "data":
                [
                    {
                    "tempid":"134324",
                    "name":"元",
                    "onlineId":"",
                    "state":"0"
                    },
                    {
                        "tempid":"134325",
                        "name":"公斤",
                        "onlineId":"123124",
                        "state":"1"},
                ],
            "data2":
                [
                    {
                        "tempid":"132646545",
                        "unitTypeName":"第一组",
                        "onlineId":"123145",
                        "state":"1",
                        "units":
                            [
                                {
                                    "tempid":"12343424",
                                    "onlineId":"12314",
                                    "state":"1",
                                    "unitname":"个",
                                    "rate":"1.5",
                                    "isDefault":"false",
                                    "isDelete":"false"
                                },
                                {
                                    "tempid":"12343425",
                                    "onlineId":"",
                                    "state":"0",
                                    "unitname":"元",
                                    "rate":"1.5",
                                    "isDefault":"false",
                                    "isDelete":"false"
                                }
                            ]
                    }

                    ]
        },
    ]
}


#     "format":"json",
#     "siId":"79409641912",
#     "action":"queryData",
#     "businessType":"all_saleorder",
#     "paraData":{"paras":{"lasttag":"","lastIds":"","start":"0","length":"100"}}}



headers = {"user-agent": "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:47.0) Gecko/20100101 Firefox/47.0"}
data = s.get(url, params=json.dumps(payload), headers=headers)
import re
pattern = re.compile(r'returnCode"')
math = pattern.match('returnCode":"0","returnMsg":"error:params is illegal","data":"","callback":"","action":"queryData"')

if math:
    print "the test is OK"
    print math.group()
else:
    print "the test is wrong"
print data.text
