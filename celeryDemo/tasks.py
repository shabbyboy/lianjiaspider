from __future__ import absolute_import
from celeryDemo.celeryConf import app
from celeryDemo.scrapyLijia import scrapyProcess

@app.task
def spider(region):
    q =[]
    process = scrapyProcess(region,q,"Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:31.0) Gecko/20100101 Firefox/31.0",None,5)
    process.run()
