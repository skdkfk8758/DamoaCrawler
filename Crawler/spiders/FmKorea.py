
"""
FM Korea Spider
Create :  2017.10.23

MAX_PAGE -> Damoa.spiders.Setting에 있음

"""

import scrapy

from Crawler.filterItem import *
from Crawler.items import DamoaItem
from Crawler.spiders.Setting import *
from Crawler.CreateItem import *

class Spider(scrapy.Spider):
    name = 'fmkorea' # spider name

    baseUrl = "http://www.fmkorea.com/"

    # 각 게시판별로 리퀘스트 요청
    def start_requests(self):
        for i in range(1, MAX_PAGE, 1):
            yield scrapy.Request("http://www.fmkorea.com/index.php?mid=humor&page={}".format(i))
            yield scrapy.Request("http://www.fmkorea.com/index.php?mid=mystery&page={}".format(i))
            yield scrapy.Request("http://www.fmkorea.com/index.php?mid=news&page={}".format(i))
            yield scrapy.Request("http://www.fmkorea.com/index.php?mid=free&page={}".format(i))
            yield scrapy.Request("http://www.fmkorea.com/index.php?mid=sreckovic&page={}".format(i))
            yield scrapy.Request("http://www.fmkorea.com/index.php?mid=love&page={}".format(i))
            yield scrapy.Request("http://www.fmkorea.com/index.php?mid=fashion&page={}".format(i))
            yield scrapy.Request("http://www.fmkorea.com/index.php?mid=gomin&page={}".format(i))
            yield scrapy.Request("http://www.fmkorea.com/index.php?mid=job&page={}".format(i))
            yield scrapy.Request("http://www.fmkorea.com/index.php?mid=car&page={}".format(i))
            yield scrapy.Request("http://www.fmkorea.com/index.php?mid=study&page={}".format(i))
            yield scrapy.Request("http://www.fmkorea.com/index.php?mid=baseball&page={}".format(i))
            yield scrapy.Request("http://www.fmkorea.com/index.php?mid=other_sports&page={}".format(i))
            yield scrapy.Request("http://www.fmkorea.com/index.php?mid=basketball&page={}".format(i))
            yield scrapy.Request("http://www.fmkorea.com/index.php?mid=stock&page={}".format(i))
            yield scrapy.Request("http://www.fmkorea.com/index.php?mid=fm17free&page={}".format(i))
            yield scrapy.Request("http://www.fmkorea.com/index.php?mid=fm17tips&page={}".format(i))
            yield scrapy.Request("http://www.fmkorea.com/index.php?mid=fm17tqna&page={}".format(i))
            yield scrapy.Request("http://www.fmkorea.com/index.php?mid=game_fifa&page={}".format(i))
            yield scrapy.Request("http://www.fmkorea.com/index.php?mid=fifa_series&page={}".format(i))
            yield scrapy.Request("http://www.fmkorea.com/index.php?mid=lol&page={}".format(i))
            yield scrapy.Request("http://www.fmkorea.com/index.php?mid=battlegrounds&page={}".format(i))
            yield scrapy.Request("http://www.fmkorea.com/index.php?mid=overwatch&page={}".format(i))
            yield scrapy.Request("http://www.fmkorea.com/index.php?mid=mgame&page={}".format(i))
            yield scrapy.Request("http://www.fmkorea.com/index.php?mid=gf&page={}".format(i))
            yield scrapy.Request("http://www.fmkorea.com/index.php?mid=Seven&page={}".format(i))
            yield scrapy.Request("http://www.fmkorea.com/index.php?mid=gallery_foods&page={}".format(i))
            yield scrapy.Request("http://www.fmkorea.com/index.php?mid=stock&page={}".format(i))
            yield scrapy.Request("http://www.fmkorea.com/index.php?mid=fm17players&page={}".format(i))

    # 리스폰스 받아서 사이트 파싱
    def parse(self, response):
        # print(response.xpath("//table/tbody"))
        for select in response.xpath("//table/tbody/tr"):
            item = DamoaItem() # item객체 생성

            # 게시물 출처 저장
            item['source'] = self.name

            # 게시물 제목 저장
            if createItemUseXpath(select, "td[@class='cate']/a/text()", texttype="") == "공지" \
                    or (createItemUseXpath(select, "td[@class='title']/a/text()", texttype="")).split(" ")[0] == "":
                # 공지사항 패스
                continue
            else:
                titleXpath = "td[@class='title']/a/text()"
                item['title'] = createItemUseXpath(select, titleXpath, texttype="")
                # print(item['title'])

                # 게시물 링크 저장
                linkXpath = "td[@class='title']/a/@href"
                item['link'] = (self.baseUrl + createItemUseXpath(select, linkXpath, texttype=TextType.LINK)).split(' ')[0]
                print(item['link'])

                # 현재 게시판 url을 분석해서 게시판 속성 저장
                attrXpath = "td[@class='cate']/span/a/text()"
                item['attribute'] = createItemUseXpath(select, attrXpath, texttype="")
                # print(item['attribute'])

                # 게시물 게시일 저장
                tagName = "span"
                tagAttr = {"class": "date"}
                item['date'] = "".join(createItemUseBs4(item['link'], tagName, tagAttr, texttype=TextType.DATE, encoding="utf8")) + ":00"
                # print(item['date'])

                # 게시물 조회수 저장
                # tagName = "div"
                # tagAttrs = {"class": "side fr"}
                # item['hits'] = createItemUseBs4(item['link'], tagName, tagAttrs, texttype=TextType.INT, encoding="utf8").split("조회")[1].split(" ")[0].replace("회","")
                hitsXpath = "td[@class='m_no']/text()"
                item['hits'] = createItemUseXpath(select, hitsXpath, texttype=TextType.INT)
                # print(item['hits'])

                # 추천수 저장
                tagName = "div"
                tagAttrs = {"class": "side fr"}
                item['recommened'] = createItemUseBs4(item['link'], tagName, tagAttrs, encoding="utf8", texttype=TextType.INT).split(" ")[-3]
                # recommenedXpath = "td[@class='m_no m_no_voted']/text()"
                # if select.xpath(recommenedXpath) == "":
                #     item['recommened'] = 0
                # else:
                #     item['recommened'] = createItemUseXpath(select, recommenedXpath, texttype=TextType.INT)
                # print(item['recommened'])

                # 마지막 갱신일 저장 -> 현재 시간
                item['last_update'] = getCurrentTime(TextType.STRING)

                # 게시물 인기도 저장
                item['pop'] = createItem_pop(item['date'], item['recommened'], item['hits'])
                # print(item['pop'])

                # 게시물 텍스트 저장
                tagName = "div"
                tagAttrs = {"class": "xe_content"}
                if createItemUseBs4(item['link'], tagName, tagAttrs, encoding="utf8", texttype=TextType.TEXT) == "":
                    item['text'] = "None Text"
                else:
                    item['text'] = createItemUseBs4(item['link'], tagName, tagAttrs, encoding="utf8", texttype=TextType.TEXT)
                # print(item['text'])


            # Item -> DB에 저장
            if filterItem(item) != None:
                # 아이템 필터링 후 DB저장
                yield filterItem(item)



