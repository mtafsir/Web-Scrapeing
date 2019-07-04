# -*- coding: utf-8 -*-
import scrapy


class HarWebsiteSpider(scrapy.Spider):
    name = 'Har_Website'
    allowed_domains = ['Har.com']
    start_urls = ['http://Har.com/']

    def parse(self, response):
        pass
