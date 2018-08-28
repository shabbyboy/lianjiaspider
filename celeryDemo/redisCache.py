import json
import zlib
from redis import StrictRedis
from datetime import timedelta

class RedisCache:
    #是否压缩文件 compress endcoding 编码方式，key:url value:html redis链接：client 设置缓存过期时间expires=timedelta(days=30)
    def __init__(self,client=None,compress=True,endcoding='utf-8',expires=timedelta(days=30)):
        self.client = StrictRedis(host='localhost',port=6379,db=0)
        self.compress = True
        self.endcoding =endcoding
        self.expires = expires
    #序列化 解压 解码 序列化
    def __getitem__(self,url):
        value = self.client.get(url)
        if value:
            if self.compress:
                value = zlib.decompress(value)
            return json.loads(value.decode(self.endcoding))
        else:
            raise KeyError(url+'does exit')
    #反序列化 解码 解压
    def __setitem__(self,url,html):
        data = bytes(json.dumps(html),encoding=self.endcoding)
        if self.compress:
            data = zlib.compress(data)
            #设置过期时间 setex
        self.client.setex(url,self.expires,data)
