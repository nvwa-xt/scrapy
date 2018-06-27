# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class AliyunPipeline(object):
    def process_item(self, item, spider):
        fileName = 'jiaocheng.txt'
        for i in range(1, 10000):
            link = item['link'][i]
            title = item['title'][]
            with open(fileName, 'a') as fp:
                fp.write(link)
                fp.write(title)
                fp.close()
            return item

