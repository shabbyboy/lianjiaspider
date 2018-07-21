# -*- coding: utf-8 -*-
import scrapy


class DoubanspiderSpider(scrapy.Spider):
    name = 'doubanSpider'
    allowed_domains = ['doubanSpider.com']
    #start_urls = ['http://doubanSpider.com/']

    def start_requests(self):
        url = 'https://movie.douban.com/subject/25823277/comments?start={}&limit=20&sort=new_score&status=P'
        for i in range(3201):
            realUrl = url.format(str(i*20))
            yield scrapy.Request(url=realUrl,callback=self.parse)

    def parse(self, response):
        pass
