# -*- coding: utf-8 -*-
import scrapy
# import sys
# import io
# sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='gb18030')
from scrapy.selector import Selector
from scrapy.http import Request
from ..items import XiaohuarItem


class XiaohuarSpider(scrapy.Spider):
    name = 'xiaohuar'
    allowed_domains = ['xiaohuar.com']
    start_urls = ['http://www.xiaohuar.com/hua']
    # visited_urls = set()

    def md5(self, url):
        import hashlib
        obj = hashlib.md5()
        obj.update(bytes(url, encoding='utf-8'))
        return obj.hexdigest()

    def parse(self, response):
        # 获取页面中校花名字和校花图片地址
        hxs1 = Selector(response=response).xpath('//div[@class="item_t"]')
        for obj in hxs1:
            item = XiaohuarItem()
            item['title'] = obj.xpath('.//img/@alt').extract_first()
            item['img_url'] = obj.xpath('.//img/@src').extract_first().strip()
            item['img_name'] = obj.xpath(
                './/span[@class="price"]/text()').extract_first()
            # print(img_name, '\n', img_urls.strip(), '\n\n')
            # item = XiaohuarItem(imgs=img_name, img_url=img_urls.strip())
            yield item  # 将对像传到pipeline
        # 获取页面中的所有链接地址
        hxs2 = Selector(response=response).xpath(
            '//div[@class="page_num"]//a/@href').extract()
        for url in hxs2:
            # 将要访问的新url添加到调度器
            yield Request(url=url, callback=self.parse)
