# -*- coding:utf-8 -*-
import json
import pandas as pd
from urllib import request
import re
from urllib.parse import quote

def goseek(lat,lon):
    # 输入你的秘钥，获取地址http://lbsyun.baidu.com/apiconsole/key/create
    your_ak = '你的ak'
    url = 'http://api.map.baidu.com/geocoder/v2/?callback=renderReverse&extensions_town=true&location={},{}&output=json&pois=1&latest_admin=1&ak={}'.format(lat,lon,your_ak)
    rp = request.urlopen(url).read().decode('utf-8')
    rp = re.findall(r"\((.*)\)",rp)[0]
    rpjson= json.loads(rp)
    # 经纬度
    lon = rpjson['result']['location']['lng']
    lat = rpjson['result']['location']['lat']
    # 国家
    country = rpjson['result']['addressComponent']['country']
    # 省份
    province = rpjson['result']['addressComponent']['province']
    # 城市
    city = rpjson['result']['addressComponent']['city']
    # 区县
    district = rpjson['result']['addressComponent']['district']
    # 乡镇
    town = rpjson['result']['addressComponent']['town']
    # 描述
    desc = rpjson['result']['sematic_description']
    # pois
    pois = rpjson['result']['pois']

    print('经纬度：',lon,lat)
    print('国家：',country)
    print('省：',province)
    print('市：',city)
    print('区县：',district)
    print('乡镇：',town)
    print('描述：',desc)
    num = 1
    pois_file = []
    for poi in pois:
        print('pois')
        print(num,poi['name'],poi['tag'])
        pois_file.append(poi['name'])
        num+=1
    print('---------------------------------')
    data = pd.DataFrame([[lon, lat, country, province, city, district, town, desc, pois_file]], columns=range(9))
    data.to_csv('goeinfo.csv', mode='a', index=False, header=False)


if __name__ == '__main__':
    with open('goeinfo.csv', 'a+',encoding='utf-8') as f:
        f.write("经度,纬度,国家,省份,城市,区县,乡镇,描述,pois\n")
    coors = ((31.22874037307247,121.47298325512693),(31.22206126567911,121.5394162080078),(31.161340496865517,121.43847931835936))
    for i in coors:
        goseek(i[0],i[1])
