# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql
from lianjiaSpider.items import LianjiaspiderItem

class LianjiaspiderPipeline(object):

    def __init__(self,mysql_url,mysql_db,mysql_pw,mysql_root,port):
        self.mysql_url = mysql_url
        self.mysql_db = mysql_db
        self.mysql_pw = mysql_pw
        self.mysql_root = mysql_root
        self.port = port

    @classmethod
    def from_crawler(cls, crawler):
        return  cls(
            mysql_url = crawler.settings.get('mysql_url'),
            mysql_db = crawler.settings.get('mysql_db'),
            mysql_pw = crawler.settings.get('mysql_pw'),
            mysql_root = crawler.settings.get('mysql_root'),
            port = crawler.settings.get('port')
        )


    def open_spider(self,spider):
        #self.connect = pymysql.connect(host=self.mysql_url,user=self.mysql_root,password=self.mysql_pw,port=self.port,db=self.mysql_db)
        self.connect = pymysql.connect(host="localhost", user="root", password="root",
                                       port=3306, db="mysql")
    def process_item(self, item, spider):
        cursor =self.connect.cursor()
        sql = "insert into lianjiaitem (region,href,name,style,area,orientation,decoration,elevator,floor,build_year,sign_time,unit_price,total_price,fangchan_class,school,subway)"
        sql += "values ('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s');" %(item['region'],item['href'],item['name'],'1','2','3','4','5','6','7','8','9','10','11','12',item['subway'])
        try:
            cursor.execute(sql)
            self.connect.commit()
        except:
            self.connect.rollback()
        return item
    def close_spider(self,spider):
        self.connect.close()
