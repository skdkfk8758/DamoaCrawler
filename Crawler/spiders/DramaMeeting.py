
"""
드라마미팅 Spider
Create :  2017.10.09

MAX_PAGE -> Damoa.spiders.Setting에 있음

"""

import scrapy

from Crawler.filterItem import *
from Crawler.items import DamoaItem
from Crawler.spiders.Setting import *
from Crawler.CreateItem import *

class Spider(scrapy.Spider):
    name = 'dramameeting' # spider name

    baseUrl = "http://www.dramameeting.com/"

    def start_requests(self):
        for i in range(1, MAX_PAGE, 1):
            yield scrapy.Request("http://www.dramameeting.com/index.php?mid=entertainment&page={}".format(i))
            yield scrapy.Request("http://www.dramameeting.com/index.php?mid=broadcast&page={}".format(i))
            yield scrapy.Request("http://www.dramameeting.com/index.php?mid=photo&page={}".format(i))
            yield scrapy.Request("http://www.dramameeting.com/index.php?mid=music&page={}".format(i))
            yield scrapy.Request("http://www.dramameeting.com/index.php?mid=drama&page={}".format(i))
            yield scrapy.Request("http://www.dramameeting.com/index.php?mid=review&page={}".format(i))
            yield scrapy.Request("http://www.dramameeting.com/index.php?mid=humor&page={}".format(i))
            yield scrapy.Request("http://www.dramameeting.com/index.php?mid=humor&page={}".format(i))
            yield scrapy.Request("http://www.dramameeting.com/index.php?mid=love&page={}".format(i))
            yield scrapy.Request("http://www.dramameeting.com/index.php?mid=fashion&page={}".format(i))
            yield scrapy.Request("http://www.dramameeting.com/index.php?mid=mystery&page={}".format(i))

    def parse(self, response):
        for select in response.xpath("//table/tbody/tr"):
            item = DamoaItem() # item객체 생성

            item['source'] = self.name

            titleXpath = "td[@class='no']/strong/text()"
            item['title'] = createItemUseXpath(select, titleXpath, texttype="")
            if item['title'] != "":
                pass
            else:
                titleXpath = "td[@class='title']/a/text()"
                item['title'] = createItemUseXpath(select, titleXpath, texttype="")

                linkXpath = "td[@class='title']/a/@href"
                item['link'] = createItemUseXpath(select, linkXpath, texttype=TextType.LINK).split(" ")[0]

                item['attribute'] = str(item['link']).split("/")[3].split("=")[1].replace("&page","")

                dateXpath = "td[@class='time']/text()"
                item['date'] = createItemUseXpath(select, dateXpath, texttype=TextType.DATE)+" 00:00:00"

                item['hits'] = 0

                tagName = "div"
                tagAttrs = {"class":"side fr"}
                item['recommened'] = createItemUseBs4(item['link'], tagName, tagAttrs, encoding="utf8", texttype=TextType.INT).split(" ")[3]

                item['last_update'] = getCurrentTime(TextType.STRING)

                item['pop'] = createItem_pop(item['date'], item['recommened'], item['hits'])

                tagName = "div"
                tagAttrs = {"class": "rd_body clear"}
                if createItemUseBs4(item['link'], tagName, tagAttrs, encoding="utf8", texttype=TextType.TEXT) == "":
                    item['text'] = "None Text"
                else:
                    item['text'] = createItemUseBs4(item['link'], tagName, tagAttrs, encoding="utf8", texttype=TextType.TEXT)

                if filterItem(item) != None:
                    yield filterItem(item)



