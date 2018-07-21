import scrapy
from lianjiaSpider.items import LianjiaspiderItem
import json
from lxml import etree


class firstSpider(scrapy.Spider):
    name = "lianjia"
    allowed_domains = ['nj.lianjia.com']
    regions = {
        'gulou': '鼓楼',
    }

    def start_requests(self):
        for region in list(self.regions.keys()):
            url = "https://nj.lianjia.com/chengjiao/"+region +"/"
            #meta 的作用是在回调函数之间传递值的作用
            yield  scrapy.Request(url,callback=self.parse,meta={'region':region})

    def parse(self, response):
        region = response.meta['region']
        selector = etree.HTML(response.text)
        sel = selector.xpath("//div[@class='page-box house-lst-page-box']/@page-data")[0]
        sel = json.loads(sel)
        total_page = sel.get("totalPage")

        for page in range(int(total_page)):
            if(page > 5):
                return
            url = "https://nj.lianjia.com/chengjiao/"+region +"/pg"+str(page+1)+"/"
            yield scrapy.Request(url,callback=self.parseAera,meta={'region':region})

    def parseAera(self,response):
        region = response.meta['region']
        selector = etree.HTML(response.text)
        cj_list = selector.xpath("//ul[@class='listContent']//li//a[@class='img']/@href")
        for list in cj_list:
            yield scrapy.Request(list,callback=self.parseContent,meta={'region':region,'link':list})
    def parseContent(self,response):
        lianjiaitem = LianjiaspiderItem()
        selector = etree.HTML(response.text)
        lianjiaitem['region'] = response.meta['region']
        lianjiaitem['href'] = response.meta['link']
        lianjiaitem['name'] = selector.xpath("//div[@class='house-title']//div[@class='wrapper']/text()")
        area = selector.xpath("//div[@class='m-right']//div[@class='name']//a/text()")[0]
        lianjiaitem['area'] = area
        listSub = selector.xpath("//div[@id='mapListContainer']//div[@class='itemInfo']/text()")
        s = set(listSub)
        s1 = ''
        for sub in s:
            s1 = s1+sub+"|"
        lianjiaitem['subway'] = s1
        yield lianjiaitem

