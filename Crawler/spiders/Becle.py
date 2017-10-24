
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

    # 각 게시판별로 리퀘스트 요청
    def start_requests(self):
        for i in range(1, MAX_PAGE, 1):
            yield scrapy.Request("http://www.becle.net/index.php?mid=best&page={}".format(i))
            yield scrapy.Request("http://www.becle.net/index.php?mid=drip&page={}".format(i))
            yield scrapy.Request("http://www.becle.net/index.php?mid=drip&search_target=extra_vars1&search_keyword=%EC%A0%95%EB%B3%B4&page={}".format(i))
            yield scrapy.Request("http://www.becle.net/index.php?mid=drip&search_target=extra_vars1&search_keyword=%EC%B0%BD%EC%9E%91&page={}".format(i))
            yield scrapy.Request("http://www.becle.net/index.php?mid=ssul&page={}".format(i))
            yield scrapy.Request("http://www.becle.net/index.php?mid=ssultoon&page={}".format(i))
            yield scrapy.Request("http://www.becle.net/index.php?mid=free&page={}".format(i))

    # 리스폰스 받아서 사이트 파싱
    def parse(self, response):
        for select in response.xpath("//table/tbody/tr"):
            item = DamoaItem() # item객체 생성

            # 게시물 출처 저장
            item['source'] = self.name

            # 게시물 제목 저장
            titleXpath = "td/span/text()"
            item['title'] = createItemUseXpath(select, titleXpath, texttype="")
            if item['title'] == "공지":
                # 공지사항 필터링
                pass
            else:
                titleXpath = "td/a/text()"
                item['title'] = createItemUseXpath(select, titleXpath, texttype="")
                # print(item['title'])

                # 게시물 링크 저장
                linkXpath = "td/a/@href"
                item['link'] = createItemUseXpath(select, linkXpath, texttype=TextType.LINK).split(" ")[0]
                # print(item['link'])

                # 현재 게시판 url을 분석해서 게시판 속성 저장
                item['attribute'] = str(item['link']).split("=")[1].replace("&page","").replace("&search_target","")
                # print(item['attribute'])

                # 게시물 게시일 저장
                dateXpath = "td[@class='time']/text()"
                item['date'] = createItemUseXpath(select, dateXpath, texttype=TextType.DATE)+":00"
                # print(item['date'])

                # 게시물 조회수 저장
                hitsXpath = "td/text()"
                item['hits'] = createItemUseXpath(select, hitsXpath, texttype=TextType.INT).split(" ")[-1]
                # print(item['hits'])

                # 추천수 저장
                recommenedXpath = "td/text()"
                if select.xpath(recommenedXpath).extract()[0] == "-":
                    item['recommened'] = 0
                else:
                    item['recommened'] = createItemUseXpath(select, hitsXpath, texttype=TextType.INT).split(" ")[0]
                # print(item['recommened'])

                # 마지막 갱신일 저장 -> 현재 시간
                item['last_update'] = getCurrentTime("STR")
                # print(item['last_update'])

                # 게시물 인기도 저장
                item['pop'] = createItem_pop(item['date'], item['recommened'], item['hits'])
                # print(item['pop'])

                # 게시물 텍스트 저장
                tagName = "div"
                tagAttrs = {"id": "article_1"}
                if createItemUseBs4(item['link'], tagName, tagAttrs, encoding="utf8", texttype=TextType.TEXT) == "":
                    item['text'] = "None Text"
                else:
                    item['text'] = createItemUseBs4(item['link'], tagName, tagAttrs, encoding="utf8", texttype=TextType.TEXT)
                    # print(item['text'])

                # Item -> DB에 저장
                if filterItem(item) != None:
                    # 아이템 필터링 후 DB저장
                    yield filterItem(item)



