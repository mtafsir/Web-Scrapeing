# -*- coding: utf-8 -*-
import scrapy


class HarSpider(scrapy.Spider):
    name = 'Har_'
    allowed_domains = ['Har.com']
    start_urls = ['http://Har.com/']

    def parse(self, response):
        pass
