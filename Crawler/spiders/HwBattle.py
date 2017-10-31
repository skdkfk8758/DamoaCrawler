
"""
하드웨어배틀 Spider
Create :  2017.10.21

MAX_PAGE -> Damoa.spiders.Setting에 있음

"""

import scrapy

from Crawler.filterItem import *
from Crawler.items import DamoaItem
from Crawler.spiders.Setting import *
from Crawler.CreateItem import *

class Spider(scrapy.Spider):
    name = 'hwbattle' # spider name

    def start_requests(self):
        for i in range(1, MAX_PAGE, 1):
            yield scrapy.Request("http://www.hwbattle.com/bbs/board.php?bo_table=gameboard&sca=%EC%9E%A1%EB%8B%B4&page={}".format(i))
            yield scrapy.Request("http://www.hwbattle.com/bbs/board.php?bo_table=gameboard&sca=%EC%A7%88%EB%AC%B8&page={}".format(i))
            yield scrapy.Request("http://www.hwbattle.com/bbs/board.php?bo_table=gameboard&sca=%EB%A6%AC%EB%B7%B0+%EB%B0%8F+%EA%B3%B5%EB%9E%B5&page={}".format(i))
            yield scrapy.Request("http://www.hwbattle.com/bbs/board.php?bo_table=gameboard&sca=%EC%A0%95%EB%B3%B4&page={}".format(i))
            yield scrapy.Request("http://www.hwbattle.com/bbs/board.php?bo_table=gameboard&sca=%EA%B5%AC%EB%A7%A4%2F%EC%84%B8%EC%9D%BC&page={}".format(i))
            yield scrapy.Request("http://www.hwbattle.com/bbs/board.php?bo_table=gameboard&sca=%EB%B0%B0%EA%B7%B8&page={}".format(i))
            yield scrapy.Request("http://www.hwbattle.com/bbs/board.php?bo_table=cpumbram&sca=%EB%A9%94%EC%9D%B8%EB%B3%B4%EB%93%9C&page={}".format(i))
            yield scrapy.Request("http://www.hwbattle.com/bbs/board.php?bo_table=cpumbram&sca=CPU&page={}".format(i))
            yield scrapy.Request("http://www.hwbattle.com/bbs/board.php?bo_table=cpumbram&sca=%EB%A9%94%EB%AA%A8%EB%A6%AC&page={}".format(i))
            yield scrapy.Request("http://www.hwbattle.com/bbs/board.php?bo_table=cpumbram&sca=%EC%98%A4%EB%B2%84%ED%81%B4%EB%9F%AD&page={}".format(i))
            yield scrapy.Request("http://www.hwbattle.com/bbs/board.php?bo_table=vga&sca=%EC%A0%95%EB%B3%B4&page={}".format(i))
            yield scrapy.Request("http://www.hwbattle.com/bbs/board.php?bo_table=vga&sca=%EC%9E%A1%EB%8B%B4&page={}".format(i))
            yield scrapy.Request("http://www.hwbattle.com/bbs/board.php?bo_table=vga&sca=%EC%A7%88%EB%AC%B8&page={}".format(i))
            yield scrapy.Request("http://www.hwbattle.com/bbs/board.php?bo_table=hardwareboard&sca=SSD&page={}".format(i))
            yield scrapy.Request("http://www.hwbattle.com/bbs/board.php?bo_table=hardwareboard&sca=%ED%8C%8C%EC%9B%8C&page={}".format(i))
            yield scrapy.Request("http://www.hwbattle.com/bbs/board.php?bo_table=hardwareboard&sca=%EC%BC%80%EC%9D%B4%EC%8A%A4&page={}".format(i))
            yield scrapy.Request("http://www.hwbattle.com/bbs/board.php?bo_table=hardwareboard&sca=%EC%A3%BC%EB%B3%80%EA%B8%B0%EA%B8%B0&page={}".format(i))
            yield scrapy.Request("http://www.hwbattle.com/bbs/board.php?bo_table=softwareboard&sca=%EC%9A%B4%EC%98%81%EC%B2%B4%EC%A0%9C&page={}".format(i))
            yield scrapy.Request("http://www.hwbattle.com/bbs/board.php?bo_table=softwareboard&sca=%EC%A7%88%EB%AC%B8&page={}".format(i))
            yield scrapy.Request("http://www.hwbattle.com/bbs/board.php?bo_table=softwareboard&sca=%EC%A0%95%EB%B3%B4&page={}".format(i))
            yield scrapy.Request("http://www.hwbattle.com/bbs/board.php?bo_table=keyma&sca=%ED%82%A4%EB%B3%B4%EB%93%9C&page={}".format(i))
            yield scrapy.Request("http://www.hwbattle.com/bbs/board.php?bo_table=review&sca=%EC%82%AC%EC%9A%A9%EA%B8%B0&page={}".format(i))
            yield scrapy.Request("http://www.hwbattle.com/bbs/board.php?bo_table=review&sca=%ED%95%84%EB%93%9C%ED%85%8C%EC%8A%A4%ED%8A%B8&page={}".format(i))
            yield scrapy.Request("http://www.hwbattle.com/bbs/board.php?bo_table=review&sca=%EC%B2%B4%ED%97%98%EB%8B%A8&page={}".format(i))
            yield scrapy.Request("http://www.hwbattle.com/bbs/board.php?bo_table=freeboard&sca=%EC%9D%BC%EB%B0%98&page={}".format(i))
            yield scrapy.Request("http://www.hwbattle.com/bbs/board.php?bo_table=freeboard&sca=%EC%9E%A1%EB%8B%B4&page={}".format(i))
            yield scrapy.Request("http://www.hwbattle.com/bbs/board.php?bo_table=qaboard&sca=%EC%A7%88%EB%AC%B8&page={}".format(i))

    def parse(self, response):
        for select in response.xpath("//table/tbody/tr"):
            item = DamoaItem() # item객체 생성

            item['source'] = self.name

            if createItemUseXpath(select, "td[@class='td_num']/strong/text()", texttype="")== "공지":
                # 공지사항 패스
                continue
            else:
                titleXpath = "td[@class='td_subject']/a/text()"
                item['title'] = createItemUseXpath(select, titleXpath, texttype="")

                linkXpath = "td[@class='td_subject']/a/@href"
                item['link'] = createItemUseXpath(select, linkXpath, texttype=TextType.LINK).strip()

                attrXpath = "td[@class='td_subject']/a[@class='bo_cate_link']/text()"
                item['attribute'] = createItemUseXpath(select, attrXpath, texttype="")

                tagName = "section"
                tagAttr = {"id": "bo_v_info"}
                item['date'] = "20"+"".join(createItemUseBs4(item['link'], tagName, tagAttr, texttype=TextType.DATE, encoding="utf8")).split("조회")[0].split("작성")[2].strip() + ":00"

                tagName = "section"
                tagAttrs = {"id": "bo_v_info"}
                item['hits'] = createItemUseBs4(item['link'], tagName, tagAttrs, texttype=TextType.INT, encoding="utf8").split("조회")[1].split(" ")[0].replace("회","")

                item['recommened'] = 0

                item['last_update'] = getCurrentTime(TextType.STRING)

                item['pop'] = createItem_pop(item['date'], item['recommened'], item['hits'])

                tagName = "div"
                tagAttrs = {"id": "bo_v_con"}
                if createItemUseBs4(item['link'], tagName, tagAttrs, encoding="utf8", texttype=TextType.TEXT) == "":
                    item['text'] = "None Text"
                else:
                    item['text'] = createItemUseBs4(item['link'], tagName, tagAttrs, encoding="utf8", texttype=TextType.TEXT)

            if filterItem(item) != None:
                yield filterItem(item)



