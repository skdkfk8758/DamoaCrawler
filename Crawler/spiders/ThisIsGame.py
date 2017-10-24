
"""
This is Game Spider
Create :  2017.10.08

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
    name = 'thisisgame' # spider name

    baseUrl = "http://www.thisisgame.com"

    # 리퀘스트 요청
    def start_requests(self):
        for i in range(1, MAX_PAGE, 1):
            yield scrapy.Request("http://www.thisisgame.com/webzine/community/tboard/?board=36&page={}".format(i))
            yield scrapy.Request("http://www.thisisgame.com/webzine/community/tboard/?board=37&page={}".format(i))
            yield scrapy.Request("http://www.thisisgame.com/webzine/community/tboard/?board=38&page={}".format(i))
            yield scrapy.Request("http://www.thisisgame.com/webzine/community/tboard/?board=39&page={}".format(i))
            yield scrapy.Request("http://www.thisisgame.com/webzine/community/tboard/?board=40&page={}".format(i))
            yield scrapy.Request("http://www.thisisgame.com/webzine/community/tboard/?board=956&page={}".format(i))
            yield scrapy.Request("http://www.thisisgame.com/webzine/community/tboard/?board=32&page={}".format(i))
            yield scrapy.Request("http://www.thisisgame.com/webzine/gallery/tboard/?board=33&&category=1&page={}".format(i))
            yield scrapy.Request("http://www.thisisgame.com/webzine/gallery/tboard/?board=33&&category=2&page={}".format(i))
            yield scrapy.Request("http://www.thisisgame.com/webzine/gallery/tboard/?board=33&&category=13page={}".format(i))

    # 사이트 파싱
    def parse(self, response):
        for select in response.xpath("//table/tbody/tr"):

            if select.xpath("td/span/text()").extract()[0] == "공지":
                # 공지사항 거르고 크롤링
                pass
            else:
                item = DamoaItem() # item객체 생성

                # 게시물 출처 저장
                item['source'] = self.name

                # 게시물 제목 저장
                titleXpath = "td/a/text()"
                item['title'] = createItemUseXpath(select, titleXpath, texttype="")
                # print(item['title'])

                # 게시물 링크 저장
                linkXpath = "td/a/@href"
                item['link'] = self.baseUrl + createItemUseXpath(select, linkXpath, texttype=TextType.LINK)
                # print(item['link'])

                # 게시물 속성 저장
                attrXpath = "//div[@class='board-title-part']/h1/a/strong/text()"
                item['attribute'] = createItemUseXpath(select, attrXpath, texttype="")
                # print(item['attribute'])

                # 게시물 게시일 저장
                tagName = "span"
                tagAttrs = {"class": "info-one postdate"}
                item['date'] = createItemUseBs4(item['link'], tagName, tagAttrs, encoding="utf8", texttype=TextType.DATE)
                # print(item['date'])

                # 게시물 조회수 저장
                tagName = "span"
                tagAttrs = {"class": "info-one readcount"}
                item['hits'] = createItemUseBs4(item['link'], tagName, tagAttrs, encoding="utf8", texttype=TextType.INT)
                # print(item['hits'])

                # 추천수 OR 공감수 저장, 추천수나 공감수가 게시물에 존재하지않으면 0
                recommenedXpath = "td/text()"
                item['recommened'] = createItemUseXpath(select, recommenedXpath, texttype=TextType.INT)[-1]
                # print(item['recommened'])

                # 마지막 갱신일 저장 -> 현재시간
                item['last_update'] = getCurrentTime("str")

                # 게시물 인기도 저장
                item['pop'] = createItem_pop(item['date'], item['recommened'], item['hits'])
                # print(item['pop'])

                # 게시물 텍스트 저장
                tagName = "div"
                tagAttrs = {"class": "content board-content"}
                item['text'] = createItemUseBs4(item['link'], tagName, tagAttrs, encoding="utf8", texttype=TextType.TEXT)
                # print(postText)

                # Item -> DB에 저장
                if filterItem(item) != None:
                    # 아이템 필터링 후 DB저장
                    yield filterItem(item)



