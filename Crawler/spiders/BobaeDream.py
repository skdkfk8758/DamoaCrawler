
"""
SeeKo 스파이더
Create : 2017.10.09

MAX_PAGE -> Damoa.spiders.Setting에 있음

"""

import scrapy

from Crawler.filterItem import *
from Crawler.items import DamoaItem
from Crawler.spiders.Setting import *
from Crawler.CreateItem import *

class GameShot(scrapy.Spider):
    name = 'bobaedream' # spider name

    baseUrl = "http://www.bobaedream.co.kr/"

    # 리퀘스트 요청
    def start_requests(self):
        for i in range(1, MAX_PAGE, 1):
            yield scrapy.Request("http://www.bobaedream.co.kr/list?code=freeb&s_cate=&maker_no=&model_no=&or_gu=10&or_se=desc&s_selday=&pagescale=30&info3=&noticeShow=&s_select=&s_key=&level_no=&vdate=&type=list&page={}".format(i))
            yield scrapy.Request("http://www.bobaedream.co.kr/list?code=battle&s_cate=&maker_no=&model_no=&or_gu=10&or_se=desc&s_selday=&pagescale=30&info3=&noticeShow=&s_select=&s_key=&level_no=&vdate=&type=list&page={}".format(i))
            yield scrapy.Request("http://www.bobaedream.co.kr/list?code=famous&s_cate=&maker_no=&model_no=&or_gu=10&or_se=desc&s_selday=&pagescale=30&info3=&noticeShow=&s_select=&s_key=&level_no=&vdate=&type=list&page={}".format(i))
            yield scrapy.Request("http://www.bobaedream.co.kr/list?code=nnews&s_cate=&maker_no=&model_no=&or_gu=10&or_se=desc&s_selday=&pagescale=30&info3=&noticeShow=&s_select=&s_key=&level_no=&vdate=&type=list&page={}".format(i))
            yield scrapy.Request("http://www.bobaedream.co.kr/list?code=politic&s_cate=&maker_no=&model_no=&or_gu=10&or_se=desc&s_selday=&pagescale=30&info3=&noticeShow=&s_select=&s_key=&level_no=&vdate=&type=list&page={}".format(i))
            yield scrapy.Request("http://www.bobaedream.co.kr/list?code=strange&s_cate=&maker_no=&model_no=&or_gu=10&or_se=desc&s_selday=&pagescale=30&info3=&noticeShow=&s_select=&s_key=&level_no=&vdate=&type=list&page={}".format(i))
            yield scrapy.Request("http://www.bobaedream.co.kr/list?code=accident&s_cate=&maker_no=&model_no=&or_gu=10&or_se=desc&s_selday=&pagescale=30&info3=&noticeShow=&s_select=&s_key=&level_no=&vdate=&type=list&page={}".format(i))
            yield scrapy.Request("http://www.bobaedream.co.kr/list?code=national&s_cate=&maker_no=&model_no=&or_gu=10&or_se=desc&s_selday=&pagescale=30&info3=&noticeShow=&s_select=&s_key=&level_no=&vdate=&type=list&page={}".format(i))
            yield scrapy.Request("http://www.bobaedream.co.kr/list?code=import&s_cate=&maker_no=&model_no=&or_gu=10&or_se=desc&s_selday=&pagescale=30&info3=&noticeShow=&s_select=&s_key=&level_no=&vdate=&type=list&page={}".format(i))
            yield scrapy.Request("http://www.bobaedream.co.kr/list?code=dica&s_cate=&maker_no=&model_no=&or_gu=10&or_se=desc&s_selday=&pagescale=30&info3=&noticeShow=&s_select=&s_key=&level_no=&vdate=&type=list&page={}".format(i))
            yield scrapy.Request("http://www.bobaedream.co.kr/list?code=special&s_cate=&maker_no=&model_no=&or_gu=10&or_se=desc&s_selday=&pagescale=30&info3=&noticeShow=&s_select=&s_key=&level_no=&vdate=&type=list&page={}".format(i))
            yield scrapy.Request("http://www.bobaedream.co.kr/list?code=girl&s_cate=&maker_no=&model_no=&or_gu=10&or_se=desc&s_selday=&pagescale=30&info3=&noticeShow=&s_select=&s_key=&level_no=&vdate=&type=list&page={}".format(i))
            yield scrapy.Request("http://www.bobaedream.co.kr/list?code=music&s_cate=&maker_no=&model_no=&or_gu=10&or_se=desc&s_selday=&pagescale=30&info3=&noticeShow=&s_select=&s_key=&level_no=&vdate=&type=list&page={}".format(i))
            yield scrapy.Request("http://www.bobaedream.co.kr/list?code=army&s_cate=&maker_no=&model_no=&or_gu=10&or_se=desc&s_selday=&pagescale=30&info3=&noticeShow=&s_select=&s_key=&level_no=&vdate=&type=list&page={}".format(i))
            yield scrapy.Request("http://www.bobaedream.co.kr/list?code=truck&s_cate=&maker_no=&model_no=&or_gu=10&or_se=desc&s_selday=&pagescale=30&info3=&noticeShow=&s_select=&s_key=&level_no=&vdate=&type=list&page={}".format(i))
            yield scrapy.Request("http://www.bobaedream.co.kr/list?code=skybr&s_cate=&maker_no=&model_no=&or_gu=10&or_se=desc&s_selday=&pagescale=30&info3=&noticeShow=&s_select=&s_key=&level_no=&vdate=&type=list&page={}".format(i))
            yield scrapy.Request("http://www.bobaedream.co.kr/list?code=vi&s_cate=&maker_no=&model_no=&or_gu=10&or_se=desc&s_selday=&pagescale=30&info3=&noticeShow=&s_select=&s_key=&level_no=&vdate=&type=list&page={}".format(i))
            yield scrapy.Request("http://www.bobaedream.co.kr/list?code=wheel&s_cate=&maker_no=&model_no=&or_gu=10&or_se=desc&s_selday=&pagescale=30&info3=&noticeShow=&s_select=&s_key=&level_no=&vdate=&type=list&page={}".format(i))

    # 사이트 파싱
    def parse(self, response):
        for select in response.xpath("//table/tbody/tr"):

            if select.xpath("td/span/text()").extract()[0] == "영자C":
                # 관리자가 작성한 게시물(공지) 거르고 크롤링
                continue
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
                item['link'] =  self.baseUrl + createItemUseXpath(select, linkXpath, texttype=TextType.LINK).split("java")[0]
                # print(item['link'])

                # 게시물 속성 저장
                attrXpath = "//div[@class='titleArea02']/h2/img/@alt"
                item['attribute'] = createItemUseXpath(select, attrXpath, texttype="")
                # print(item['attribute'])

                # 게시물 게시일 저장
                tagName = "span"
                tagAttrs =  {"class": "countGroup"}
                item['date'] = createItemUseBs4(item['link'], tagName, tagAttrs, encoding="utf8", texttype=TextType.DATE).split("|")[-1].strip()+":00"
                # print(item['date'])

                # 게시물 조회수 저장
                tagName = "span"
                tagAttrs = {"class": "countGroup"}
                item['hits'] = createItemUseBs4(item['link'], tagName, tagAttrs, encoding="utf8", texttype=TextType.INT).split("|")[0].strip()
                # print(item['hits'])

                # 추천수 OR 공감수 저장, 추천수나 공감수가 게시물에 존재하지않으면 0
                tagName = "span"
                tagAttrs = {"class": "countGroup"}
                item['hits'] = \
                item['recommened'] = createItemUseBs4(item['link'], tagName, tagAttrs, encoding="utf8", texttype=TextType.INT).split("|")[1].strip()
                # print(item['recommened'])

                # 마지막 갱신일 저장 -> 현재시간
                item['last_update'] = getCurrentTime(TextType.STRING)
                # print(item['last_update'])

                # 게시물 인기도 저장
                item['pop'] = createItem_pop(item['date'], item['recommened'], item['hits'])
                # print(item['pop'])

                # 게시물 텍스트 저장
                tagName = "div"
                tagAttrs = {"class": "bodyCont"}
                item['text'] = createItemUseBs4(item['link'], tagName, tagAttrs, encoding="utf8", texttype=TextType.TEXT)
                # print(item['text'])

                # Item -> DB에 저장
                if filterItem(item) != None:
                    # 아이템 필터링 후 DB저장
                    yield filterItem(item)



