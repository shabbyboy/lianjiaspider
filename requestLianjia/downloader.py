import requests
from redisCache import RedisCache
from throttle import Throttle
from random import choice
class Downloader:
    #错误重复尝试次数 numTry,延迟 delay 缓存 cache user_agent  proxies 代理
    def __init__(self,user_angent='wsap',proxies=None,delay=5,numTry=5,cache=None,timeout =30):
        self.user_agent=user_angent
        self.proxies = proxies
        self.delay =delay
        self.numTry=numTry
        self.cache = RedisCache()
        self.throt = Throttle(delay)
        self.timeOut =timeout

    #回调方法，可以让类和方法一样被使用
    def __call__(self,url):
        try:
            html = self.cache.__getitem__(url)
        except KeyError:
            html = None
        if html is None:
            self.throt.wait(url)
            header = {'user-agent':self.user_agent}
            #lamda表达式
            proixe = choice(self.proxies) if self.proxies else None
            html = self.download(url,header,proixe)
        self.cache.__setitem__(url,html)
        return html['html']

    #处理url下载问题
    def download(self,url,header,proxie):
        try:
            resp = requests.get(url,headers=header,proxies=proxie,timeout=self.timeOut)
            html = resp.text
            #小于400表示成功了
            if resp.status_code >=400:
                html = None
                #500到600需要重试 400到500是可以直接退出的错误
                if 600> resp.status_code >500 and self.numTry:
                    self.numTry -= 1
                    #递归 实现错误重试
                    return self.download(url,header,proxie)
        except requests.exceptions.RequestException as e:

            return {'html':None,'code':500}
        return {'html':html,'code':resp.status_code}