
"""
82cook Spider
Create :  2017.10.19

MAX_PAGE -> Damoa.spiders.Setting에 있음

"""

import scrapy

from Crawler.filterItem import *
from Crawler.items import DamoaItem
from Crawler.spiders.Setting import *
from Crawler.CreateItem import *

class _82Cook(scrapy.Spider):
    name = '82cook' # spider name

    baseUrl = "http://www.82cook.com/entiz/"

    # 리퀘스트 요청
    def start_requests(self):
        for i in range(1, MAX_PAGE, 1):
            yield scrapy.Request("http://www.82cook.com/entiz/enti.php?bn=1&page={}".format(i))
            yield scrapy.Request("http://www.82cook.com/entiz/enti.php?bn=2&page={}".format(i))
            yield scrapy.Request("http://www.82cook.com/entiz/enti.php?bn=3&page={}".format(i))
            yield scrapy.Request("http://www.82cook.com/entiz/enti.php?bn=31&page={}".format(i))
            yield scrapy.Request("http://www.82cook.com/entiz/enti.php?bn=6&page={}".format(i))
            yield scrapy.Request("http://www.82cook.com/entiz/enti.php?bn=7&page={}".format(i))
            yield scrapy.Request("http://www.82cook.com/entiz/enti.php?bn=8&page={}".format(i))
            yield scrapy.Request("http://www.82cook.com/entiz/enti.php?bn=9&page={}".format(i))
            yield scrapy.Request("http://www.82cook.com/entiz/enti.php?bn=11&page={}".format(i))
            yield scrapy.Request("http://www.82cook.com/entiz/enti.php?bn=12&page={}".format(i))
            yield scrapy.Request("http://www.82cook.com/entiz/enti.php?bn=13&page={}".format(i))
            yield scrapy.Request("http://www.82cook.com/entiz/enti.php?bn=14&page={}".format(i))
            yield scrapy.Request("http://www.82cook.com/entiz/enti.php?bn=15&page={}".format(i))
            yield scrapy.Request("http://www.82cook.com/entiz/enti.php?bn=16&page={}".format(i))
            yield scrapy.Request("http://www.82cook.com/entiz/enti.php?bn=17&page={}".format(i))


    # 사이트 파싱
    def parse(self, response):
        # print(response.xpath("//table/tbody"))
        for select in response.xpath("//table/tbody/tr"):

            item = DamoaItem() # item객체 생성

            # 게시물 출처 저장
            item['source'] = self.name

            # 게시물 제목 저장
            titleXpath = "td/a/b/text()"
            item['title'] = createItemUseXpath(select, titleXpath, texttype="")
            if item['title'] != "":
                pass
            else:
                titleXpath = "td[@class='title']/a/text()"
                item['title'] = createItemUseXpath(select, titleXpath, texttype="")
                # print(item['title'])

                # 게시물 링크 저장
                linkXpath = "td/a/@href"
                item['link'] = self.baseUrl + createItemUseXpath(select, linkXpath, texttype="link")
                # print(item['link'])

                # 게시물 속성 저장
                attrXpath = "//div/div/div/h1/text()"
                item['attribute'] = createItemUseXpath(select, attrXpath, texttype="text")
                # print(item['attribute'])

                # 게시물 게시일 저장
                tagName = "div"
                tagAttrs = {"class": "readRight"}
                item['date'] = createItemUseBs4(item['link'], tagName, tagAttrs, encoding="utf8", texttype="date")
                # print(item['date'])

                # 게시물 조회수 저장
                hitsXpath = "td[@class='numbers']/text()"
                item['hits'] = createItemUseXpath(select, hitsXpath, texttype="hits").split(" ")[0]
                # print(item['hits'])

                # 추천수 OR 공감수 저장, 추천수나 공감수가 게시물에 존재하지않으면 0
                recommenedXpath = "td[@class='numbers']/text()"
                item['recommened'] = createItemUseXpath(select, recommenedXpath, texttype="hits").split(" ")[1]
                # print(item['recommened'])

                # 마지막 갱신일 저장 -> 현재시간
                item['last_update'] = getCurrentTime("str")

                # 게시물 인기도 저장
                item['pop'] = createItem_pop(item['date'], item['recommened'], item['hits'])
                # print(item['pop'])

                # 게시물 텍스트 저장
                tagName = "div"
                tagAttrs = {"id": "articleBody"}
                item['text'] = createItemUseBs4(item['link'], tagName, tagAttrs, encoding="utf8", texttype="text")
                # print(item['text'])

                # Item -> DB에 저장
                if filterItem(item) != None:
                    # 아이템 필터링 후 DB저장
                    yield filterItem(item)



