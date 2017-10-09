
"""
게임샷 크롤링 스파이더
Make : 2017.10.08

MAX_PAGE -> Damoa.spiders.Setting에 있음

2017.10.09
 - 코드정리

"""

import scrapy
import requests
from bs4 import BeautifulSoup

from Crawler.filterItem import *
from Crawler.items import DamoaItem
from Crawler.spiders.Setting import *


class GameShot(scrapy.Spider):
    name = 'gameshot' # spider name

    baseUrl = "http://www.gameshot.net/talk/"

    # 리퀘스트 요청
    def start_requests(self): 
        for i in range(1, MAX_PAGE, 1):
            yield scrapy.Request("http://www.gameshot.net/talk/?&bbs=free&sby=title&skey=&pg={}".format(i))
            yield scrapy.Request("http://www.gameshot.net/talk/?&bbs=gamenews&sby=title&skey=&pg={}".format(i))
            yield scrapy.Request("http://www.gameshot.net/talk/?&bbs=ip_shop&sby=title&skey=&pg={}".format(i))

    # 사이트 파싱
    def parse(self, response):
        for select in response.xpath("//table/tbody/tr"):

            if select.xpath("td/text()").extract()[0] == "관리자":
                # 관리자가 작성한 게시물(공지) 거르고 크롤링
                pass
            else:
                item = DamoaItem() # item객체 생성

                # 출처 저장
                item['source'] = self.name

                # 게시물 제목 저장
                item['title'] = "".join(titleTmp = select.xpath('td/p/a/strong/text()').extract()).replace('\t','').replace('\n','').replace('\r','')
                # print(item['title'])

                # 링크 저장
                item['link'] = self.baseUrl + select.xpath('td/p/a/@href').extract()[0]
                # print(item['link'])

                # 게시판에 게시물 링크 타고가기 위해 리퀘스트 재요청
                JoinPostUrl = BeautifulSoup(requests.get(item['link']).content, "html.parser", from_encoding='CP949')

                # 게시물로 이동후 속성읽어서 저장
                item['attribute'] = "".join(select.xpath("//li[@class='active']/text()").extract()[0]).replace('\t', '').replace('\n', '').replace('\r', '')
                # print(item['attribute'])

                # 게시일 저장
                item['date'] = JoinPostUrl.find(name='p', attrs={"class": "f12 a0a0a0"}).text.strip().replace(".", "-")
                # print(item['date'])

                # 조회수 저장 -> 게시물 이동후 확인해야함
                item['hits'] = "".join(select.xpath("td/abbr/text()").extract()[0]).replace(',', '')
                # print(item['hits'])

                # 추천수 저장 -> 공감수
                # recommTmp = select.xpath("td[@class='t_hits']/text()").extract()[1]
                item['recommened'] = 0
                # print(item['recommened'])

                # 마지막 갱신일 저장 -> 현재시간
                item['last_update'] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

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

                # 게시물 텍스트 읽어서 문자열로 변환후 저장
                item['text'] = "".join(JoinPostUrl.find(name="div", attrs={"id": "content"}).text.strip()).replace('\n', '')
                # print(postText)

                # Item -> DB에 저장
                if filterItem(item) != None:
                    # 아이템 필터링 후 DB저장
                    yield filterItem(item)



