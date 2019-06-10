# -*- coding:utf-8 -*-
import json
import datetime
import time
from urllib import request

def goseek(start_date,end_date):
    # 参数分别代表需要查询的起始日期和终止日期
    start = start_date
    end = end_date
    datestart = datetime.datetime.strptime(start, '%Y-%m-%d')
    dateend = datetime.datetime.strptime(end, '%Y-%m-%d')
    server_url = 'http://api.goseek.cn/Tools/holiday?date='
    num = 0
    while datestart < dateend:
        num += 1
        datestart += datetime.timedelta(days=1)
        date = datestart.strftime('%Y%m%d')
        vop_response = request.urlopen(server_url + date)
        vop_data= json.loads(vop_response.read().decode('utf-8'))
        # 0代表工作日，1代表节假日，2代表调休补班，3代表休息日
        if vop_data['data'] == 0:
            print(date,vop_data['data'],'工作日')
        elif vop_data['data'] == 1:
            print(date,vop_data['data'],'节假日')
        elif vop_data['data'] == 2:
            print(date,vop_data['data'],'调休补班')
        elif vop_data['data'] == 3:
            print(date,vop_data['data'],'休息日')
        else:
            print('Error')
    print("process is over")
    print("run number is %s" % num)
if __name__ == '__main__':
    start_time = time.time()
    goseek('2019-06-01','2019-12-31')
    stop_time = time.time()
    print('run time is %s' % (stop_time - start_time))
