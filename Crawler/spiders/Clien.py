
"""
Clien Spider
Create : 2017.06.14

2017.10.09
 - 코드정리

"""
import scrapy

from Crawler.items import DamoaItem
from Crawler.spiders.Setting import *
from Crawler.CreateItem import *

class Clien(scrapy.Spider):
    name = 'clien' # spider name

    baseUrl = "http://www.clien.net"

    def start_requests(self):
        for i in range(1, MAX_PAGE, 1):
            yield scrapy.Request('http://clien.net/service/board/park?&od=T31&po={0}'.format(i - 1))
            yield scrapy.Request('http://clien.net/service/board/kin?&od=T31&po={0}'.format(i - 1))
            yield scrapy.Request('http://clien.net/service/board/news?&od=T31&po={0}'.format(i - 1))
            yield scrapy.Request('http://clien.net/service/board/useful?&od=T31&po={0}'.format(i - 1))
            yield scrapy.Request('http://clien.net/service/board/pds?&od=T31&po={0}'.format(i - 1))
            yield scrapy.Request('http://clien.net/service/board/lecture?&od=T31&po={0}'.format(i - 1))
            yield scrapy.Request('http://clien.net/service/board/use?&od=T31&po={0}'.format(i - 1))
            yield scrapy.Request('http://clien.net/service/board/chehum?&od=T31&po={0}'.format(i - 1))
            yield scrapy.Request('http://clien.net/service/board/bug?&od=T31&po={0}'.format(i - 1))

    def parse(self, response):
        for select in response.xpath('//div[@class="item"]'):

            try:
                if select.xpath("div[@class='list-symph']/span/text()").extract()[0] == "공지":
                    pass
            except:
                item = DamoaItem()  # item객체 생성

                item['source'] = self.name

                titleXpath = "div[@class='list-title']/a[@class='list-subject']/text()"
                item['title'] = createItemUseXpath(select, titleXpath, texttype="")

                linkXpath = "div[@class='list-title']/a/@href"
                item['link'] = self.baseUrl + createItemUseXpath(select, linkXpath, texttype=TextType.LINK)

                tagName = "li"
                tagAttr = {"class": "board-title"}
                item['attribute'] = createItemUseBs4(item['link'], tagName, tagAttr, encoding="CP949",texttype=TextType.CLIEN)

                dateXpath = "div/span[@class='time']/span[@class='timestamp']/text()"
                item['date'] = createItemUseXpath(select, dateXpath,texttype="")

                tagName = "span"
                tagAttr = {"class" : "view-count"}
                item['hits'] = createItemUseBs4(item['link'], tagName, tagAttr, encoding="CP949",texttype=TextType.INT)

                tagName = "div"
                tagAttr = {"class": "title-symph"}
                item['recommened'] = createItemUseBs4(item['link'], tagName, tagAttr, encoding="CP949",texttype=TextType.INT)

                item['last_update'] = getCurrentTime(TextType.STRING)

                item['pop'] = createItem_pop(item['date'], item['recommened'], item['hits'], self.name)

                tagName = "div"
                tagAttrs = {"class": "post-content"}
                item['text'] = createItemUseBs4(item['link'], tagName, tagAttrs, encoding="CP949", texttype=TextType.TEXT)

                item['image'] = createItemUseBs4_PostImage(item['link'], "web/api/file/F01")

                yield item



