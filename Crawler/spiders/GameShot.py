
"""
게임샷 크롤링 스파이더
Create : 2017.10.08

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
    name = 'gameshot' # spider name

    baseUrl = "http://www.gameshot.net/talk/"

    def start_requests(self):
        for i in range(1, MAX_PAGE, 1):
            yield scrapy.Request("http://www.gameshot.net/talk/?&bbs=free&sby=title&skey=&pg={}".format(i))
            yield scrapy.Request("http://www.gameshot.net/talk/?&bbs=gamenews&sby=title&skey=&pg={}".format(i))
            yield scrapy.Request("http://www.gameshot.net/talk/?&bbs=ip_shop&sby=title&skey=&pg={}".format(i))

    def parse(self, response):
        for select in response.xpath("//table/tbody/tr"):

            if select.xpath("td/text()").extract()[0] == "관리자":
                # 관리자가 작성한 게시물(공지) 거르고 크롤링
                pass
            else:
                item = DamoaItem() # item객체 생성

                item['source'] = self.name

                titleXpath = "td/p/a/strong/text()"
                item['title'] = createItemUseXpath(select, titleXpath, texttype="")

                linkXpath = "td/p/a/@href"
                item['link'] =  self.baseUrl + createItemUseXpath(select, linkXpath, texttype=TextType.LINK)

                attrXpath = "//li[@class='active']/text()"
                item['attribute'] = createItemUseXpath(select, attrXpath, texttype="")

                tagName = "p"
                tagAttrs =  {"class": "f12 a0a0a0"}
                item['date'] = createItemUseBs4(item['link'], tagName, tagAttrs, encoding="CP949", texttype=TextType.DATE)

                hitsXpath = "td/abbr/text()"
                item['hits'] = createItemUseXpath(select, hitsXpath, texttype=TextType.INT)

                item['recommened'] = 0

                item['last_update'] = getCurrentTime(TextType.STRING)

                item['pop'] = createItem_pop(item['date'], item['recommened'], item['hits'], self.name)

                tagName = "div"
                tagAttrs = {"id": "content"}
                item['text'] = createItemUseBs4(item['link'], tagName, tagAttrs, encoding="CP949", texttype=TextType.TEXT)

                item['image'] = createItemUseBs4_PostImage(item['link'], "'http://ftp'")

                yield item


