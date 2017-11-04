
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

class Spider(scrapy.Spider):
    name = 'humoruniv'

    baseUrl = "http://web.humoruniv.com/board/humor/"

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

    def parse_site(self, response):
        sel = Selector(response)
        for select in sel.xpath('//div[@id="cnts_list_new"]/div/table/tr'):
            item = DamoaItem()

            item['source'] = self.name

            titleXpath = "td[@class='li_sbj']/a/text()"
            item['title'] = createItemUseXpath(select, titleXpath,texttype="")
            if item['title'] == "":
                pass
            else:
                linkXpath = "td[@class='li_sbj']/a/@href"
                item['link'] = self.baseUrl + createItemUseXpath(select, linkXpath, texttype=TextType.LINK)

                tagName = "a"
                tagAttr = {"class" : "bo"}
                item['attribute'] = createItemUseBs4(item['link'],tagName, tagAttr, encoding="CP949", texttype="")

                dateXpath = "td[@class='li_date']/span/text()"
                item['date'] = createItemUseXpath(select, dateXpath,texttype=TextType.DATE) + ":00"
                if len(item['date'].split("-")[0])<3:
                    item['date'] = "20" + item['date']

                hitsXpath = "td[@class='li_und']/text()"
                item['hits'] = createItemUseXpath(select, hitsXpath, texttype=TextType.INT)

                recommenedXpath = "td[@class='li_und']/span[@class='o']/text()"
                item['recommened'] = createItemUseXpath(select, recommenedXpath, texttype=TextType.INT)

                item['last_update'] = getCurrentTime(TextType.STRING)

                item['pop'] = createItem_pop(item['recommened'],item['hits'], self.name)

                tagName = "div"
                tagAttr = {"id": "cnts"}
                item['text'] = createItemUseBs4(item['link'], tagName, tagAttr, encoding="CP949", texttype=TextType.TEXT)

                item['image'] = createItemUseBs4_PostImage(item['link'], "http://c.huv")

                yield item