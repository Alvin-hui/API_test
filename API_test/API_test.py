# -*- coding: utf-8 -*-
from openpyxl import Workbook
from openpyxl import load_workbook
from Para_Login import Para_login
from Para_Get import Para_get
from Para_Post import Para_post
from Save_Data import log_result
from Read_data import read_data
import json
import time

start = time.clock()

filename = r'API_testcase.xlsx'
sheetNum = 2   #测试文件API_testcase.xlxs中sheet数量
num = 0        #用例条数，初始值为0
for n in range(0,sheetNum,1):
    data = read_data(filename,n)
    rows = data[0]
    num += int(json.dumps(rows -1))   #对各个sheet中的测试用例数求和，值赋给num
    columns = data[1]
    data = data[2]

    for i in range(0, rows - 1, 1):
        case_name = data[i][0]
        url = data[i][1]
        method = data[i][2]
        payload = data[i][3]
        print type(payload)
        flag = data[i][4]

        #if payload == "None":
            #log_result('params payload is None')
        #else:


        payload = json.loads(payload)
        if n == 0:
            if method == "GET":
                test_code = Para_login(url, payload, flag)
                log_result(case_name + ':' + test_code)
                print case_name + ':' + test_code
            if method == "POST":
                test_code = Para_post(url, payload, flag)
                log_result(case_name + ':' + test_code)
                print case_name + ':' + test_code
        else:
            if method == "GET":
                test_code = Para_get(url, payload, flag)
                log_result(case_name + ':' + test_code)
                print case_name + ':' + test_code
            if method == "POST":
                test_code = Para_post(url, payload, flag)
                log_result(case_name + ':' + test_code)
                print case_name + ':' + test_code
end = time.clock()


#print u'本次一共执行了:' + str(num) + u'条用例'
print u'一共运行了: %f s ' %(end-start )
