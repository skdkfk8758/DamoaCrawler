
"""
드라마미팅 Spider
Create :  2017.10.09

MAX_PAGE -> Damoa.spiders.Setting에 있음

"""

import scrapy

from Crawler.filterItem import *
from Crawler.items import DamoaItem
from Crawler.spiders.Setting import *
from Crawler.CreateItem import *

class DramaMeeting(scrapy.Spider):
    name = 'dramameeting' # spider name

    baseUrl = "http://www.dramameeting.com/"

    # 각 게시판별로 리퀘스트 요청
    def start_requests(self):
        for i in range(1, MAX_PAGE, 1):
            yield scrapy.Request("http://www.dramameeting.com/index.php?mid=entertainment&page={}".format(i))
            yield scrapy.Request("http://www.dramameeting.com/index.php?mid=broadcast&page={}".format(i))
            yield scrapy.Request("http://www.dramameeting.com/index.php?mid=photo&page={}".format(i))
            yield scrapy.Request("http://www.dramameeting.com/index.php?mid=music&page={}".format(i))
            yield scrapy.Request("http://www.dramameeting.com/index.php?mid=drama&page={}".format(i))
            yield scrapy.Request("http://www.dramameeting.com/index.php?mid=review&page={}".format(i))
            yield scrapy.Request("http://www.dramameeting.com/index.php?mid=humor&page={}".format(i))
            yield scrapy.Request("http://www.dramameeting.com/index.php?mid=humor&page={}".format(i))
            yield scrapy.Request("http://www.dramameeting.com/index.php?mid=love&page={}".format(i))
            yield scrapy.Request("http://www.dramameeting.com/index.php?mid=fashion&page={}".format(i))
            yield scrapy.Request("http://www.dramameeting.com/index.php?mid=mystery&page={}".format(i))

    # 리스폰스 받아서 사이트 파싱
    def parse(self, response):
        for select in response.xpath("//table/tbody/tr"):
            item = DamoaItem() # item객체 생성

            # 게시물 출처 저장
            item['source'] = self.name

            # 게시물 제목 저장
            titleXpath = "td[@class='no']/strong/text()"
            item['title'] = createItemUseXpath(select, titleXpath, texttype="")
            # print(item['title'])
            if item['title'] != "":
                # 공지사항 필터링
                # print(item['title'])
                pass
            else:
                titleXpath = "td[@class='title']/a/text()"
                item['title'] = createItemUseXpath(select, titleXpath, texttype="")
                # print(item['title'])

                # 게시물 링크 저장
                linkXpath = "td[@class='title']/a/@href"
                item['link'] = createItemUseXpath(select, linkXpath, texttype=TextType.LINK).split(" ")[0]
                # print(item['link'])

                # 현재 게시판 url을 분석해서 게시판 속성 저장
                item['attribute'] = str(item['link']).split("/")[3].split("=")[1].replace("&page","")
                # print(item['attribute'])

                # 게시물 게시일 저장
                dateXpath = "td[@class='time']/text()"
                item['date'] = createItemUseXpath(select, dateXpath, texttype=TextType.DATE)+" 00:00:00"
                # print(item['date'])

                # 게시물 조회수 저장
                # hitsXpath = "td/text()"
                item['hits'] = 0
                # print(item['hits'])

                # 추천수 저장
                tagName = "div"
                tagAttrs = {"class":"side fr"}
                item['recommened'] = createItemUseBs4(item['link'], tagName, tagAttrs, encoding="utf8", texttype=TextType.INT).split(" ")[3]
                # print(item['recommened'])

                # 마지막 갱신일 저장 -> 현재 시간
                item['last_update'] = getCurrentTime(TextType.STRING)
                # print(item['last_update'])

                # 게시물 인기도 저장
                item['pop'] = createItem_pop(item['date'], item['recommened'], item['hits'])
                # print(item['pop'])

                # 게시물 텍스트 저장
                tagName = "div"
                tagAttrs = {"class": "rd_body clear"}
                if createItemUseBs4(item['link'], tagName, tagAttrs, encoding="utf8", texttype=TextType.TEXT) == "":
                    item['text'] = "None Text"
                else:
                    item['text'] = createItemUseBs4(item['link'], tagName, tagAttrs, encoding="utf8", texttype=TextType.TEXT)
                    # print(item['text'])

                # Item -> DB에 저장
                if filterItem(item) != None:
                    # 아이템 필터링 후 DB저장
                    yield filterItem(item)



