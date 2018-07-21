import requests

try:
    #header
    kv = {'user-agent':'Mozilla/5.0'}
    #关键字
    kv = {'wd':'python'}
    path = "D://demo.jpg"
    url = "https://timgsa.baidu.com/timg?image&quality=80&size=b10000_10000&sec=1529895643&di=b3055fb78d18a69efb99c784140364e2&src=http://www.cbdio.com/image/attachement/jpg/site2/20170810/f04da2247c301af63d0815.jpg"
    #关键字参数
    re = requests.get(url)
    re.raise_for_status()
    # #通过header中的meta中获取
    #re.encoding = requests.utils.get_encodings_from_content(re.text)
    # 通过程序去分析，比较慢
    re.encoding = re.apparent_encoding
    with open(path,'wb') as f:
        #re.content 是二进制流
        f.write(re.content)
        f.close()
        print('爬取图片成功')
except:
    print(re.status_code)


