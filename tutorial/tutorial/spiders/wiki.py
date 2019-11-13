# -*- coding: utf-8 -*-
import scrapy
from tutorial.items import WikiItem

class QuotesSpider(scrapy.Spider):
    name = 'wiki'
    allowed_domains = ['www.nw-siken.com']
    start_urls = ['https://www.nw-siken.com/kakomon/30_aki/']

    def parse(self, response):
            time.sleep(4)
            item = WikiItem()
            for i in response.xpath('//table/tbody/tr'):
                item['name'] = i.xpath('td[2]/text()').extract_first()
                item['context'] = i.xpath('td[3]/text()').extract()

                print(i.xpath('td[2]/text()').extract_first())
                print(i.xpath('td[3]/text()').extract())


            yield item
