import requests
from downloader import Downloader
from lxml.html import fromstring,tostring
import json


#启动函数
def scrapyItem(agent,proxies,max_depth =4):
    region = ['gulou','jianye']
    startUrl = 'https://nj.lianjia.com/chengjiao/'
    D = Downloader(user_angent=agent,proxies=proxies)
    for reg in region:
        seen = set()
        urls_quene = [startUrl+reg+'/']
        while urls_quene:
            url = urls_quene.pop()
            html = D(url)
            if html:
                totalpages = scrapy_page(html)
                if totalpages:
                    for page in range(2,totalpages):
                        urlpage = startUrl+reg+'/'+"pg"+str(page)+"/"
                        if urlpage not in seen:
                            seen.add(urlpage)
                            urls_quene.append(urlpage)
                            htmlpage = D(urlpage)
                            links = scrapy_callback(htmlpage)
                            for linkurl in links:
                                if linkurl not in seen:
                                    seen.add(linkurl)
                                    urls_quene.append(linkurl)
                else:
                    print(url)
                    links = scrapy_callback(html)
                    for linkurl in links:
                        if linkurl not in seen:
                            seen.add(linkurl)
                            urls_quene.append(linkurl)
            else:
                continue

#获取新的成交房源url并且存储数据
def scrapy_callback(html):
    tree = fromstring(html)
    links = []
    title = tree.xpath('//div[@class="house-title LOGVIEWDATA LOGVIEW"]/div/text()')
    price = tree.xpath('//span[@class="dealTotalPrice"]/i/text()')

    #插入数据库房子的信息
    try:
        print(title)
        with open('lianjia.txt','a') as f:
            f.writelines(title + price)
    finally:
        if f:
            f.close()

    link = tree.xpath('//a[@class="img"]/@href')
    link2= tree.xpath('//div[@class="fl pic"]/a/@href')
    if link:
        for li in link:
            links.append(li)
    if link2:
        for li2 in link2:
            links.append(li2)
    return links
#构建爬取队列

def scrapy_page(html):
    tree = fromstring(html)
    pagejson = tree.xpath('//div[@class="page-box house-lst-page-box"]/@page-data')
    totalpage=0
    if pagejson:
        pagejson = json.loads(pagejson[0])
        totalpage = pagejson["totalPage"]
    return totalpage

if __name__ == '__main__':
    scrapyItem("Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:31.0) Gecko/20100101 Firefox/31.0",None)