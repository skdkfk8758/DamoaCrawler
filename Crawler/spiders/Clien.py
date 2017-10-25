
"""
Clien Spider
Create : 2017.06.14

MAX_PAGE -> DamoaCrawler.spiders.spider_Setting에 있음

2017.10.09
 - 코드정리

"""
import scrapy

from Crawler.filterItem import *
from Crawler.items import DamoaItem
from Crawler.spiders.Setting import *
from Crawler.CreateItem import *

class Clien(scrapy.Spider):
    name = 'clien' # spider name

    baseUrl = "http://www.clien.net"

    # 리퀘스트 요청
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

    # 사이트 파싱
    def parse(self, response):
        for select in response.xpath('//div[@class="item"]'):
            item = DamoaItem() # item객체 생성

            # 게시물 출처 저장
            item['source'] = self.name
            # print(type(item["source"]))

            # 게시물 제목 저장
            titleXpath = "div[@class='list-title']/a[@class='list-subject']/text()"
            item['title'] = createItemUseXpath(select, titleXpath, texttype="")
            # print(item["title"])

            # 게시물 링크 저장
            linkXpath = "div[@class='list-title']/a/@href"
            item['link'] = self.baseUrl + createItemUseXpath(select, linkXpath, texttype=TextType.LINK)
            # print(item["link"])

            # 게시물 속성 저장
            tagName = "li"
            tagAttr = {"class": "board-title"}
            item['attribute'] = createItemUseBs4(item['link'], tagName, tagAttr, encoding="CP949",texttype="")
            # print(type(item["attribute"]))

            # 게시물 게시일 저장
            dateXpath = "div/span[@class='time']/span[@class='timestamp']/text()"
            item['date'] = createItemUseXpath(select, dateXpath,texttype="")
            # print(item["date"])

            # 게시물 조회수 저장
            tagName = "span"
            tagAttr = {"class" : "view-count"}
            item['hits'] = createItemUseBs4(item['link'], tagName, tagAttr, encoding="CP949",texttype=TextType.INT)
            # print(type(item["hits"]))

            # 게시물 추천수 OR 공감수 저장
            tagName = "div"
            tagAttr = {"class": "title-symph"}
            item['recommened'] = createItemUseBs4(item['link'], tagName, tagAttr, encoding="CP949",texttype=TextType.INT)
            # print(type(item["recommened"]))

            # 마지막 갱신일 저장 -> 현재시간
            item['last_update'] = getCurrentTime(TextType.STRING)
            # print(type(item["last_update"]))

            # 게시물 인기도 저장
            item['pop'] = createItem_pop(item['date'], item['recommened'], item['hits'])
            # print(item['pop'])

            # 게시물 텍스트 저장
            tagName = "div"
            tagAttrs = {"class": "post-article fr-view"}
            item['text'] = createItemUseBs4(item['link'], tagName, tagAttrs, encoding="CP949", texttype=TextType.TEXT)

            # Item -> DB에 저장
            if filterItem(item) != None:
                # 아이템 필터링 후 DB저장
                yield filterItem(item)


