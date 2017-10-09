
"""
Clien Spider
Make : 2017.06.14

MAX_PAGE -> DamoaCrawler.spiders.spider_Setting에 있음

2017.10.09
 - 코드정리

"""
import scrapy
import requests
from bs4 import BeautifulSoup

from Crawler.filterItem import *
from Crawler.items import DamoaItem
from Crawler.spiders.Setting import *

class Clien(scrapy.Spider):
    name = 'clien' # spider name

    # 리퀘스트 요청
    def start_requests(self):
        for i in range(1, MAX_PAGE, 1):
            yield scrapy.Request('http://clien.net/service/board/park?&od=T31&po={0}'.format(i - 1))
            yield scrapy.Request('http://clien.net/service/board/kin?&od=T31&po={0}'.format(i - 1))
            yield scrapy.Request('http://clien.net/service/board/news?&od=T31&po={0}'.format(i - 1))
            yield scrapy.Request('http://clien.net/service/board/useful?&od=T31&po={0}'.format(i - 1))
            yield scrapy.Request('http://clien.net/service/board/pds?&od=T31&po={0}'.format(i - 1))
            yield scrapy.Request('http://clien.net/service/board/lecture?&od=T31&po={0}'.format(i - 1))
            yield scrapy.Request('http://clien.net/service/board/use?&od=T31&po={0}'.format(i - 1))
            yield scrapy.Request('http://clien.net/service/board/chehum?&od=T31&po={0}'.format(i - 1))
            yield scrapy.Request('http://clien.net/service/board/bug?&od=T31&po={0}'.format(i - 1))

    # 사이트 파싱
    def parse(self, response):
        for select in response.xpath('//div[@class="item"]'):
            item = DamoaItem() # item객체 생성

            #출처 저장
            item['source'] = self.name
            # print(type(item["source"]))

            # 해당xpath 텍스트를 읽어와서 문자열로 바꾸고 item객체에 저장
            item['title'] = "".join(select.xpath('div[@class="list-title"]/a[@class="list-subject"]/text()').extract()).replace('\t','').replace('\n','').replace('\r','')
            # print(type(item["title"]))

            # 링크 저장
            item['link'] = 'http://www.clien.net' + select.xpath('div[@class="list-title"]/a/@href').extract()[0]
            # print(type(item["link"]))

            # 게시물 텍스트를 읽기위해 게시물 링크로 이동
            JoinPostUrl = BeautifulSoup(requests.get(item['link']).content, "html.parser",from_encoding='CP949')

            # 게시물로 이동후 속성읽어서 저장
            item['attribute'] = JoinPostUrl.find(name="li", attrs={"class": "board-title"}).text.strip()
            # print(type(item["attribute"]))

            # 게시일 저장
            item['date'] = select.xpath('div/span[@class="time"]/span[@class="timestamp"]/text()').extract()
            # print(type(item["date"]))

            # 조회수 저장 -> 게시물 이동후 확인해야함
            item['hits'] = JoinPostUrl.find(name='span', attrs={"class" : "view-count"}).text.strip()
            # print(type(item["hits"]))

            # 추천수 저장 -> 공감수
            item['recommened'] = JoinPostUrl.find(name='div', attrs={"class" : "title-symph"}).text.strip()
            # print(type(item["recommened"]))

            # 마지막 갱신일 저장 -> 현재시간
            item['last_update'] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            # print(type(item["last_update"]))

            postDateTypeOfDateTime = datetime.strptime(item['date'], '%Y-%m-%d %H:%M:%S')  # 문자열 날짜를 datetime으로 변형
            currentDateTypeOfDateTime = datetime.strptime(item['last_update'],
                                                          '%Y-%m-%d %H:%M:%S')  # 문자열 날짜를 datetime으로 변형

            # 한시간당 가중치 감소(시간으로 조회수 나눔)
            postOpeningTime = (currentDateTypeOfDateTime - postDateTypeOfDateTime).total_seconds() / 3600

            # 인기도 계산 -> 저장
            if (postOpeningTime <= 0):
                postOpeningTime = 1
                item['pop'] = int(item['recommened']) + ((int(item['hits']) / postOpeningTime))
            else:
                item['pop'] = int(item['recommened']) + ((int(item['hits']) / postOpeningTime))
            # print(item['pop'])

            # 게시물 텍스트 읽어서 문자열로 변환후 저장
            item['text'] = "".join(JoinPostUrl.find(name="div", attrs={"class":"post-article fr-view"}).text.strip()).replace('\n','')

            # Item -> DB에 저장
            if filterItem(item) != None:
                # 아이템 필터링 후 DB저장
                yield filterItem(item)


