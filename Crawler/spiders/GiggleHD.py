
"""
기글하드웨어 Spider
Create :  2017.10.21

MAX_PAGE -> Damoa.spiders.Setting에 있음

"""

import scrapy

from Crawler.filterItem import *
from Crawler.items import DamoaItem
from Crawler.spiders.Setting import *
from Crawler.CreateItem import *

class Spider(scrapy.Spider):
    name = 'giggle' # spider name

    baseUrl = "https://gigglehd.com/gg/"

    # 각 게시판별로 리퀘스트 요청
    def start_requests(self):
        for i in range(1, MAX_PAGE, 1):
            yield scrapy.Request("https://gigglehd.com/gg/index.php?mid=bbs&category=13759&page={}".format(i))
            yield scrapy.Request("https://gigglehd.com/gg/index.php?mid=bbs&category=207062&page={}".format(i))
            yield scrapy.Request("https://gigglehd.com/gg/index.php?mid=bbs&category=13770&page={}".format(i))
            yield scrapy.Request("https://gigglehd.com/gg/index.php?mid=bbs&category=856796&page={}".format(i))
            yield scrapy.Request("https://gigglehd.com/gg/index.php?mid=bbs&category=14058&page={}".format(i))

    # 리스폰스 받아서 사이트 파싱
    def parse(self, response):
        # print(response.xpath("//table/tbody"))
        for select in response.xpath("//table/tbody/tr"):
            item = DamoaItem() # item객체 생성

            # 게시물 출처 저장
            item['source'] = self.name

            # 게시물 제목 저장
            if createItemUseXpath(select, "td[@class='no']/strong/text()", texttype="")== "공지":
                # 공지사항 패스
                continue
            else:
                titleXpath = "td[@class='title']/a[@class='hx']/text()"
                item['title'] = createItemUseXpath(select, titleXpath, texttype="")

                # 게시물 링크 저장
                linkXpath = "td[@class='title']/a/@href"
                item['link'] = createItemUseXpath(select, linkXpath, texttype=TextType.LINK)

                # 현재 게시판 url을 분석해서 게시판 속성 저장
                attrXpath = "td[@class='cate']/span/text()"
                item['attribute'] = createItemUseXpath(select, attrXpath, texttype="")

                # 게시물 게시일 저장
                tagName = "span"
                tagAttr = {"class": "date m_no"}
                item['date'] = "".join(createItemUseBs4(item['link'], tagName, tagAttr, texttype=TextType.DATE, encoding="utf8")) + ":00"

                # 게시물 조회수 저장
                tagName = "div"
                tagAttrs = {"class": "side fr"}
                item['hits'] = createItemUseBs4(item['link'], tagName, tagAttrs, texttype=TextType.INT, encoding="utf8").split(" ")[2]

                # 추천수 저장
                # recommenedXpath = "td[@class='vote']/text()"
                # if select.xpath(recommenedXpath).extract()[0] == "-":
                #     item['recommened'] = 0
                # else:
                #     item['recommened'] = createItemUseXpath(select,recommenedXpath,texttype=TextType.INT)
                item['recommened'] = 0

                # 마지막 갱신일 저장 -> 현재 시간
                item['last_update'] = getCurrentTime(TextType.STRING)

                # 게시물 인기도 저장
                item['pop'] = createItem_pop(item['date'], item['recommened'], item['hits'])

                # 게시물 텍스트 저장
                tagName = "div"
                tagAttrs = {"class": "rd_body clear"}
                if createItemUseBs4(item['link'], tagName, tagAttrs, encoding="utf8", texttype=TextType.TEXT) == "":
                    item['text'] = "None Text"
                else:
                    item['text'] = createItemUseBs4(item['link'], tagName, tagAttrs, encoding="utf8", texttype=TextType.TEXT)

                # Item -> DB에 저장
                if filterItem(item) != None:
                    # 아이템 필터링 후 DB저장
                    yield filterItem(item)



