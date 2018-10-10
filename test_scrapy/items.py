# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ChoutiItem(scrapy.Item):

    title = scrapy.Field()
    href = scrapy.Field()


class XiaohuarItem(scrapy.Item):
    title = scrapy.Field()
    img_name = scrapy.Field()
    img_url = scrapy.Field()
    image_paths = scrapy.Field()

<<<<<<< HEAD
=======

>>>>>>> da14fbcf45a369ac4b91f521c39f9ef71d85f55e
class QuoteItem(scrapy.Item):
    text = scrapy.Field()
    author = scrapy.Field()
    tags = scrapy.Field()



