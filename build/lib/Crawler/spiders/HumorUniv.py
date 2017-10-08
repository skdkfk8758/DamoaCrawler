
"""
웃긴대학 크롤링 스파이더

클리앙 게시물 별로 크롤링

2017.10.06
 - 스파이더 이름 변경 humiruniv -> humor

"""

import scrapy

import requests
from bs4 import BeautifulSoup
from scrapy.selector import Selector

from Crawler.filterItem import *
from Crawler.items import DamoaItem
from Crawler.spiders.Setting import *


class HumorUniv(scrapy.Spider):
    name = 'humor'

    # 리퀘스트 요청 (여러 게시판 돌때 동기적으로 수행됨)
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

    # 사이트 파싱
    def parse_site(self, response):
        sel = Selector(response)

        for parse_path in sel.xpath('//div[@id="cnts_list_new"]/div/table/tr'):
            item = DamoaItem()

            item['source'] = "humoruniv"

            # 해당xpath 텍스트를 읽어와서 문자열로 바꾸고 item객체에 저장
            titleTmp = parse_path.xpath('td[@class="li_sbj"]/a/text()').extract()
            tmpList_title = "".join(titleTmp).replace('\t', '').replace('\r', '').replace('\n','')

            item['title'] = tmpList_title

            # 링크 저장
            tmp = parse_path.xpath('td[@class="li_sbj"]/a/@href').extract()

            if len(tmp)>0:
                part_link = parse_path.xpath('td[@class="li_sbj"]/a/@href').extract()[0]
            else:
                continue
            item['link'] = 'http://web.humoruniv.com/board/humor/' + part_link

            # 게시판에 게시물 링크 타고가기 위해 리퀘스트 재요청
            postUrl = BeautifulSoup(requests.get(item['link']).content, "html.parser",from_encoding='CP949')

            # 게시물로 이동후 속성읽어서 저장
            attributeTmp = postUrl.find(name='a', attrs={"class" : "bo"}).text.strip()
            item['attribute'] = attributeTmp

            # 게시일 저장
            tmpdate = parse_path.xpath('td[@class="li_date"]/span/text()').extract()
            # item['date'] = ' '.join(tmpdate) + ":00"

            if '2017' not in ' '.join(tmpdate) + ":00":
                item['date'] = '20'+ ' '.join(tmpdate) + ":00"
            else:
                item['date'] = ' '.join(tmpdate) + ":00"

            # 조회수 저장 -> 게시물 이동후 확인해야함
            hitsTmp = parse_path.xpath('td[@class="li_und"]/text()').extract()
            item['hits'] = "".join(hitsTmp).replace('\t', '').replace('\r', '').replace('\n','').replace('/','').replace(',','').strip()

            # 추천수 저장
            recommTmp = parse_path.xpath('td[@class="li_und"]/span[@class="o"]/text()').extract()
            item['recommened'] = "".join(recommTmp).replace('\t', '').replace('\r', '').replace('\n', '').replace('/', '')

            # 마지막 갱신일 저장
            item['last_update'] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

            # 인기도 저장
            dateTmp_post = datetime.strptime(item['date'], '%Y-%m-%d %H:%M:%S')
            dateTmp_curr = datetime.strptime(datetime.now().strftime('%Y-%m-%d %H:%M:%S'), '%Y-%m-%d %H:%M:%S')

            # 한시간당 가중치 감소(시간으로 조회수 나눔)
            timeTmp = (dateTmp_curr-dateTmp_post).total_seconds()/3600

            if(timeTmp <= 0):
                timeTmp = 1
                commentTmp = int(item['recommened']) + ((int(item['hits']) / timeTmp))
            else :
                commentTmp = int(item['recommened']) + ((int(item['hits']) / timeTmp))

            popTmp = commentTmp
            item['pop'] = popTmp

            # 게시물 텍스트 읽어서 문자열로 변환후 저장
            textTmp = postUrl.find(name="div", attrs={"id":"cnts"}).text.strip()
            postText = "".join(textTmp).replace('\n','')
            item['text'] = postText

            if filterItem(item) != None:
                yield filterItem(item)

