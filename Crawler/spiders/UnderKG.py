
"""
UnderKG Spider
Create :  2017.10.19

MAX_PAGE -> Damoa.spiders.Setting에 있음

"""

import scrapy

from Crawler.filterItem import *
from Crawler.items import DamoaItem
from Crawler.spiders.Setting import *
from Crawler.CreateItem import *
from Crawler.TextTypeEnum import *

class Spider(scrapy.Spider):
    name = 'underkg' # spider name

    baseUrl = "http://underkg.co.kr/"

    # 리퀘스트 요청
    def start_requests(self):
        for i in range(1, MAX_PAGE, 1):
            yield scrapy.Request("http://underkg.co.kr/index.php?mid=freeboard&page={}".format(i))
            yield scrapy.Request("http://underkg.co.kr/index.php?mid=QnA&page={}".format(i))
            yield scrapy.Request("http://underkg.co.kr/index.php?mid=user_review&page={}".format(i))

    # 사이트 파싱
    def parse(self, response):
        # print(response.xpath("//table/tbody/tr"))
        for select in response.xpath("//table/tbody/tr"):

            item = DamoaItem() # item객체 생성

            # 게시물 출처 저장
            item['source'] = self.name

            # 게시물 제목 저장
            titleXpath = "td[@class='notice']/text()"
            item['title'] = createItemUseXpath(select, titleXpath, texttype="")
            # print(item['title'])
            if item['title'] == "공지":
                pass
            else:
                titleXpath = "td[@class='title']/a/text()"
                item['title'] = createItemUseXpath(select, titleXpath, texttype="")
                # print(item['title'])

                # 게시물 링크 저장
                linkXpath = "td/a/@href"
                item['link'] = createItemUseXpath(select, linkXpath, texttype=TextType.LINK)
                # print(item['link'])

                # 게시물 속성 저장
                attrXpath = "//div/div/div/div/div/text()"
                item['attribute'] = createItemUseXpath(select, attrXpath, texttype=TextType.TEXT).strip()
                # print(item['attribute'])

                # 게시물 게시일 저장
                dateXpath = "td[@class='time']/text()"
                item['date'] = createItemUseXpath(select, dateXpath, texttype=TextType.DATE)+" 00:00:00"
                # print(item['date'])

                # 게시물 조회수 저장
                hitsXpath = "td[@class='readNum']/text()"
                item['hits'] = createItemUseXpath(select, hitsXpath, texttype=TextType.INT)
                # print(item['hits'])

                # 추천수 OR 공감수 저장, 추천수나 공감수가 게시물에 존재하지않으면 0
                recommenedXpath = "td[@class='voteNum']/text()"
                item['recommened'] = createItemUseXpath(select, recommenedXpath, texttype=TextType.INT)
                # print(item['recommened'])

                # 마지막 갱신일 저장 -> 현재시간
                item['last_update'] = getCurrentTime(TextType.STRING)

                # 게시물 인기도 저장
                item['pop'] = createItem_pop(item['date'], item['recommened'], item['hits'])
                # print(item['pop'])

                # 게시물 텍스트 저장
                tagName = "div"
                tagAttrs = {"class": "xe_content"}
                item['text'] = createItemUseBs4(item['link'], tagName, tagAttrs, encoding="utf8", texttype=TextType.INT)
                # print(item['text'])

                # Item -> DB에 저장
                if filterItem(item) != None:
                    # 아이템 필터링 후 DB저장
                    yield filterItem(item)



