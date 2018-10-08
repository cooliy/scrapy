# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ChoutiItem(scrapy.Item):
    title = scrapy.Field()
    href = scrapy.Field()
    # desc = scrapy.Field()


class XiaohuarItem(scrapy.Item):
    img_name = scrapy.Field()
    img_url = scrapy.Field()
    # desc = scrapy.Field()

# class XiaohuarItem(scrapy.Item):
#     image_urls = scrapy.Field()
#     images = scrapy.Field()