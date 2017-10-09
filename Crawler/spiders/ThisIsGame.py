
"""
This is Game Spider
Make :  2017.10.08

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

class ThisIsGame(scrapy.Spider):
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

                #출처 저장
                item['source'] = self.name

                # 게시물 제목 저장
                item['title'] = "".join(select.xpath('td/a/text()').extract()).replace('\t','').replace('\n','').replace('\r','')
                # print(item['title'])

                # 링크 저장
                item['link'] = self.baseUrl + select.xpath('td/a/@href').extract()[0]
                # print(item['link'])

                # 게시물 텍스트를 읽기위해 게시물 링크로 이동
                JoinPostUrl = BeautifulSoup(requests.get(item['link']).content, "html.parser")

                # 게시물로 이동후 속성읽어서 저장
                item['attribute'] = "".join(select.xpath("//div[@class='board-title-part']/h1/a/strong/text()").extract()[0]).replace('\t', '').replace('\n', '').replace('\r', '')
                # print(item['attribute'])

                # 게시일 저장
                item['date'] = JoinPostUrl.find(name='span', attrs={"class": "info-one postdate"}).text.strip().replace(".", "-")
                # print(item['date'])

                # 조회수 저장 -> 게시물 이동후 확인해야함
                item['hits'] = "".join(JoinPostUrl.find(name='span', attrs={"class": "info-one readcount"}).text.strip()).replace(',', '').replace('조회: ','')
                # print(item['hits'])

                # 추천수 저장 -> 공감수
                item['recommened'] = JoinPostUrl.find(name='span', attrs={"class": "field-tboard-overall-article-ratingsum"}).text.strip()
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
                    # print(item['pop'])

                    # 게시물 텍스트 저장
                item['text'] = "".join(JoinPostUrl.find(name="div", attrs={"class": "content board-content"}).text.strip()).replace('\n', '')
                # print(postText)

                if filterItem(item) != None:
                    yield filterItem(item)



