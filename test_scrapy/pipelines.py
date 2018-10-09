# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import scrapy
# from scrapy import Request
from scrapy.pipelines.images import ImagesPipeline
from scrapy.exceptions import DropItem


class TestScrapyPipeline(object):
    # def __init__(self):
    def process_item(self, item, spider):
        # print(spider, item)
        tpl = "%s\n%s\n\n" %(item['title'], item['href'])
        f = open('news.csv', 'a', newline='')
        f.write(tpl)
        f.close()


class MyImagesPipeline(ImagesPipeline):

    def get_media_requests(self, item, info):
        image_url = item['img_url']
        if image_url.split("/")[0] not in ("https:", "http:"):
            image_url = "http://www.xiaohuar.com" + image_url
            yield scrapy.Request(image_url, meta={'img_name': item['img_name']})
        else:
            yield scrapy.Request(image_url, meta={'img_name': item['img_name']})

    def item_completed(self, results, item, info):
        image_paths = [x['path'] for ok, x in results if ok]
        if not image_paths:
            raise DropItem("Item contains no images")
        item['image_paths'] = image_paths
        return item

    def file_path(self, request, response=None, info=None):
        img_name = request.meta['img_name']
        img_name_end = request.url.split('.')[-1]
        file_name = img_name+'.'+img_name_end
        return 'full/%s' % file_name
