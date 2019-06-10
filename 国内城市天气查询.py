# -*- coding:utf-8 -*-
import json
import time
from urllib import request
from urllib.parse import quote
import pandas as pd

def goseek(placeName):
    text = quote(placeName, 'utf-8')
    server_url = 'https://www.apiopen.top/weatherApi?city=' + text
    vop_response = request.urlopen(server_url)
    x = json.loads(vop_response.read().decode('utf-8'))['data']
    print('城市:', x['city'])
    print('温度:', x['wendu'],'℃')
    print('提醒:', x['ganmao'])
    n = 0
    for i in x['forecast']:
        if n == 0:
            # i.keys() = ['日期','高温','风力','低温','风向','类型']
            df = pd.DataFrame(i, index=['指标'])
            df_all = df
        else:
            df = pd.DataFrame(i, index=['指标'])
            df_all = df_all.append(df)
        n += 1
    df_all.reset_index(inplace=True, drop=True)
    df_all.columns = ['日期', '高温', '风力', '低温', '风向', '类型']
    df_all = df_all[['日期', '高温', '低温', '类型', '风力', '风向']]
    df_all['高温'] = df_all['高温'].apply(lambda x: x[2:])
    df_all['低温'] = df_all['低温'].apply(lambda x: x[2:])
    df_all['风力'] = df_all['风力'].apply(lambda x: x[-5:-3])
    print('--------------------------以下详细天气--------------------------------')
    print(df_all)

if __name__ == '__main__':
    start_time = time.time()
    goseek('上海')
    stop_time = time.time()
    print('run time is %s' % (stop_time - start_time))
