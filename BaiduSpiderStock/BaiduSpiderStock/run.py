# -*- coding: utf-8 -*-
# @Time : 2017/1/1 17:51
# @Author : woodenrobot
from scrapy import cmdline

name = 'stocks'
cmd = 'scrapy crawl {0}'.format(name)
cmdline.execute(cmd.split())