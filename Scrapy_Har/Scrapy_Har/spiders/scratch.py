# -*- coding: utf-8 -*-
import scrapy

print('Hello it works')
class HarWebsiteSpider(scrapy.Spider):
    name = "Har_website"
    allowed_domains = ["har.com/zipcode_75081/realestate/for_sale"]
    start_urls = (
        'http://www.har.com/zipcode_75081/realestate/for_sale',
    )

    def parse(self, response):
        y=0

        h1_Address = response.xpath('//a[@class="address"]/span/text()').extract
        h1_Address_str = "" + str(h1_Address)
        h1_Address_str = h1_Address_str.split("data=u")
        h1_Address_str[0] = "skip'"


        h1_Price = response.xpath('//div[@class="price"]/text()').extract
        h1_Price_str = "" + str(h1_Price)
        h1_Price_str = h1_Price_str.split("data=u")
        h1_Price_str[0] = "skip'"

        f=open(r'C:\Users\mtafs\Desktop\Test\Test.txt', 'w+')
        for x in h1_Address_str:

                Address = x[1:len(x)-1]
                match_Address = Address.find("'")

                Price_out = h1_Price_str[y]

                Price = Price_out[1:len(Price_out)-1]
                match_Price = Price.find("'")

        h1_Price = response.xpath('//div[@class="price"]/text()').extract
        h1_Price_str = "" + str(h1_Price)
        h1_Price_str = h1_Price_str.split("data=u")
        h1_Price_str[0] = "skip'"


        f=open(r'C:\Users\mtafs\Desktop\Test\Test.txt', 'w+')
        for x in h1_Address_str:

                Address = x[1:len(x)-1]
                match_Address = Address.find("'")

                Price_out = h1_Price_str[y]

                Price = Price_out[1:len(Price_out)-1]
                match_Price = Price.find("'")

                f.write("\n Ouput: %s (break) %s" % (x[1:match_Address],Price_out[1:match_Price]))

                y=y+1
        f.close()


