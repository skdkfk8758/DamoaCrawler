
"""
기글하드웨어 Spider
Create :  2017.10.21

MAX_PAGE -> Damoa.spiders.Setting에 있음

"""

import scrapy

from Crawler.filterItem import *
from Crawler.items import DamoaItem
from Crawler.spiders.Setting import *
from Crawler.CreateItem import *

class Spider(scrapy.Spider):
    name = 'giggle' # spider name

    baseUrl = "https://gigglehd.com/gg/"

    def start_requests(self):
        for i in range(1, MAX_PAGE, 1):
            yield scrapy.Request("https://gigglehd.com/gg/index.php?mid=bbs&category=13759&page={}".format(i))
            yield scrapy.Request("https://gigglehd.com/gg/index.php?mid=bbs&category=207062&page={}".format(i))
            yield scrapy.Request("https://gigglehd.com/gg/index.php?mid=bbs&category=13770&page={}".format(i))
            yield scrapy.Request("https://gigglehd.com/gg/index.php?mid=bbs&category=856796&page={}".format(i))
            yield scrapy.Request("https://gigglehd.com/gg/index.php?mid=bbs&category=14058&page={}".format(i))

    def parse(self, response):
        for select in response.xpath("//table/tbody/tr"):
            item = DamoaItem() # item객체 생성

            item['source'] = self.name

            if createItemUseXpath(select, "td[@class='no']/strong/text()", texttype="")== "공지":
                # 공지사항 패스
                continue
            else:
                titleXpath = "td[@class='title']/a[@class='hx']/text()"
                item['title'] = createItemUseXpath(select, titleXpath, texttype="")

                linkXpath = "td[@class='title']/a/@href"
                item['link'] = createItemUseXpath(select, linkXpath, texttype=TextType.LINK)

                attrXpath = "td[@class='cate']/span/text()"
                item['attribute'] = createItemUseXpath(select, attrXpath, texttype="")

                tagName = "span"
                tagAttr = {"class": "date m_no"}
                item['date'] = "".join(createItemUseBs4(item['link'], tagName, tagAttr, texttype=TextType.DATE, encoding="utf8")) + ":00"

                tagName = "div"
                tagAttrs = {"class": "side fr"}
                item['hits'] = createItemUseBs4(item['link'], tagName, tagAttrs, texttype=TextType.INT, encoding="utf8").split(" ")[2]

                item['recommened'] = 0

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



