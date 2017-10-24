
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

    # 리퀘스트 요청
    def start_requests(self): 
        for i in range(1, MAX_PAGE, 1):
            yield scrapy.Request("http://www.gameshot.net/talk/?&bbs=free&sby=title&skey=&pg={}".format(i))
            yield scrapy.Request("http://www.gameshot.net/talk/?&bbs=gamenews&sby=title&skey=&pg={}".format(i))
            yield scrapy.Request("http://www.gameshot.net/talk/?&bbs=ip_shop&sby=title&skey=&pg={}".format(i))

    # 사이트 파싱
    def parse(self, response):
        for select in response.xpath("//table/tbody/tr"):

            if select.xpath("td/text()").extract()[0] == "관리자":
                # 관리자가 작성한 게시물(공지) 거르고 크롤링
                pass
            else:
                item = DamoaItem() # item객체 생성

                # 게시물 출처 저장
                item['source'] = self.name

                # 게시물 제목 저장
                titleXpath = "td/p/a/strong/text()"
                item['title'] = createItemUseXpath(select, titleXpath, texttype="")
                # print(item['title'])

                # 게시물 링크 저장
                linkXpath = "td/p/a/@href"
                item['link'] =  self.baseUrl + createItemUseXpath(select, linkXpath, texttype=TextType.LINK)
                # print(item['link'])

                # 게시물 속성 저장
                attrXpath = "//li[@class='active']/text()"
                item['attribute'] = createItemUseXpath(select, attrXpath, texttype="")
                # print(item['attribute'])

                # 게시물 게시일 저장
                tagName = "p"
                tagAttrs =  {"class": "f12 a0a0a0"}
                item['date'] = createItemUseBs4(item['link'], tagName, tagAttrs, encoding="CP949", texttype=TextType.DATE)
                # print(item['date'])

                # 게시물 조회수 저장
                hitsXpath = "td/abbr/text()"
                item['hits'] = createItemUseXpath(select, hitsXpath, texttype=TextType.INT)
                # print(item['hits'])

                # 추천수 OR 공감수 저장, 추천수나 공감수가 게시물에 존재하지않으면 0
                item['recommened'] = 0

                # 마지막 갱신일 저장 -> 현재시간
                item['last_update'] = getCurrentTime(TextType.STRING)
                # print(item['last_update'])

                # 게시물 인기도 저장
                item['pop'] = createItem_pop(item['date'], item['recommened'], item['hits'])
                # print(item['pop'])

                # 게시물 텍스트 저장
                tagName = "div"
                tagAttrs = {"id": "content"}
                item['text'] = createItemUseBs4(item['link'], tagName, tagAttrs, encoding="CP949", texttype=TextType.TEXT)
                # print(item['text'])

                # Item -> DB에 저장
                if filterItem(item) != None:
                    # 아이템 필터링 후 DB저장
                    yield filterItem(item)



