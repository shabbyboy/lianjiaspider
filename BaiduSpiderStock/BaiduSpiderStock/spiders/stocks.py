# -*- coding: utf-8 -*-
import scrapy
from bs4 import BeautifulSoup
from ..items import BaiduspiderstockItem
import re
class StocksSpider(scrapy.Spider):
    name = 'stocks'
    #allowed_domains = ['baidu.com']
    start_urls = ['http://jandan.net/ooxx']

    def parse(self,response):
        url = response.css('link[rel=stylesheet]::attr(href)').extract()
        for rl in url:
            yield scrapy.Request('http:' +rl,callback=self.parseStock)

    def parseStock(self,response):
        item = BaiduspiderstockItem()
        item['image_urls'] = re.findall('(background:url)(\(.+?)(.gif|.jpg|.png)',response.text)
        yield item
'''
    def parse(self, response):
        item = BaiduspiderstockItem()
        item['image_urls'] = response.xpath('//img//@src').extract()
        yield item
'''
'''
    def parseStock(self,response):
        infoDict ={}
        stockinfo = response.css('.stock-bots')
        name = stockinfo.css('.bets-name').extract()[0]
        keylist = stockinfo.css('dt').extract()
        valulelist = stockinfo.css('dd').extract()
        for i in range(len(keylist)):
            key = re.findall(r'>.*</dt>',keylist[i])[0][1:-5]
            try:
                val = re.findall(r'\d+\.?.*</dd>',valulelist[i])[0][0:-5]
            except:
                val='---'
            infoDict[key] = val
        infoDict.update({'股票名称':re.findall('\s.*\(',name)[0].split()[0]+\
                                re.findall('\>.*\<',name)[0][1:-1]})
        yield infoDict
'''