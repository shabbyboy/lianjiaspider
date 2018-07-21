# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import os
import re
from urllib import request
from scrapy.exceptions import DropItem
from scrapy.pipelines.images import ImagesPipeline
from BaiduSpiderStock import settings
class BaiduspiderstockPipeline(object):
    def process_item(self, item, spider):
        return item
class BaiduSpiderStock(object):
    def open_spider(self,spider):
        self.dir_path = '%s/%s'%(settings.IMAGES_STORE,spider.name)
        if not os.path.exists(self.dir_path):
            os.makedirs(self.dir_path)

    def close_spider(self,spider):
        pass
    def process_item(self,item,spider):
        for url in item['image_urls']:
            s = url[0]+url[1]+url[2]
            name = s.split('/')
            file_name = '%s/%s'%(self.dir_path,name[len(name)-1])
            if(os.path.exists(file_name)):
                continue
            urlname = s.split('"')
            with  open(file_name,'wb') as f:
                conn = request.urlopen('http://cdn.jandan.net'+urlname[len(urlname)-1])
                f.write(conn.read())
                f.close()
        return item
class ImagePipeline(ImagesPipeline):
    def get_media_requests(self, item, info):
        for url in item['image_urls']:
            url = "http:" + url
            yield scrapy.Request(url)
    def item_completed(self, results, item, info):
        image_paths = [x['path'] for ok,x in results if ok]
        if not image_paths:
            raise DropItem("no images")

        return item
