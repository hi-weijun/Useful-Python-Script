'''
auther:zhu weijun
content:计算两坐标之间的空间距离
'''

# 方法一，使用geopy库
from geopy.distance import geodesic

def corrtodistance(lat_1,lon_1,lat_2,lon_2):
    # lat:纬度值，lon:经度值
    coor1 = (lat_1,lon_1)
    coor2 = (lat_2,lon_2)
    distance = geodesic(coor1,coor2).km
    return distance

''' 
示例：
上海虹桥火车站(31.204927,121.343656)
南京南站(31.975614,118.805403)
百度地图拾取：两地距离255.7km

d = corrtodistance(31.204927,121.343656,31.975614,118.805403)
print(d)

输出：255.606
'''
