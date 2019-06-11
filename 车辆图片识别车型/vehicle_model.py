import requests
import base64
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

# 输入你的api_key和secret_key，获取地址https://console.bce.baidu.com/ai
api_key = '你的api_key'
secret_key = '你的secret_key'
url = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id=' + str(api_key) + '&client_secret=' + str(secret_key)
res = requests.get(url).text
a = eval(res)
access_token = a['access_token']
animal = 'https://aip.baidubce.com/rest/2.0/image-classify/v1/car?access_token=' + str(access_token)
header = {
    'Content-Type':'application/x-www-form-urlencoded'
}
data = {}
with open('图片地址.jpg', 'rb') as f:
    image = base64.b64encode(f.read())
    data["image"] = str(image, 'utf-8')
    res2 = requests.post(url=animal,data=data, headers=header).text
    print('颜色:',eval(res2)['color_result'])
    print('车型预测')
    for each in eval(res2)['result']:
        print(each['name'], '\t相似度：', each['score'])
    plt.imshow(mpimg.imread(f))
plt.show()
