# coding=utf-8

import sys
import time
reload(sys)
sys.setdefaultencoding("utf-8")


def log_result(data):

    now = time.time()
    timeArray = time.localtime(int(now))
    otherStyleTime = time.strftime("%Y-%m-%d %H", timeArray)
    filename = otherStyleTime + '.txt'
    file = open(filename, 'a')
    file.write(str(data))
    file.write('\n')
    file.close()
