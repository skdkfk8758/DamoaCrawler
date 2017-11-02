
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

class Spider(scrapy.Spider):
    name = 'bobaedream' # spider name

    baseUrl = "http://www.bobaedream.co.kr/"

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

    def parse(self, response):
        for select in response.xpath("//table/tbody/tr"):

            if select.xpath("td/span/text()").extract()[0] == "영자C":
                # 관리자가 작성한 게시물(공지) 거르고 크롤링
                continue
            else:
                item = DamoaItem() # item객체 생성

                item['source'] = self.name

                titleXpath = "td/a/text()"
                item['title'] = createItemUseXpath(select, titleXpath, texttype="")

                linkXpath = "td/a/@href"
                item['link'] =  self.baseUrl + createItemUseXpath(select, linkXpath, texttype=TextType.LINK).split("java")[0]

                attrXpath = "//div[@class='titleArea02']/h2/img/@alt"
                item['attribute'] = createItemUseXpath(select, attrXpath, texttype="")

                tagName = "span"
                tagAttrs =  {"class": "countGroup"}
                item['date'] = createItemUseBs4(item['link'], tagName, tagAttrs, encoding="utf8", texttype=TextType.DATE).split("|")[-1].strip()+":00"

                tagName = "span"
                tagAttrs = {"class": "countGroup"}
                item['hits'] = createItemUseBs4(item['link'], tagName, tagAttrs, encoding="utf8", texttype=TextType.INT).split("|")[0].strip()

                tagName = "span"
                tagAttrs = {"class": "countGroup"}
                item['recommened'] = createItemUseBs4(item['link'], tagName, tagAttrs, encoding="utf8", texttype=TextType.INT).split("|")[1].strip()

                item['last_update'] = getCurrentTime(TextType.STRING)

                item['pop'] = createItem_pop(item['date'], item['recommened'], item['hits'])

                tagName = "div"
                tagAttrs = {"class": "docuCont03"}
                item['text'] = createItemUseBs4(item['link'], tagName, tagAttrs, encoding="utf8", texttype=TextType.TEXT)

                item['image'] = createItemUseBs4_PostImage(item['link'])

                yield item


