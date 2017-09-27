
"""
clien 크롤링 스파이더

MAX_PAGE -> DamoaCrawler.spiders.spider_Setting에 있음

Last Update 2017.07.14

"""

import requests
import scrapy
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

            item['source'] = self.name

            # print(type(item["source"]))

            # 해당xpath 텍스트를 읽어와서 문자열로 바꾸고 item객체에 저장
            titleTmp = select.xpath('div[@class="list-title"]/a[@class="list-subject"]/text()').extract()
            titleTmp2 = "".join(titleTmp).replace('\t','').replace('\n','').replace('\r','')
            item['title'] = titleTmp2

            # print(type(item["title"]))

            # 링크 저장
            item['link'] = 'http://www.clien.net' + select.xpath('div[@class="list-title"]/a/@href').extract()[0]

            # print(type(item["link"]))

            # 게시판에 게시물 링크 타고가기 위해 리퀘스트 재요청
            postUrl = BeautifulSoup(requests.get(item['link']).content, "html.parser")

            # 게시물로 이동후 속성읽어서 저장
            attributeTmp = postUrl.find(name="li", attrs={"class": "board-title"}).text.strip()
            item['attribute'] = attributeTmp[2:]

            # print(type(item["attribute"]))

            # 게시일 저장
            dateTmp = select.xpath('div/span[@class="time"]/span[@class="timestamp"]/text()').extract()
            item['date'] = dateTmp[0]

            # print(type(item["date"]))

            # 조회수 저장 -> 게시물 이동후 확인해야함
            hitsTmp = postUrl.find(name='span', attrs={"class" : "view-count"}).text.strip()
            item['hits'] = hitsTmp

            # print(type(item["hits"]))

            # 추천수 저장 -> 공감수
            recommTmp = postUrl.find(name='div', attrs={"class" : "title-symph"}).text.strip()
            item['recommened'] = recommTmp

            # print(type(item["recommened"]))

            # 마지막 갱신일 저장
            item['last_update'] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

            # print(type(item["last_update"]))

            dateTmp_post = datetime.strptime(item['date'], '%Y-%m-%d %H:%M:%S')
            dateTmp_curr = datetime.strptime(datetime.now().strftime('%Y-%m-%d %H:%M:%S'), '%Y-%m-%d %H:%M:%S')

            # 한시간당 가중치 감소(시간으로 조회수 나눔)
            timeTmp = (dateTmp_curr-dateTmp_post).total_seconds()/3600

            if(timeTmp <= 1):
                timeTmp = 1
                commentTmp = int(item['recommened']) + ((int(item['hits']) / timeTmp))
            else :
                commentTmp = int(item['recommened']) + ((int(item['hits']) / timeTmp))

            item['pop'] = commentTmp    # 인기도 저장

            # print(type(item["pop"]))

            # 게시물 텍스트 읽어서 문자열로 변환후 저장
            textTmp = postUrl.find(name="div", attrs={"class":"post-article fr-view"}).text.strip()
            item['text'] = "".join(textTmp).replace('\n','')

            # print(type(item["text"]))
            # print("\n")
            #
            # print("sdsdsdsdsd")
            # print(item["title"])
            # # print(filterItem(item))
            # print("sdsdsdsdsd")

            # if filterItem(item) != None:
            #     yield filterItem(item)
                # print(filterItem(item))
            # print(pp)
            # print("sdsd")

            yield item


            # print("sd")


