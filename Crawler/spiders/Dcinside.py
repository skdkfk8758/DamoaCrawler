
"""
DcInsede 크롤링 스파이더

MAX_PAGE -> Damoa.spiders.Setting에 있음

Last Update 2017.08.13

"""

import scrapy
from bs4 import BeautifulSoup
import requests
import urllib.request

from Crawler.filterItem import *
from Crawler.items import DamoaItem
from Crawler.spiders.Setting import *


class DcInside(scrapy.Spider):
    name = 'dcinside' # spider name

    baseUrl = "http://gall.dcinside.com"

    # 리퀘스트 요청
    def start_requests(self):
        for i in range(1, MAX_PAGE, 1):
            yield scrapy.Request("http://gall.dcinside.com/board/lists?id=47&page={0}".format(i))
            # yield scrapy.Request("http://gall.dcinside.com/board/lists/?id=leavesister&page={}".format(i))
            # yield scrapy.Request("http://gall.dcinside.com/board/lists/?id=strongest&page={}".format(i))
            # yield scrapy.Request("http://gall.dcinside.com/board/lists/?id=manhole&page={}".format(i))
            # yield scrapy.Request("http://gall.dcinside.com/board/lists/?id=onmyoji&page={}".format(i))
            # yield scrapy.Request("http://gall.dcinside.com/board/lists/?id=hit&page={}".format(i))
            # yield scrapy.Request("http://gall.dcinside.com/board/lists/?id=superidea&page={}".format(i))
            # yield scrapy.Request("http://gall.dcinside.com/board/lists/?id=yusik&page={}".format(i))
            # yield scrapy.Request("http://gall.dcinside.com/board/lists/?id=event_voicere&page={}".format(i))
            # yield scrapy.Request("http://gall.dcinside.com/board/lists/?id=dcwiki&page={}".format(i))
            # yield scrapy.Request("http://gall.dcinside.com/board/lists/?id=study_listN&page={}".format(i))
            # yield scrapy.Request("http://gall.dcinside.com/board/lists/?id=cool&page={}".format(i))
            # yield scrapy.Request("http://gall.dcinside.com/board/lists/?id=dogdripdoctor&page={}".format(i))
            # yield scrapy.Request("http://gall.dcinside.com/board/lists/?id=rb&page={}".format(i))
            # yield scrapy.Request("http://gall.dcinside.com/board/lists/?id=xmas&page={}".format(i))
            # yield scrapy.Request("http://gall.dcinside.com/board/lists/?id=biza&page={}".format(i))
            # yield scrapy.Request("http://gall.dcinside.com/board/lists/?id=biza_1&page={}".format(i))
            # yield scrapy.Request("http://gall.dcinside.com/board/lists/?id=congratulation&page={}".format(i))
            # yield scrapy.Request("http://gall.dcinside.com/board/lists/?id=assistance&page={}".format(i))

    # 사이트 파싱
    def parse(self, response):

        for select in response.xpath("//table/tbody/tr"):

            item = DamoaItem() # item객체 생성

            # print(select.xpath("td[@class='t_notice']/text()").extract())
            if select.xpath("td[@class='t_notice']/text()").extract()[0] == "공지":
                # 공지사항 제거하고 파싱
                # print("asd")
                pass
            else:
                item['source'] = self.name

                # print(item['source'])

                # 해당xpath 텍스트를 읽어와서 문자열로 바꾸고 item객체에 저장
                titleTmp = select.xpath('td/a/text()').extract()
                titleTmp2 = "".join(titleTmp).replace('\t','').replace('\n','').replace('\r','')
                item['title'] = titleTmp2

                # print(item['title'])

                # 링크 저장
                item['link'] = self.baseUrl + select.xpath('td/a/@href').extract()[0]

                # print(item['link'])

                # 게시물로 이동후 속성읽어서 저장
                attributeTmp = select.xpath("//body/div[@id='dgn_wrap']/div[@id='dgn_gallery_wrap']/div[@class='gallery_content']/div/div[@class='gallery_title']/h1/a/span/text()").extract()[0]
                item['attribute'] = attributeTmp

                # print(item['attribute'])

                # 게시일 저장
                dateTmp = select.xpath("td/@title").extract()[0]
                item['date'] = dateTmp.replace(".", "-")
                # print(item['date'])

                # 조회수 저장 -> 게시물 이동후 확인해야함
                hitsTmp = select.xpath("td[@class='t_hits']/text()").extract()[0]
                item['hits'] = hitsTmp
                # print(item['hits'])

                # 추천수 저장 -> 공감수
                recommTmp = select.xpath("td[@class='t_hits']/text()").extract()[1]
                item['recommened'] = recommTmp
                # print(item['recommened'])

                # 마지막 갱신일 저장
                item['last_update'] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

                dateTmp1 = datetime.strptime(item['date'], '%Y-%m-%d %H:%M:%S')
                dateTmp2 = dateTmp1.strftime('%Y-%m-%d %H:%M:%S')
                # print(dateTmp_post.strftime('%Y-%m-%d %H:%M:%S'))
                # dateTmp_post = datetime.strptime(datetime.now().strftime('%Y-%m-%d %H:%M:%S'), '%Y-%m-%d %H:%M:%S')
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

                yield scrapy.Request(item["link"], callback=self.parseText)

                print(item['text'])

                if filterItem(item) != None:
                    yield filterItem(item)

    def parseText(self, response):

        # ss = BeautifulSoup(response)

        response.xpath("//title")

