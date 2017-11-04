
"""
This is Game Spider
Create :  2017.10.08

MAX_PAGE -> Damoa.spiders.Setting에 있음

2017.10.09
 - 코드정리

"""

import scrapy

from Crawler.filterItem import *
from Crawler.items import DamoaItem
from Crawler.spiders.Setting import *
from Crawler.CreateItem import *

class Spider(scrapy.Spider):
    name = 'thisisgame' # spider name

    baseUrl = "http://www.thisisgame.com"

    def start_requests(self):
        for i in range(1, MAX_PAGE, 1):
            yield scrapy.Request("http://www.thisisgame.com/webzine/community/tboard/?board=36&page={}".format(i))
            yield scrapy.Request("http://www.thisisgame.com/webzine/community/tboard/?board=37&page={}".format(i))
            yield scrapy.Request("http://www.thisisgame.com/webzine/community/tboard/?board=38&page={}".format(i))
            yield scrapy.Request("http://www.thisisgame.com/webzine/community/tboard/?board=39&page={}".format(i))
            yield scrapy.Request("http://www.thisisgame.com/webzine/community/tboard/?board=40&page={}".format(i))
            yield scrapy.Request("http://www.thisisgame.com/webzine/community/tboard/?board=956&page={}".format(i))
            yield scrapy.Request("http://www.thisisgame.com/webzine/community/tboard/?board=32&page={}".format(i))
            yield scrapy.Request("http://www.thisisgame.com/webzine/gallery/tboard/?board=33&&category=1&page={}".format(i))
            yield scrapy.Request("http://www.thisisgame.com/webzine/gallery/tboard/?board=33&&category=2&page={}".format(i))

    def parse(self, response):
        for select in response.xpath("//table/tbody/tr"):

            if select.xpath("td/span/text()").extract()[0] == "공지":
                # 공지사항 거르고 크롤링
                pass
            else:
                item = DamoaItem() # item객체 생성

                item['source'] = self.name

                titleXpath = "td/a/text()"
                item['title'] = createItemUseXpath(select, titleXpath, texttype="")

                linkXpath = "td/a/@href"
                item['link'] = self.baseUrl + createItemUseXpath(select, linkXpath, texttype=TextType.LINK)

                attrXpath = "//div[@class='board-title-part']/h1/a/strong/text()"
                item['attribute'] = createItemUseXpath(select, attrXpath, texttype="")

                tagName = "span"
                tagAttrs = {"class": "info-one postdate"}
                item['date'] = createItemUseBs4(item['link'], tagName, tagAttrs, encoding="utf8", texttype=TextType.DATE)

                tagName = "span"
                tagAttrs = {"class": "info-one readcount"}
                item['hits'] = createItemUseBs4(item['link'], tagName, tagAttrs, encoding="utf8", texttype=TextType.INT)

                recommenedXpath = "td/text()"
                item['recommened'] = createItemUseXpath(select, recommenedXpath, texttype=TextType.INT)[-1]

                item['last_update'] = getCurrentTime("str")

                item['pop'] = createItem_pop(item['date'], item['recommened'], item['hits'], self.name)

                tagName = "div"
                tagAttrs = {"class": "content board-content"}
                item['text'] = createItemUseBs4(item['link'], tagName, tagAttrs, encoding="utf8", texttype=TextType.TEXT)

                item['image'] = createItemUseBs4_PostImage(item['link'], "/upload/tboard/user")

                if item['pop'] < 1:
                    pass
                else:
                    yield item



