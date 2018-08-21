from lxml.html import fromstring,tostring

import requests
"""
用来测试lxml和beautifulsoup表达式的
"""
def downxml():
    xml = '<div class="house-title" data-lj_view_evtid="11228" data-lj_action_resblock_id="103102672365" data-lj_action_housedel_id="1411000000686"><div class="wrapper">王府园小区 2室1厅 46.49平米<span>2018.08.02 链家成交</span><h1 class="index_h1">王府园小区 2室1厅 46.49平米</h1></div></div>'
    resp = requests.get("https://nj.lianjia.com/chengjiao/103100472329.html",proxies ={"http":"http://115.32.41.100:80"})
    html = resp.text
    tree = fromstring(html)
    print(html)
    links = []
    title = tree.xpath('//div[@class="wrapper"]/text()')
    price = tree.xpath('//span[@class="dealTotalPrice"]/i/text()')

# 插入数据库房子的信息
    try:
        print(title)
        with open('lianjia.txt', 'a') as f:
            f.writelines(title+price)
    finally:
        if f:
            f.close()

    link = tree.xpath('//a[@class="img"]/@href')
    link2 = tree.xpath('//div[@class="fl pic"]/a/@href')
    if link:
        for li in link:
            links.append(li)
    if link2:
        for li2 in link2:
            links.append(li2)
if __name__ == '__main__':
    downxml()