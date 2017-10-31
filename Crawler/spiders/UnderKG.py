
"""
UnderKG Spider
Create :  2017.10.19

MAX_PAGE -> Damoa.spiders.Setting에 있음

"""

import scrapy

from Crawler.filterItem import *
from Crawler.items import DamoaItem
from Crawler.spiders.Setting import *
from Crawler.CreateItem import *
from Crawler.TextTypeEnum import *

class Spider(scrapy.Spider):
    name = 'underkg' # spider name

    baseUrl = "http://underkg.co.kr/"

    def start_requests(self):
        for i in range(1, MAX_PAGE, 1):
            yield scrapy.Request("http://underkg.co.kr/index.php?mid=freeboard&page={}".format(i))
            yield scrapy.Request("http://underkg.co.kr/index.php?mid=QnA&page={}".format(i))
            yield scrapy.Request("http://underkg.co.kr/index.php?mid=user_review&page={}".format(i))

    def parse(self, response):
        for select in response.xpath("//table/tbody/tr"):

            item = DamoaItem() # item객체 생성

            item['source'] = self.name

            titleXpath = "td[@class='notice']/text()"
            item['title'] = createItemUseXpath(select, titleXpath, texttype="")
            if item['title'] == "공지":
                pass
            else:
                titleXpath = "td[@class='title']/a/text()"
                item['title'] = createItemUseXpath(select, titleXpath, texttype="")

                linkXpath = "td/a/@href"
                item['link'] = createItemUseXpath(select, linkXpath, texttype=TextType.LINK)

                attrXpath = "//div/div/div/div/div/text()"
                item['attribute'] = createItemUseXpath(select, attrXpath, texttype=TextType.TEXT).strip()

                dateXpath = "td[@class='time']/text()"
                item['date'] = createItemUseXpath(select, dateXpath, texttype=TextType.DATE)+" 00:00:00"

                hitsXpath = "td[@class='readNum']/text()"
                item['hits'] = createItemUseXpath(select, hitsXpath, texttype=TextType.INT)

                recommenedXpath = "td[@class='voteNum']/text()"
                item['recommened'] = createItemUseXpath(select, recommenedXpath, texttype=TextType.INT)

                item['last_update'] = getCurrentTime(TextType.STRING)

                item['pop'] = createItem_pop(item['date'], item['recommened'], item['hits'])

                tagName = "div"
                tagAttrs = {"class": "xe_content"}
                item['text'] = createItemUseBs4(item['link'], tagName, tagAttrs, encoding="utf8", texttype=TextType.INT)

                if filterItem(item) != None:
                    yield filterItem(item)



