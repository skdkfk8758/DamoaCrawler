
"""
becle Spider
Create :  2017.10.09

MAX_PAGE -> Damoa.spiders.Setting에 있음

"""

import scrapy

from Crawler.filterItem import *
from Crawler.items import DamoaItem
from Crawler.spiders.Setting import *
from Crawler.CreateItem import *

class Spider(scrapy.Spider):
    name = 'becle' # spider name

    baseUrl = "http://www.becle.net/"

    def start_requests(self):
        for i in range(1, MAX_PAGE, 1):
            yield scrapy.Request("http://www.becle.net/index.php?mid=best&page={}".format(i))
            yield scrapy.Request("http://www.becle.net/index.php?mid=drip&page={}".format(i))
            yield scrapy.Request("http://www.becle.net/index.php?mid=drip&search_target=extra_vars1&search_keyword=%EC%A0%95%EB%B3%B4&page={}".format(i))
            yield scrapy.Request("http://www.becle.net/index.php?mid=drip&search_target=extra_vars1&search_keyword=%EC%B0%BD%EC%9E%91&page={}".format(i))
            yield scrapy.Request("http://www.becle.net/index.php?mid=ssul&page={}".format(i))
            yield scrapy.Request("http://www.becle.net/index.php?mid=ssultoon&page={}".format(i))
            yield scrapy.Request("http://www.becle.net/index.php?mid=free&page={}".format(i))

    def parse(self, response):
        for select in response.xpath("//table/tbody/tr"):
            item = DamoaItem() # item객체 생성

            item['source'] = self.name

            titleXpath = "td/span/text()"
            item['title'] = createItemUseXpath(select, titleXpath, texttype="")
            if item['title'] == "공지":
                pass
            else:
                titleXpath = "td/a/text()"
                item['title'] = createItemUseXpath(select, titleXpath, texttype="")

                linkXpath = "td/a/@href"
                item['link'] = createItemUseXpath(select, linkXpath, texttype=TextType.LINK).split(" ")[0]

                item['attribute'] = str(item['link']).split("=")[1].replace("&page","").replace("&search_target","")

                dateXpath = "td[@class='time']/text()"
                item['date'] = createItemUseXpath(select, dateXpath, texttype=TextType.DATE)+":00"

                hitsXpath = "td/text()"
                item['hits'] = createItemUseXpath(select, hitsXpath, texttype=TextType.INT).split(" ")[-1]

                recommenedXpath = "td/text()"
                if select.xpath(recommenedXpath).extract()[0] == "-":
                    item['recommened'] = 0
                else:
                    item['recommened'] = createItemUseXpath(select, hitsXpath, texttype=TextType.INT).split(" ")[0]

                item['last_update'] = getCurrentTime("STR")

                item['pop'] = createItem_pop(item['date'], item['recommened'], item['hits'])

                tagName = "div"
                tagAttrs = {"id": "article_1"}
                if createItemUseBs4(item['link'], tagName, tagAttrs, encoding="utf8", texttype=TextType.TEXT) == "":
                    item['text'] = "None Text"
                else:
                    item['text'] = createItemUseBs4(item['link'], tagName, tagAttrs, encoding="utf8", texttype=TextType.TEXT)

                if filterItem(item) != None:
                    yield filterItem(item)



