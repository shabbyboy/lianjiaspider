import requests
from bs4 import BeautifulSoup
import bs4
import re

def getHtmlText(url):
    try:
        rsp = requests.get(url)
        rsp.encoding = rsp.apparent_encoding
        rsp.raise_for_status()
        return rsp.text
    except:
        print('爬取数据失败')

def fillDataToInner(ulist,text):
    bsoup = BeautifulSoup(text,'html.parser')
    list = re.findall(r'<td>[0-9]+<td>',text)
    i = 0
    for tr in bsoup.find("tbody",attrs={"class":"hidden_zhpm"}).children:
        if isinstance(tr,bs4.element.Tag):
            td = tr('td')
            ulist.append([list[i][4:-4],td[1].string,td[3].string])
            i = i+1

def printText(ulist):
    tplt = "{0:^10}{1:{3}^10}{2:^20}"
    print(tplt.format("排名","学校名称","分数",chr(12288)))
    for li in ulist:
        print(tplt.format(li[0], li[1], li[2],chr(12288)))

def main():
    url = "http://www.zuihaodaxue.cn/zuihaodaxuepaiming2017.html"
    html = getHtmlText(url)
    ulist = []
    fillDataToInner(ulist,html)
    printText(ulist)

main()


