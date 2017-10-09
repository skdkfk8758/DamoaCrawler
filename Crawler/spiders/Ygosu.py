
"""
ygosu Spider
Create :  2017.10.09

MAX_PAGE -> Damoa.spiders.Setting에 있음

"""

import scrapy

from Crawler.filterItem import *
from Crawler.items import DamoaItem
from Crawler.spiders.Setting import *
from Crawler.CreateItem import *

class Ygosu(scrapy.Spider):
    name = 'ygosu' # spider name

    baseUrl = "http://www.ygosu.com"

    # 각 게시판별로 리퀘스트 요청
    def start_requests(self):
        for i in range(1, 2, 1):
            yield scrapy.Request("http://www.ygosu.com/community/yeobgi/?page={}".format(i))
            # yield scrapy.Request("http://www.ygosu.com/community/free/?page={}".format(i))
            # yield scrapy.Request("http://www.ygosu.com/community/issue/?page={}".format(i))
            # yield scrapy.Request("http://www.ygosu.com/community/love/?page={}".format(i))
            # yield scrapy.Request("http://www.ygosu.com/community/study/?page={}".format(i))
            # yield scrapy.Request("http://www.ygosu.com/community/secret/?page={}".format(i))
            # yield scrapy.Request("http://www.ygosu.com/community/horror/?page={}".format(i))
            # yield scrapy.Request("http://www.ygosu.com/community/tip/?page={}".format(i))
            # yield scrapy.Request("http://www.ygosu.com/community/jobs/?page={}".format(i))
            # yield scrapy.Request("http://www.ygosu.com/community/soccer/?page={}".format(i))
            # yield scrapy.Request("http://www.ygosu.com/community/baseball/?page={}".format(i))
            # yield scrapy.Request("http://www.ygosu.com/community/basketball/?page={}".format(i))
            # yield scrapy.Request("http://www.ygosu.com/community/sports/?page={}".format(i))
            # yield scrapy.Request("http://www.ygosu.com/community/computer/?page={}".format(i))
            # yield scrapy.Request("http://www.ygosu.com/community/phone/?page={}".format(i))
            # yield scrapy.Request("http://www.ygosu.com/community/bicycle/?page={}".format(i))
            # yield scrapy.Request("http://www.ygosu.com/community/animation/?page={}".format(i))
            # yield scrapy.Request("http://www.ygosu.com/community/stars/?page={}".format(i))
            # yield scrapy.Request("http://www.ygosu.com/community/movie/?page={}".format(i))
            # yield scrapy.Request("http://www.ygosu.com/community/music/?page={}".format(i))
            # yield scrapy.Request("http://www.ygosu.com/community/food/?page={}".format(i))
            # yield scrapy.Request("http://www.ygosu.com/community/mil/?page={}".format(i))
            # yield scrapy.Request("http://www.ygosu.com/community/fashion/?page={}".format(i))
            # yield scrapy.Request("http://www.ygosu.com/community/hiphop/?page={}".format(i))
            # yield scrapy.Request("http://www.ygosu.com/community/animal/?page={}".format(i))
            # yield scrapy.Request("http://www.ygosu.com/community/stock/?page={}".format(i))
            # yield scrapy.Request("http://www.ygosu.com/community/art/?page={}".format(i))
            # yield scrapy.Request("http://www.ygosu.com/community/travel/?page={}".format(i))
            # yield scrapy.Request("http://www.ygosu.com/community/game_etc/?page={}".format(i))
            # yield scrapy.Request("http://www.ygosu.com/community/lo_legend/?page={}".format(i))
            # yield scrapy.Request("http://www.ygosu.com/community/st/?page={}".format(i))
            # yield scrapy.Request("http://www.ygosu.com/community/star2_st/?page={}".format(i))
            # yield scrapy.Request("http://www.ygosu.com/community/over/?page={}".format(i))
            # yield scrapy.Request("http://www.ygosu.com/community/fm/?page={}".format(i))
            # yield scrapy.Request("http://www.ygosu.com/community/ffonline2/?page={}".format(i))
            # yield scrapy.Request("http://www.ygosu.com/community/baram/?page={}".format(i))
            # yield scrapy.Request("http://www.ygosu.com/community/black/?page={}".format(i))
            # yield scrapy.Request("http://www.ygosu.com/community/hearthstone/?page={}".format(i))
            # yield scrapy.Request("http://www.ygosu.com/community/diablo/?page={}".format(i))
            # yield scrapy.Request("http://www.ygosu.com/community/df/?page={}".format(i))
            # yield scrapy.Request("http://www.ygosu.com/community/maple/?page={}".format(i))
            # yield scrapy.Request("http://www.ygosu.com/community/pubg/?page={}".format(i))

    # 리스폰스 받아서 사이트 파싱
    def parse(self, response):
        for select in response.xpath("//table/tbody/tr"):
            item = DamoaItem() # item객체 생성

            # 게시물 출처 저장
            item['source'] = self.name

            # 게시물 제목 저장
            titleXpath = "td[@class='tit']/a/text()"
            item['title'] = createItemUseXpath(select, titleXpath, texttype="")
            if item['title'] == "":
                # td태그안에 빈 텍스트가있어서 오류가 발생 -> 빈 텍스트는 패스
                pass
            else:
                # 게시물 링크 저장
                linkXpath = "td/a/@href"
                item['link'] = self.baseUrl + createItemUseXpath(select, linkXpath, texttype="link")
                print(item['link'])

                # 현재 게시판 url을 분석해서 게시판 속성 저장
                item['attribute'] = str(response).split('/')[4]
                # print(item['attribute'])

                # 게시물 게시일 저장
                tagName = "div"
                tagAttr = {"class": "date"}
                item['date'] = createItemUseBs4(item['link'], tagName, tagAttr, texttype="date", encoding="CP949")
                print(item['date'])

                # 게시물 조회수 저장
                tagName = "div"
                tagAttrs = {"class": "date"}
                item['hits'] = createItemUseBs4(item['link'], tagName, tagAttrs, encoding="utf8", texttype="hits")
                print(item['hits'])

                # 추천수 저장
                recommenedXpath = "td[@class='vote']/text()"
                if select.xpath(recommenedXpath).extract()[0] == "-":
                    item['recommened'] = 0
                else:
                    item['recommened'] = createItemUseXpath(select,recommenedXpath,texttype="")
                # print(item['recommened'])

                # 마지막 갱신일 저장 -> 현재 시간
                item['last_update'] = getCurrentTime()

                # 게시물 인기도 저장
                item['pop'] = createItem_pop(item['date'], item['recommened'], item['hits'])
                # print(item['pop'])

                # 게시물 텍스트 저장
                tagName = "div"
                tagAttrs = {"class": "container"}
                if createItemUseBs4(item['link'], tagName, tagAttrs, encoding="utf8", texttype="") == "":
                    item['text'] = "None Text"
                else:
                    item['text'] = createItemUseBs4(item['link'], tagName, tagAttrs, encoding="utf8", texttype="")
                    # print(item['text'])

                # Item -> DB에 저장
                if filterItem(item) != None:
                    # 아이템 필터링 후 DB저장
                    yield filterItem(item)



