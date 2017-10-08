
"""
게임샷 크롤링 스파이더

MAX_PAGE -> Damoa.spiders.Setting에 있음

Last Update 2017.10.08

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
        # print(response)

        for select in response.xpath("//table/tbody/tr"):

            if select.xpath("td/text()").extract()[0] == "관리자":
                pass
            else:
                item = DamoaItem() # item객체 생성

                item['source'] = self.name

                # 해당xpath 텍스트를 읽어와서 문자열로 바꾸고 item객체에 저장
                titleTmp = select.xpath('td/p/a/strong/text()').extract()
                titleTmp2 = "".join(titleTmp).replace('\t','').replace('\n','').replace('\r','')
                item['title'] = titleTmp2

                # print(item['title'])

                # 링크 저장
                item['link'] = self.baseUrl + select.xpath('td/p/a/@href').extract()[0]

                # print(item['link'])

                # 게시물로 이동후 속성읽어서 저장
                attributeTmp = select.xpath("//li[@class='active']/text()").extract()[0]
                attributeTmp2 = "".join(attributeTmp).replace('\t', '').replace('\n', '').replace('\r', '')
                item['attribute'] = attributeTmp2

                # print(item['attribute'])

                # 게시판에 게시물 링크 타고가기 위해 리퀘스트 재요청
                postUrl = BeautifulSoup(requests.get(item['link']).content, "html.parser", from_encoding='CP949')

                # 게시일 저장
                dateTmp = postUrl.find(name='p', attrs={"class": "f12 a0a0a0"}).text.strip()
                item['date'] = dateTmp.replace(".", "-")
                # print(item['date'])

                # 조회수 저장 -> 게시물 이동후 확인해야함
                hitsTmp = select.xpath("td/abbr/text()").extract()[0]
                hitsTmp2 = "".join(hitsTmp).replace(',', '')
                item['hits'] = hitsTmp2
                # print(item['hits'])

                # 추천수 저장 -> 공감수
                # recommTmp = select.xpath("td[@class='t_hits']/text()").extract()[1]
                item['recommened'] = 0
                # print(item['recommened'])

                # 마지막 갱신일 저장
                item['last_update'] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

                dateTmp1 = datetime.strptime(item['date'], '%Y-%m-%d %H:%M:%S')
                dateTmp2 = dateTmp1.strftime('%Y-%m-%d %H:%M:%S')
                dateTmp_post = datetime.strptime(dateTmp2, '%Y-%m-%d %H:%M:%S')
                dateTmp_curr = datetime.strptime(datetime.now().strftime('%Y-%m-%d %H:%M:%S'), '%Y-%m-%d %H:%M:%S')

                # 한시간당 가중치 감소(시간으로 조회수 나눔)
                timeTmp = (dateTmp_curr-dateTmp_post).total_seconds()/3600

                if(timeTmp <= 0):
                    timeTmp = 1
                    commentTmp = int(item['recommened']) + ((int(item['hits']) / timeTmp))
                else :
                    commentTmp = int(item['recommened']) + ((int(item['hits']) / timeTmp))

                item['pop'] = commentTmp    # 인기도 저장

                # 게시물 텍스트 읽어서 문자열로 변환후 저장
                textTmp = postUrl.find(name="div", attrs={"id": "content"}).text.strip()
                postText = "".join(textTmp).replace('\n', '')
                item['text'] = postText

                # print(postText)

                if filterItem(item) != None:
                    yield filterItem(item)



