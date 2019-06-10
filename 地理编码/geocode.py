from urllib import parse
from urllib.request import urlopen
import hashlib
import json
import pandas as pd

def get_urt(addtress):
    #添加秘钥
    your_ak = '你的sk'
    queryStr = '/geocoder/v2/?address=%s&output=json&ak=your_ak' % addtress
    # 对queryStr进行转码，safe内的保留字符不转换
    encodedStr = parse.quote(queryStr, safe="/:=&?#+!$,;'@()*[]")
    #计算sn
    sn = (hashlib.md5(parse.quote_plus(rawStr).encode("utf8")).hexdigest())
    #由于URL里面含有中文，所以需要用parse.quote进行处理，然后返回最终可调用的url
    url = parse.quote("http://api.map.baidu.com"+queryStr+"&sn="+sn, safe="/:=&?#+!$,;'@()*[]")
    response = urlopen(url).read().decode('utf-8')
    # print(response)
    #将返回的数据转化成json格式
    responseJson = json.loads(response)
    #获取经纬度
    lon = responseJson.get('result')['location']['lng']
    lat = responseJson.get('result')['location']['lat']
    # status = responseJson.get('status')
    #获取误差范围
    confidence = responseJson.get('result')['confidence']
    #获取地区等级
    level = responseJson.get('result')['confidence']
    data = pd.DataFrame(data = [[addtress,lon,lat,confidence,level]],columns=['地名','经度','纬度','误差（米）','地区等级'])

    data.to_csv('goeinfo.csv',mode='a',index=False,header=False)
    return data
if __name__ == '__main__':
    #加载地区名，这里放在tuple里，也可以从csv等文件读取
    places = ('黄浦区','徐汇区','长宁区','静安区','普陀区','虹口区','杨浦区','宝山区','闵行区','嘉定区','浦东新区','松江区','金山区','青浦区','奉贤区','崇明区')
    with open('goeinfo.csv', 'a+',encoding='utf-8') as f:
        f.write("地名,经度,纬度,误差（米）,地区等级\n", )
        f.close()
    for i in places:
        get_urt(i)
    print('地区加载完成，已生成结果')
