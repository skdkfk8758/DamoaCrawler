
"""
FM Korea Spider
Create :  2017.10.23

MAX_PAGE -> Damoa.spiders.Setting에 있음

"""

import scrapy

from Crawler.filterItem import *
from Crawler.items import DamoaItem
from Crawler.spiders.Setting import *
from Crawler.CreateItem import *

class Spider(scrapy.Spider):
    name = 'fmkorea' # spider name

    baseUrl = "http://www.fmkorea.com/"

    def start_requests(self):
        for i in range(1, 2, 1):
            yield scrapy.Request("http://www.fmkorea.com/index.php?mid=humor&page={}".format(i))
            yield scrapy.Request("http://www.fmkorea.com/index.php?mid=mystery&page={}".format(i))
            yield scrapy.Request("http://www.fmkorea.com/index.php?mid=news&page={}".format(i))
            yield scrapy.Request("http://www.fmkorea.com/index.php?mid=free&page={}".format(i))
            yield scrapy.Request("http://www.fmkorea.com/index.php?mid=sreckovic&page={}".format(i))
            yield scrapy.Request("http://www.fmkorea.com/index.php?mid=love&page={}".format(i))
            yield scrapy.Request("http://www.fmkorea.com/index.php?mid=fashion&page={}".format(i))
            yield scrapy.Request("http://www.fmkorea.com/index.php?mid=gomin&page={}".format(i))
            yield scrapy.Request("http://www.fmkorea.com/index.php?mid=job&page={}".format(i))
            yield scrapy.Request("http://www.fmkorea.com/index.php?mid=car&page={}".format(i))
            yield scrapy.Request("http://www.fmkorea.com/index.php?mid=study&page={}".format(i))
            yield scrapy.Request("http://www.fmkorea.com/index.php?mid=baseball&page={}".format(i))
            yield scrapy.Request("http://www.fmkorea.com/index.php?mid=other_sports&page={}".format(i))
            yield scrapy.Request("http://www.fmkorea.com/index.php?mid=basketball&page={}".format(i))
            yield scrapy.Request("http://www.fmkorea.com/index.php?mid=stock&page={}".format(i))
            yield scrapy.Request("http://www.fmkorea.com/index.php?mid=fm17free&page={}".format(i))
            yield scrapy.Request("http://www.fmkorea.com/index.php?mid=fm17tips&page={}".format(i))
            yield scrapy.Request("http://www.fmkorea.com/index.php?mid=fm17tqna&page={}".format(i))
            yield scrapy.Request("http://www.fmkorea.com/index.php?mid=game_fifa&page={}".format(i))
            yield scrapy.Request("http://www.fmkorea.com/index.php?mid=fifa_series&page={}".format(i))
            yield scrapy.Request("http://www.fmkorea.com/index.php?mid=lol&page={}".format(i))
            yield scrapy.Request("http://www.fmkorea.com/index.php?mid=battlegrounds&page={}".format(i))
            yield scrapy.Request("http://www.fmkorea.com/index.php?mid=overwatch&page={}".format(i))
            yield scrapy.Request("http://www.fmkorea.com/index.php?mid=mgame&page={}".format(i))
            yield scrapy.Request("http://www.fmkorea.com/index.php?mid=gf&page={}".format(i))
            yield scrapy.Request("http://www.fmkorea.com/index.php?mid=Seven&page={}".format(i))
            yield scrapy.Request("http://www.fmkorea.com/index.php?mid=gallery_foods&page={}".format(i))
            yield scrapy.Request("http://www.fmkorea.com/index.php?mid=stock&page={}".format(i))
            yield scrapy.Request("http://www.fmkorea.com/index.php?mid=fm17players&page={}".format(i))

    def parse(self, response):
        for select in response.xpath("//table/tbody/tr"):
            item = DamoaItem() # item객체 생성

            item['source'] = self.name

            if createItemUseXpath(select, "td[@class='cate']/a/text()", texttype="") == "공지" \
                    or (createItemUseXpath(select, "td[@class='title']/a/text()", texttype="")).split(" ")[0] == "":
                # 공지사항 패스
                continue
            else:
                titleXpath = "td[@class='title']/a/text()"
                item['title'] = createItemUseXpath(select, titleXpath, texttype="")

                linkXpath = "td[@class='title']/a/@href"
                item['link'] = (self.baseUrl + createItemUseXpath(select, linkXpath, texttype=TextType.LINK)).split(' ')[0]

                attrXpath = "td[@class='cate']/span/a/text()"
                item['attribute'] = createItemUseXpath(select, attrXpath, texttype="")

                tagName = "span"
                tagAttr = {"class": "date"}
                item['date'] = "".join(createItemUseBs4(item['link'], tagName, tagAttr, texttype=TextType.DATE, encoding="utf8")) + ":00"

                hitsXpath = "td[@class='m_no']/text()"
                item['hits'] = createItemUseXpath(select, hitsXpath, texttype=TextType.INT)

                tagName = "div"
                tagAttrs = {"class": "side fr"}
                item['recommened'] = createItemUseBs4(item['link'], tagName, tagAttrs, encoding="utf8", texttype=TextType.INT).split(" ")[-3]

                item['last_update'] = getCurrentTime(TextType.STRING)

                item['pop'] = createItem_pop(item['date'], item['recommened'], item['hits'])

                tagName = "div"
                tagAttrs = {"class": "xe_content"}
                if createItemUseBs4(item['link'], tagName, tagAttrs, encoding="utf8", texttype=TextType.TEXT) == "":
                    item['text'] = "None Text"
                else:
                    item['text'] = createItemUseBs4(item['link'], tagName, tagAttrs, encoding="utf8", texttype=TextType.TEXT)

                item['image'] = createItemUseBs4_PostImage(item['link'])

                yield item


