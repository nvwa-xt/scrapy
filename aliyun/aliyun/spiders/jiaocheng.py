# -*- coding: utf-8 -*-
import scrapy
from aliyun.items import AliyunItem

class JiaochengSpider(scrapy.Spider):
    name = 'jiaocheng'
    allowed_domains = ['aliyun.com']
    start_urls = []
    for i in range(1, 200):
        start_urls.append('https://m.aliyun.com/jiaocheng/python-'+str(i)+'.html')

    def parse(self, response):
        item = AliyunItem()
        item['title'] = response.xpath('//div[@data-spm="3"]/a/text()').extract()
        item['link'] = response.xpath('//div[@data-spm="3"]/a/@href').extract()
        return item
