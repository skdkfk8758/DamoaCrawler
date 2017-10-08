
"""
This is Game 크롤링 스파이더

MAX_PAGE -> Damoa.spiders.Setting에 있음

Last Update 2017.10.08

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
                pass
            else:
                item = DamoaItem() # item객체 생성

                item['source'] = self.name

                # 해당xpath 텍스트를 읽어와서 문자열로 바꾸고 item객체에 저장
                titleTmp = select.xpath('td/a/text()').extract()
                titleTmp2 = "".join(titleTmp).replace('\t','').replace('\n','').replace('\r','')
                item['title'] = titleTmp2

                print(item['title'])

                # 링크 저장
                item['link'] = self.baseUrl + select.xpath('td/a/@href').extract()[0]

                # print(item['link'])

                # 게시물로 이동후 속성읽어서 저장
                attributeTmp = select.xpath("//div[@class='board-title-part']/h1/a/strong/text()").extract()[0]
                attributeTmp2 = "".join(attributeTmp).replace('\t', '').replace('\n', '').replace('\r', '')
                item['attribute'] = attributeTmp2

                print(item['attribute'])

                # 게시판에 게시물 링크 타고가기 위해 리퀘스트 재요청
                postUrl = BeautifulSoup(requests.get(item['link']).content, "html.parser")

                # 게시일 저장
                dateTmp = postUrl.find(name='span', attrs={"class": "info-one postdate"}).text.strip()
                item['date'] = dateTmp.replace(".", "-")
                # print(item['date'])

                # 조회수 저장 -> 게시물 이동후 확인해야함
                hitsTmp = postUrl.find(name='span', attrs={"class": "info-one readcount"}).text.strip()
                hitsTmp2 = "".join(hitsTmp).replace(',', '').replace('조회: ','')
                item['hits'] = hitsTmp2
                # print(item['hits'])

                # 추천수 저장 -> 공감수
                recommenedTmp = postUrl.find(name='span', attrs={"class": "field-tboard-overall-article-ratingsum"}).text.strip()
                item['recommened'] = recommenedTmp
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
                textTmp = postUrl.find(name="div", attrs={"class": "content board-content"}).text.strip()
                postText = "".join(textTmp).replace('\n', '')
                item['text'] = postText

                # print(postText)

                if filterItem(item) != None:
                    yield filterItem(item)



