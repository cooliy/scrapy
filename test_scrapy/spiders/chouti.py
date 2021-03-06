# -*- coding: utf-8 -*-
import scrapy
# import sys
# import io
# sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='gb18030')
from scrapy.selector import Selector
from scrapy.http import Request
from ..items import ChoutiItem

class ChoutiSpider(scrapy.Spider):
    name = 'chouti'
    allowed_domains = ['chouti.com']
    start_urls = ['http://dig.chouti.com/']

    # visited_urls = set()

    def parse(self, response):
        # print(response, type(response))
        # content = str(response.body, encoding='utf-8')
        # print(content)
        # hxs = Selector(response=response).xpath('//a')
        # for i in hxs:
        #     print(i)
        # -----------------获取页面中的新闻text----------------------------
        hxs1 = Selector(response=response).xpath('//div[@class="item"]')
        for obj in hxs1:

            title = obj.xpath('.//a[@class="show-content color-chag"]/text()').extract_first().strip()
            href = obj.xpath('.//a[@class="show-content color-chag"]/@href').extract_first().strip()
            item_obj = ChoutiItem(title=title, href=href)
            yield item_obj # 将对像传到pipeline

        # -----------------获取所有页码链接----------------------------
        hxs2 = Selector(response=response).xpath(
            '//div[@id="dig_lcpage"]//a/@href').extract()
        for url in hxs2:
            # 调用urljoin方法构造成一个绝对的url
            url = response.urljoin(url)
            # # 将要访问的新url添加到调度器callback回调函数
            yield Request(url=url, callback=self.parse)

    # def md5(self, url):
    #     import hashlib
    #     obj = hashlib.md5()
    #     obj.update(bytes(url, encoding='utf-8'))
    #     return obj.hexdigest()
