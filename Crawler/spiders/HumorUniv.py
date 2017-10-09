
"""
웃긴대학 Spider
Make : 2017.10.06

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

class HumorUniv(scrapy.Spider):
    name = 'humoruniv'

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

            # 출처 저장
            item['source'] = self.name

            # 게시물 제목 저장
            item['title'] = "".join(select.xpath('td[@class="li_sbj"]/a/text()').extract()).replace('\t', '').replace('\r', '').replace('\n','')

            # 링크 저장
            linkLengthTmp = select.xpath('td[@class="li_sbj"]/a/@href').extract()
            if len(linkLengthTmp)>0:
                part_link = select.xpath('td[@class="li_sbj"]/a/@href').extract()[0]
            else:
                continue
            item['link'] = 'http://web.humoruniv.com/board/humor/' + part_link
            # print(item['link'])

            # 게시물 텍스트를 읽기위해 게시물 링크로 이동
            JoinPostUrl = BeautifulSoup(requests.get(item['link']).content, "html.parser",from_encoding='CP949')

            # 게시물로 이동후 게시판속성 저장
            item['attribute'] = JoinPostUrl.find(name='a', attrs={"class" : "bo"}).text.strip()
            # print(item['attribute'])

            # 게시일 저장
            item['date'] = ' '.join(select.xpath('td[@class="li_date"]/span/text()').extract()) + ":00"
            # print(item['date'])

            # 조회수 저장 -> 게시물 이동후 확인해야함
            hitsTmp = select.xpath('td[@class="li_und"]/text()').extract()
            item['hits'] = "".join(hitsTmp).replace('\t', '').replace('\r', '').replace('\n','').replace('/','').replace(',','').strip()

            # 추천수 저장
            item['recommened'] = "".join(select.xpath('td[@class="li_und"]/span[@class="o"]/text()').extract()).replace('\t', '').replace('\r', '').replace('\n', '').replace('/', '')

            # 마지막 갱신일 저장 -> 현재 시간
            item['last_update'] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

            postDateTypeOfDateTime = datetime.strptime(item['date'], '%Y-%m-%d %H:%M:%S')  # 문자열 날짜를 datetime으로 변형
            currentDateTypeOfDateTime = datetime.strptime(item['last_update'],
                                                          '%Y-%m-%d %H:%M:%S')  # 문자열 날짜를 datetime으로 변형

            # 한시간당 가중치 감소(시간으로 조회수 나눔)
            postOpeningTime = (currentDateTypeOfDateTime-postDateTypeOfDateTime).total_seconds()/3600

            # 인기도 계산 -> 저장
            if(postOpeningTime <= 0):
                postOpeningTime = 1
                item['pop'] = int(item['recommened']) + ((int(item['hits']) / postOpeningTime))
            else :
                item['pop'] = int(item['recommened']) + ((int(item['hits']) / postOpeningTime))

            # 게시물 텍스트 읽어서 문자열로 변환후 저장
            item['text'] = "".join(JoinPostUrl.find(name="div", attrs={"id": "cnts"}).text.strip()).replace('\n', '')

            # Item -> DB에 저장
            if filterItem(item) != None:
                # 아이템 필터링 후 DB저장
                yield filterItem(item)
