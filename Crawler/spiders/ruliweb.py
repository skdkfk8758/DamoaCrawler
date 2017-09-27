
"""
Ruliweb 크롤링 스파이더

MAX_PAGE -> DamoaCrawler.spiders.spider_Setting에 있음

Last Update : 2017.07.16

"""

import requests
import scrapy
from bs4 import BeautifulSoup

from Crawler.filterItem import *
from Crawler.items import DamoaItem
from Crawler.spiders.Setting import *


class RuliWeb(scrapy.Spider):
    name = 'ruli' # spider name

    #게시판 속성 -> url이동에 사용
    postListTitle = ['http://bbs.ruliweb.com/ps', 'http://bbs.ruliweb.com/psp', 'http://bbs.ruliweb.com/xbox',
                     'http://bbs.ruliweb.com/nin', 'http://bbs.ruliweb.com/nds', 'http://bbs.ruliweb.com/pc',
                     'http://bbs.ruliweb.com/mobile', 'http://bbs.ruliweb.com/av', 'http://bbs.ruliweb.com/sports',
                     'http://bbs.ruliweb.com/news', 'http://bbs.ruliweb.com/hobby', 'http://bbs.ruliweb.com/market/board/1020',
                     'http://bbs.ruliweb.com/community', 'http://bbs.ruliweb.com/twitch', 'http://bbs.ruliweb.com/best',
                     'http://bbs.ruliweb.com/game/search', 'http://bbs.ruliweb.com/family/212', 'http://bbs.ruliweb.com/family/242',
                     'http://bbs.ruliweb.com/family/232', 'http://bbs.ruliweb.com/family/211', 'http://bbs.ruliweb.com/family/249']

    # 중복게시물 처리를 위한 리스트
    tmp1 = []
    tmp2 = []
    tmp3 = []

    # postListTitle의 title을 하나씩 가져와서 리퀘스트 요청
    def start_requests(self):
        for title in self.postListTitle:
            yield scrapy.Request(title, self.parse_url)

    # 1차적으로 url받아와서 하위 url파싱(하위 게시판)
    def parse_url(self, response):
        for select in response.xpath('//ul[@class="sub_wrapper"]/li/a/@href'):
            if 'http://mypi.ruliweb.com/m/index_market.htm' in select.extract() \
                    or '/grb.htm' in select.extract() \
                    or '/list.htm' in select.extract() \
                    or '/310001' in select.extract() \
                    or '/310002' in select.extract():
                # 로그인이 필요하거나 파싱이 불필요한 게시판 필터링
                pass
            else:
                # 필터링 후 남은 url처리
                self.tmp1.append(select.extract()) # tmp1에 필터링 후 남은 url추가
                self.tmp2.append(select.extract().split('/')[-1]) # 필터링 후 중복되는 게시판을 처리하기위해 게시판 번호 추출

                for url_Last in self.tmp2: # 게시판번호를 기준으로 중복된 게시판은 한개만 저장
                    count = 0 # 중복게시판 중 최초 한개만 추출하기위한 변수
                    for url in self.tmp1:
                        if url_Last in url and count<1:
                            self.tmp3.append(url)
                            count += 1
                        else:
                            continue

        for url in set(self.tmp3): # 게시물 파싱을 위해 리퀘스트 요청
            for i in range(1,MAX_PAGE,1):
                URL = url + '/list?page={}'.format(i)
                yield scrapy.Request(URL)

    # 사이트 파싱
    def parse(self, response):
        for select in response.xpath('//tr[@class="table_body"]'):
            item = DamoaItem()

            item['source'] = self.name # 게시물 출처

            # 해당xpath 텍스트를 읽어와서 문자열로 바꾸고 item객체에 저장
            titleTmp = select.xpath('td[@class="subject"]/div[@class="relative"]/a/text()').extract()
            item['title'] = titleTmp

            # 링크 저장
            item['link'] = select.xpath('td/div[@class="relative"]/a/@href').extract()[0]

            # 게시판에 게시물 링크 타고가기 위해 리퀘스트 요청
            postUrl = BeautifulSoup(requests.get(item['link']).content, "html.parser")

            # 게시물로 이동후 속성읽어서 저장
            attributeTmp = select.xpath('td[@class="divsn"]/a/text()').extract()[0]
            item['attribute'] = attributeTmp

            # 게시일 저장
            dateTmp = "".join(postUrl.find(name="span", attrs={"class": "regdate"}).text.replace("(","").replace(")",""))
            item['date'] = datetime.strptime(dateTmp,'%Y.%m.%d %H:%M:%S').strftime('%Y-%m-%d %H:%M:%S')

            # 조회수 저장 -> 게시물 이동후 확인해야함
            hitsTmp1 = select.xpath('td[@class="hit"]/text()').extract()[0]
            hitsTmp2 = "".join(hitsTmp1).replace('\t','').replace('\n','').replace('\r','')
            item['hits'] = hitsTmp2

            # 추천수 저장 -> 공감수
            recommTmp1 = select.xpath('td[@class="recomd"]/text()').extract()[0]
            recommTmp2 = "".join(recommTmp1).replace('\t', '').replace('\n', '').replace('\r', '')
            item['recommened'] = recommTmp2

            # 마지막 갱신일 저장
            item['last_update'] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

            # 인기도 저장
            dateTmp_post = datetime.strptime(item['date'], '%Y-%m-%d %H:%M:%S')
            dateTmp_curr = datetime.strptime(datetime.now().strftime('%Y-%m-%d %H:%M:%S'), '%Y-%m-%d %H:%M:%S')

                # 한시간당 가중치 감소
            timeTmp = (dateTmp_curr-dateTmp_post).total_seconds()/3600

            if(timeTmp <= 0):
                timeTmp = 1
                commentTmp = int(item['recommened']) + ((int(item['hits']) / timeTmp))
            else :
                commentTmp = int(item['recommened']) + ((int(item['hits']) / timeTmp))

            item['pop'] = commentTmp

            # 게시물 텍스트 읽어서 문자열로 변환후 저장
            textTmp = postUrl.find(name="div", attrs={"class": "view_content"}).text.strip()
            item['text'] = "".join(textTmp).replace('\n', '')

            # item 누적
            if filterItem(item) != None:
                yield filterItem(item)



