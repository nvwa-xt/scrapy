# -*- coding: utf-8 -*-

from scrapy.spiders import Spider
from scrapy.selector import Selector

from wy.items import Website
import sys
import string

reload(sys)
sys.setdefaultencoding('utf8') 

sys.stdout=open('output.txt','w') #将打印信息输出在相应的位置下

class WooYunSpider(Spider):
    name = "wooyun"
    allowed_domains = ["wooyun.org"]
    start_urls = ["http://wooyun.org/whitehats/do/1/page/2",]

    def parse(self, response):
     sel = Selector(response)
     sites = sel.xpath('//tbody')
     items = []
     for site in  sites:
         item = Website()

         name = site.xpath('//td/a/text()').extract()
         url  = site.xpath('//td/a/@href').extract()

         item['name'] = [n.encode('utf-8') for n in name]
         item['url']  = [u.encode('utf-8') for u in url ]
         items.append(item)
        
     return items
     


