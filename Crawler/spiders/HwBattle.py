
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

    # baseUrl = "http://www.hwbattle.com/"

    # 각 게시판별로 리퀘스트 요청
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

    # 리스폰스 받아서 사이트 파싱
    def parse(self, response):
        # print(response.xpath("//table/tbody"))
        for select in response.xpath("//table/tbody/tr"):
            item = DamoaItem() # item객체 생성

            # 게시물 출처 저장
            item['source'] = self.name

            # 게시물 제목 저장
            if createItemUseXpath(select, "td[@class='td_num']/strong/text()", texttype="")== "공지":
                # 공지사항 패스
                continue
            else:
                titleXpath = "td[@class='td_subject']/a/text()"
                item['title'] = createItemUseXpath(select, titleXpath, texttype="")
                # print(item['title'])

                # 게시물 링크 저장
                linkXpath = "td[@class='td_subject']/a/@href"
                item['link'] = createItemUseXpath(select, linkXpath, texttype=TextType.LINK).strip()
                # print(item['link'])

                # 현재 게시판 url을 분석해서 게시판 속성 저장
                attrXpath = "td[@class='td_subject']/a[@class='bo_cate_link']/text()"
                item['attribute'] = createItemUseXpath(select, attrXpath, texttype="")
                # print(item['attribute'])

                # 게시물 게시일 저장
                tagName = "section"
                tagAttr = {"id": "bo_v_info"}
                item['date'] = "20"+"".join(createItemUseBs4(item['link'], tagName, tagAttr, texttype=TextType.DATE, encoding="utf8")).split("조회")[0].split("작성")[2].strip() + ":00"
                # print(item['date'])

                # 게시물 조회수 저장
                tagName = "section"
                tagAttrs = {"id": "bo_v_info"}
                item['hits'] = createItemUseBs4(item['link'], tagName, tagAttrs, texttype=TextType.INT, encoding="utf8").split("조회")[1].split(" ")[0].replace("회","")
                # print(item['hits'])

                # 추천수 저장
                # recommenedXpath = "td[@class='td_vote']/div[@class='list_good2']/b/text()"
                # if select.xpath(recommenedXpath).extract()[0] == "-":
                #     item['recommened'] = 0
                # else:
                #     item['recommened'] = createItemUseXpath(select,recommenedXpath,texttype=TextType.INT)
                item['recommened'] = 0
                # print(item['recommened'])

                # 마지막 갱신일 저장 -> 현재 시간
                item['last_update'] = getCurrentTime(TextType.STRING)

                # 게시물 인기도 저장
                item['pop'] = createItem_pop(item['date'], item['recommened'], item['hits'])
                # print(item['pop'])

                # 게시물 텍스트 저장
                tagName = "div"
                tagAttrs = {"id": "bo_v_con"}
                if createItemUseBs4(item['link'], tagName, tagAttrs, encoding="utf8", texttype=TextType.TEXT) == "":
                    item['text'] = "None Text"
                else:
                    item['text'] = createItemUseBs4(item['link'], tagName, tagAttrs, encoding="utf8", texttype=TextType.TEXT)
                # print(item['text'])

            # Item -> DB에 저장
            if filterItem(item) != None:
                # 아이템 필터링 후 DB저장
                yield filterItem(item)



