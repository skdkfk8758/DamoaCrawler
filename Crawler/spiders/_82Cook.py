
"""
82cook Spider
Create :  2017.10.19

MAX_PAGE -> Damoa.spiders.Setting에 있음

"""

import scrapy

from Crawler.filterItem import *
from Crawler.items import DamoaItem
from Crawler.spiders.Setting import *
from Crawler.CreateItem import *

class Spider(scrapy.Spider):
    name = '82cook' # spider name

    baseUrl = "http://www.82cook.com/entiz/"

    def start_requests(self):
        for i in range(1, MAX_PAGE, 1):
            yield scrapy.Request("http://www.82cook.com/entiz/enti.php?bn=1&page={}".format(i))
            yield scrapy.Request("http://www.82cook.com/entiz/enti.php?bn=2&page={}".format(i))
            yield scrapy.Request("http://www.82cook.com/entiz/enti.php?bn=3&page={}".format(i))
            yield scrapy.Request("http://www.82cook.com/entiz/enti.php?bn=31&page={}".format(i))
            yield scrapy.Request("http://www.82cook.com/entiz/enti.php?bn=6&page={}".format(i))
            yield scrapy.Request("http://www.82cook.com/entiz/enti.php?bn=7&page={}".format(i))
            yield scrapy.Request("http://www.82cook.com/entiz/enti.php?bn=8&page={}".format(i))
            yield scrapy.Request("http://www.82cook.com/entiz/enti.php?bn=9&page={}".format(i))
            yield scrapy.Request("http://www.82cook.com/entiz/enti.php?bn=11&page={}".format(i))
            yield scrapy.Request("http://www.82cook.com/entiz/enti.php?bn=12&page={}".format(i))
            yield scrapy.Request("http://www.82cook.com/entiz/enti.php?bn=13&page={}".format(i))
            yield scrapy.Request("http://www.82cook.com/entiz/enti.php?bn=14&page={}".format(i))
            yield scrapy.Request("http://www.82cook.com/entiz/enti.php?bn=15&page={}".format(i))
            yield scrapy.Request("http://www.82cook.com/entiz/enti.php?bn=16&page={}".format(i))
            yield scrapy.Request("http://www.82cook.com/entiz/enti.php?bn=17&page={}".format(i))


    # 사이트 파싱
    def parse(self, response):
        for select in response.xpath("//table/tbody/tr"):

            item = DamoaItem() # item객체 생성

            item['source'] = self.name

            titleXpath = "td/a/b/text()"
            item['title'] = createItemUseXpath(select, titleXpath, texttype="")
            if item['title'] != "":
                pass
            else:
                titleXpath = "td[@class='title']/a/text()"
                item['title'] = createItemUseXpath(select, titleXpath, texttype="")

                linkXpath = "td/a/@href"
                item['link'] = self.baseUrl + createItemUseXpath(select, linkXpath, texttype=TextType.LINK)

                attrXpath = "//div/div/div/h1/text()"
                item['attribute'] = createItemUseXpath(select, attrXpath, texttype=TextType.TEXT)

                tagName = "div"
                tagAttrs = {"class": "readRight"}
                item['date'] = createItemUseBs4(item['link'], tagName, tagAttrs, encoding="utf8", texttype=TextType.DATE)

                hitsXpath = "td[@class='numbers']/text()"
                item['hits'] = createItemUseXpath(select, hitsXpath, texttype=TextType.INT).split(" ")[0]

                recommenedXpath = "td[@class='numbers']/text()"
                item['recommened'] = createItemUseXpath(select, recommenedXpath, texttype=TextType.INT).split(" ")[1]

                item['last_update'] = getCurrentTime(TextType.STRING)

                item['pop'] = createItem_pop(item['date'], item['recommened'], item['hits'])

                tagName = "div"
                tagAttrs = {"id": "articleBody"}
                item['text'] = createItemUseBs4(item['link'], tagName, tagAttrs, encoding="utf8", texttype=TextType.TEXT)

                item['image'] = createItemUseBs4_PostImage(item['link'])

                yield item



