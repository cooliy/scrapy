# -*- coding: utf-8 -*-
import scrapy
# import sys
# import io
# sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='gb18030')
from scrapy.selector import Selector
from scrapy.http import Request

class XiaohuarSpider(scrapy.Spider):
    name = 'xiaohuar'
    allowed_domains = ['xiaohuar.com']
    start_urls = ['http://www.xiaohuar.com/list-1-0.html']

    def parse(self, response):
        hxs = Selector(response=response).xpath('//div[@class="item_t"]')
        for obj in hxs:
            # title = obj.xpath('.//img/@alt').extract_first()
            img_url = obj.xpath('.//img/@src').extract_first()
            img_name = obj.xpath('.//span[@class="price"]/text()').extract_first()
            print(img_name, '\n', img_url.strip(), '\n\n')




