
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

    # postListTitle의 title을 하나씩 가져와서 리퀘스트 요청
    def start_requests(self):
        for i in range(1, MAX_PAGE, 1):
            yield scrapy.Request("http://bbs.ruliweb.com/ps/board/300001/list?page={}".format(i))
            yield scrapy.Request("http://bbs.ruliweb.com/ps/board/1020/list?page={}".format(i))
            yield scrapy.Request("http://bbs.ruliweb.com/ps/board/300421/list?page={}".format(i))
            yield scrapy.Request("http://bbs.ruliweb.com/ps/board/300423/list?page={}".format(i))
            yield scrapy.Request("http://bbs.ruliweb.com/ps/board/300426/list?page={}".format(i))
            yield scrapy.Request("http://bbs.ruliweb.com/ps/board/300019/list?page={}".format(i))
            yield scrapy.Request("http://bbs.ruliweb.com/ps/board/300549/list?page={}".format(i))
            yield scrapy.Request("http://bbs.ruliweb.com/ps/board/300416/list?page={}".format(i))
            yield scrapy.Request("http://bbs.ruliweb.com/ps/board/300021/list?page={}".format(i))
            yield scrapy.Request("http://bbs.ruliweb.com/ps/board/299999/list?page={}".format(i))
            yield scrapy.Request("http://bbs.ruliweb.com/ps/board/299998/list?page={}".format(i))
            yield scrapy.Request("http://bbs.ruliweb.com/ps/board/300496/list?page={}".format(i))
            yield scrapy.Request("http://bbs.ruliweb.com/ps/board/300537/list?page={}".format(i))
            yield scrapy.Request("http://bbs.ruliweb.com/ps/board/320105/list?page={}".format(i))
            yield scrapy.Request("http://bbs.ruliweb.com/ps/board/300418/list?page={}".format(i))
            yield scrapy.Request("http://bbs.ruliweb.com/ps/board/300406/list?page={}".format(i))
            yield scrapy.Request("http://bbs.ruliweb.com/ps/board/300401/list?page={}".format(i))
            yield scrapy.Request("http://bbs.ruliweb.com/ps/board/300152/list?cate=1&page={}".format(i))
            yield scrapy.Request("http://bbs.ruliweb.com/ps/board/300143/list?cate=2&page={}".format(i))
            yield scrapy.Request("http://bbs.ruliweb.com/ps/board/300145/list?page={}".format(i))
            # yield scrapy.Request("http://bbs.ruliweb.com/ps/board/300001/list?page={}".format(i))
            # yield scrapy.Request("http://bbs.ruliweb.com/ps/board/300001/list?page={}".format(i))
            # yield scrapy.Request("http://bbs.ruliweb.com/ps/board/300001/list?page={}".format(i))
            # yield scrapy.Request("http://bbs.ruliweb.com/ps/board/300001/list?page={}".format(i))
            # yield scrapy.Request("http://bbs.ruliweb.com/ps/board/300001/list?page={}".format(i))
            # yield scrapy.Request("http://bbs.ruliweb.com/ps/board/300001/list?page={}".format(i))
            # yield scrapy.Request("http://bbs.ruliweb.com/ps/board/300001/list?page={}".format(i))s



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



