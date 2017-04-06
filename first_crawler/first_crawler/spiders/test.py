# -*- coding: utf-8 -*-
"""
Created on Fri Mar 24 14:22:07 2017

@author: yfan

it is the first scrapy file

"""
import csv
from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector
from first_crawler.items import FirstCrawlerItem

class firstwebscrapy(BaseSpider):
    name = 'first_web_spider'
    allowed_domains = ["craigslist.org"]
    start_urls = ["https://sfbay.craigslist.org/search/npo/"]

    def parse(self, response):
        hxs = HtmlXPathSelector(response)
#        print response
        titles = hxs.xpath("//ul[@class = 'rows']")
        items = []
        item = FirstCrawlerItem()
        for title in titles:
            item['title'] = titles.select("li/p/a/text()").extract()
#            items.append(item)
            items.append(item)
        return items
        
        
#    with open('C:\scrapy\first_crawler\first_crawler\result.csv', 'wb') as output:
#        writer = csv.writer(output, delimiter=',')
#        writer.writerows(enumerate(items))
#        print titles
#        print titles
#        items = []
#        for titles in titles:
#            item = FirstCrawlerItem()
#            item["title"] = titles.select("a/text()").extract()
##            item["link"] = titles.select("a/@href").extract()
#            items.append(item)
#        return items
#        for article in articles:
#            title = articles.select("a/text()").extract()
#            print title

