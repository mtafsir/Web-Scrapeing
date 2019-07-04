# -*- coding: utf-8 -*-
import scrapy

class TestHarSpider(scrapy.Spider):
    name = 'Test_Har'
    allowed_domains = ['har.com/zipcode_75081/realestate/for_sale']
    start_urls = ['http://har.com/zipcode_75081/realestate/for_sale/']

    def parse(self, response):
        pass
