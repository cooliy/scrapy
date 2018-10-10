# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import scrapy
<<<<<<< HEAD
# from scrapy import Request
=======
import pymongo
>>>>>>> da14fbcf45a369ac4b91f521c39f9ef71d85f55e
from scrapy.pipelines.images import ImagesPipeline
from scrapy.exceptions import DropItem


class TestScrapyPipeline(object):
    def process_item(self, item, spider):
        tpl = "%s\n%s\n\n" %(item['title'], item['href'])
        f = open('news.csv', 'a', newline='')
        f.write(tpl)
        f.close()


class MyImagesPipeline(ImagesPipeline):
    def get_media_requests(self, item, info):
        image_url = item['img_url']
        if image_url.split("/")[0] not in ("https:", "http:"):
            image_url = "http://www.xiaohuar.com" + image_url
            yield scrapy.Request(url=image_url, meta={'img_name': item['img_name']})
        else:
            yield scrapy.Request(url=image_url, meta={'img_name': item['img_name']})

    def item_completed(self, results, item, info):
        image_paths = [x['path'] for ok, x in results if ok]
        if not image_paths:
            raise DropItem("Item contains no images")
        item['image_paths'] = image_paths
        return item

    def file_path(self, request, response=None, info=None):
        img_name = request.meta['img_name']
        img_name_end = request.url.split('.')[-1]
        # s = open('x.txt', 'a')
        # f = "%s\n" % request.url
        # s.write(f)
        # s.close()
        file_name = img_name+'.'+img_name_end
        return 'full/%s' % file_name


class TextPipeline(object):
    def __init__(self):
        self.limit = 50

    def process_item(self, item, spider):
        if item['text']:
            if len(item['text']) > self.limit:
                item['text'] = item['text'][0:self.limit].rstrip() + '...'
            return item
        else:
            return DropItem('Missing Text')

class MongoPipeline(object):
    def __init__(self, mongo_uri, mongo_db):
        self.mongo_uri = mongo_uri
        self.mongo_db = mongo_db

    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            mongo_uri=crawler.settings.get('MONGO_URI'),
            mongo_db=crawler.settings.get('MONGO_DB')
        )

    def open_spider(self, spider):
        self.client = pymongo.MongoClient(self.mongo_uri)
        self.db = self.client[self.mongo_db]

    def process_item(self, item, spider):
        name = item.__class__