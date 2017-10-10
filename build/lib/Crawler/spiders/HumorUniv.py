
"""
웃긴대학 Spider
Create : 2017.10.06

MAX_PAGE -> Damoa.spiders.Setting에 있음

2017.10.09
 - 코드정리

"""

import scrapy
import requests
from bs4 import BeautifulSoup
from scrapy.selector import Selector

from Crawler.filterItem import *
from Crawler.items import DamoaItem
from Crawler.spiders.Setting import *
from Crawler.CreateItem import *

class HumorUniv(scrapy.Spider):
    name = 'humoruniv'

    baseUrl = "http://web.humoruniv.com/board/humor/"

    # 각 게시판별로 리퀘스트 요청
    def start_requests(self):
        for i in range(1, MAX_PAGE, 1):
            yield scrapy.Request('http://web.humoruniv.com/board/humor/list.html?table=pds&pg={0}'.format(i - 1), self.parse_site)
            yield scrapy.Request('http://web.humoruniv.com//board/humor/list.html?table=pdswait&pg={0}'.format(i - 1), self.parse_site)
            yield scrapy.Request('http://web.humoruniv.com//board/humor/list.html?table=kin&pg={0}'.format(i - 1), self.parse_site)
            yield scrapy.Request('http://web.humoruniv.com//board/humor/list.html?table=otl&pg={0}'.format(i - 1), self.parse_site)
            yield scrapy.Request('http://web.humoruniv.com//board/humor/list.html?table=art_toon&pg={0}'.format(i - 1), self.parse_site)
            yield scrapy.Request('http://web.humoruniv.com//board/humor/list.html?table=nova_toon&pg={0}'.format(i - 1), self.parse_site)
            yield scrapy.Request('http://web.humoruniv.com/board/humor/list.html?table=fear&pg={0}'.format(i - 1), self.parse_site)
            yield scrapy.Request('http://web.humoruniv.com/board/humor/list.html?table=guest&pg={0}'.format(i - 1), self.parse_site)
            yield scrapy.Request('http://web.humoruniv.com/board/humor/list.html?table=mild&pg={0}'.format(i - 1), self.parse_site)
            yield scrapy.Request('http://web.humoruniv.com/board/humor/list.html?table=free&pg={0}'.format(i - 1), self.parse_site)
            yield scrapy.Request('http://web.humoruniv.com/board/humor/list.html?table=poll&pg={0}'.format(i - 1), self.parse_site)
            yield scrapy.Request('http://web.humoruniv.com/board/humor/list.html?table=game&pg={0}'.format(i - 1), self.parse_site)
            yield scrapy.Request('http://web.humoruniv.com/board/humor/list.html?table=thema2&pg={0}'.format(i - 1), self.parse_site)
            yield scrapy.Request('http://web.humoruniv.com/board/humor/list.html?table=lol&pg={0}'.format(i - 1), self.parse_site)
            yield scrapy.Request('http://web.humoruniv.com/board/humor/list.html?table=pride&pg={0}'.format(i - 1), self.parse_site)
            yield scrapy.Request('http://web.humoruniv.com/board/humor/list.html?table=muzik&pg={0}'.format(i - 1), self.parse_site)
            yield scrapy.Request('http://web.humoruniv.com/board/humor/list.html?table=thema3&pg={0}'.format(i - 1), self.parse_site)
            yield scrapy.Request('http://web.humoruniv.com/board/humor/list.html?table=animaluniv&pg={0}'.format(i - 1), self.parse_site)
            yield scrapy.Request('http://web.humoruniv.com/board/humor/list.html?table=com&pg={0}'.format(i - 1), self.parse_site)
            yield scrapy.Request('http://web.humoruniv.com/board/humor/list.html?table=moofama&pg={0}'.format(i - 1), self.parse_site)
            yield scrapy.Request('http://web.humoruniv.com/board/humor/list.html?table=whitehand&pg={0}'.format(i - 1), self.parse_site)
            yield scrapy.Request('http://web.humoruniv.com/board/humor/list.html?table=workshop&pg={0}'.format(i - 1), self.parse_site)
            yield scrapy.Request('http://web.humoruniv.com/board/humor/list.html?table=solo&pg={0}'.format(i - 1), self.parse_site)
            yield scrapy.Request('http://web.humoruniv.com/board/humor/list.html?table=love&pg={0}'.format(i - 1), self.parse_site)
            yield scrapy.Request('http://web.humoruniv.com/board/humor/list.html?table=spnatural&pg={0}'.format(i - 1), self.parse_site)
            yield scrapy.Request('http://web.humoruniv.com/board/humor/list.html?table=car&pg={0}'.format(i - 1), self.parse_site)
            yield scrapy.Request('http://web.humoruniv.com/board/humor/list.html?table=sns&pg={0}'.format(i - 1), self.parse_site)
            yield scrapy.Request('http://web.humoruniv.com/board/humor/list.html?table=dump&pg={0}'.format(i - 1), self.parse_site)
            yield scrapy.Request('http://web.humoruniv.com/board/humor/list.html?table=studying&pg={0}'.format(i - 1), self.parse_site)
            yield scrapy.Request('http://web.humoruniv.com/board/humor/list.html?table=memory&pg={0}'.format(i - 1), self.parse_site)
            yield scrapy.Request('http://web.humoruniv.com/board/humor/list.html?table=program&pg={0}'.format(i - 1), self.parse_site)
            yield scrapy.Request('http://web.humoruniv.com/board/humor/list.html?table=sympathy&pg={0}'.format(i - 1), self.parse_site)
            yield scrapy.Request('http://web.humoruniv.com/board/humor/list.html?table=phone&pg={0}'.format(i - 1), self.parse_site)
            yield scrapy.Request('http://web.humoruniv.com/board/humor/list.html?table=army&pg={0}'.format(i - 1), self.parse_site)
            yield scrapy.Request('http://web.humoruniv.com/board/humor/list.html?table=worldcup&pg={0}'.format(i - 1), self.parse_site)
            yield scrapy.Request('http://web.humoruniv.com/board/humor/list.html?table=cabinet&pg={0}'.format(i - 1), self.parse_site)

    # 리스폰스 받아서 사이트 파싱
    def parse_site(self, response):
        sel = Selector(response)
        for select in sel.xpath('//div[@id="cnts_list_new"]/div/table/tr'):
            item = DamoaItem()

            # 게시물 출처 저장
            item['source'] = self.name

            # 게시물 제목 저장
            titleXpath = "td[@class='li_sbj']/a/text()"
            item['title'] = createItemUseXpath(select, titleXpath,texttype="")
            if item['title'] == "":
                pass
            else:
                # 게시물 링크 저장
                linkXpath = "td[@class='li_sbj']/a/@href"
                item['link'] = self.baseUrl + createItemUseXpath(select, linkXpath, texttype="link")

                # 게시물 속성 저장
                tagName = "a"
                tagAttr = {"class" : "bo"}
                item['attribute'] = createItemUseBs4(item['link'],tagName, tagAttr, encoding="CP949", texttype="")
                # print(item['attribute'])

                # 게시물 게시일 저장
                dateXpath = "td[@class='li_date']/span/text()"
                item['date'] = createItemUseXpath(select, dateXpath,texttype="") + ":00"
                if len(item['date'].split("-")[0])<3:
                    item['date'] = "20" + item['date']

                # 게시물 조회수 저장
                hitsXpath = "td[@class='li_und']/text()"
                item['hits'] = createItemUseXpath(select, hitsXpath, texttype="hits")

                # 추천수 OR 공감수 저장, 추천수나 공감수가 게시물에 존재하지않으면 0
                recommenedXpath = "td[@class='li_und']/span[@class='o']/text()"
                item['recommened'] = createItemUseXpath(select, recommenedXpath, texttype="hits")
                # print(item['recommened'])

                # 마지막 갱신일 저장 -> 현재 시간
                item['last_update'] = getCurrentTime("String")

                # 게시물 인기도 저장
                item['pop'] = createItem_pop(item['date'], item['recommened'], item['hits'])
                # print(item['pop'])

                # 게시물 텍스트 저장
                tagName = "div"
                tagAttr = {"id": "cnts"}
                item['text'] = createItemUseBs4(item['link'], tagName, tagAttr, encoding="CP949", texttype="")

                # Item -> DB에 저장
                if filterItem(item) != None:
                    # 아이템 필터링 후 DB저장
                    yield filterItem(item)
