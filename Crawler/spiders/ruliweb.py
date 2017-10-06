
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
            yield scrapy.Request("http://bbs.ruliweb.com/ps/board/300170/list?page={}".format(i))
            yield scrapy.Request("http://bbs.ruliweb.com/ps/board/300561/list?page={}".format(i))
            yield scrapy.Request("http://bbs.ruliweb.com/ps/board/300144/list?page={}".format(i))
            yield scrapy.Request("http://bbs.ruliweb.com/ps/board/300147/list?page={}".format(i))
            yield scrapy.Request("http://bbs.ruliweb.com/ps/board/300432/list?page={}".format(i))
            yield scrapy.Request("http://bbs.ruliweb.com/ps/board/300433/list?page={}".format(i))
            yield scrapy.Request("http://bbs.ruliweb.com/ps/board/300434/list?page={}".format(i))
            yield scrapy.Request("http://bbs.ruliweb.com/ps/board/300413/list?page={}".format(i))
            yield scrapy.Request("http://bbs.ruliweb.com/ps/board/300428/list?page={}".format(i))
            yield scrapy.Request("http://bbs.ruliweb.com/psp/board/300002/list?page={}".format(i))
            yield scrapy.Request("http://bbs.ruliweb.com/psp/board/300424/list?page={}".format(i))
            yield scrapy.Request("http://bbs.ruliweb.com/psp/board/300427/list?page={}".format(i))
            yield scrapy.Request("http://bbs.ruliweb.com/psp/board/300022/list?page={}".format(i))
            yield scrapy.Request("http://bbs.ruliweb.com/psp/board/300417/list?page={}".format(i))
            yield scrapy.Request("http://bbs.ruliweb.com/psp/board/300452/list?page={}".format(i))
            yield scrapy.Request("http://bbs.ruliweb.com/psp/board/300419/list?page={}".format(i))
            yield scrapy.Request("http://bbs.ruliweb.com/psp/board/300408/list?page={}".format(i))
            yield scrapy.Request("http://bbs.ruliweb.com/psp/board/300404/list?page={}".format(i))
            yield scrapy.Request("http://bbs.ruliweb.com/xbox/board/300003/list?page={}".format(i))
            yield scrapy.Request("http://bbs.ruliweb.com/xbox/board/300047/list?page={}".format(i))
            yield scrapy.Request("http://bbs.ruliweb.com/xbox/board/300046/list?page={}".format(i))
            yield scrapy.Request("http://bbs.ruliweb.com/xbox/board/300045/list?page={}".format(i))
            yield scrapy.Request("http://bbs.ruliweb.com/xbox/board/300024/list?page={}".format(i))
            yield scrapy.Request("http://bbs.ruliweb.com/xbox/board/300044/list?page={}".format(i))
            yield scrapy.Request("http://bbs.ruliweb.com/xbox/board/300025/list?page={}".format(i))
            yield scrapy.Request("http://bbs.ruliweb.com/xbox/board/300048/list?page={}".format(i))
            yield scrapy.Request("http://bbs.ruliweb.com/xbox/board/300407/list?page={}".format(i))
            yield scrapy.Request("http://bbs.ruliweb.com/xbox/board/300402/list?page={}".format(i))
            yield scrapy.Request("http://bbs.ruliweb.com/nin/board/300004/list?page={}".format(i))
            yield scrapy.Request("http://bbs.ruliweb.com/nin/board/300051/list?page={}".format(i))
            yield scrapy.Request("http://bbs.ruliweb.com/nin/board/300050/list?page={}".format(i))
            yield scrapy.Request("http://bbs.ruliweb.com/nin/board/300049/list?page={}".format(i))
            yield scrapy.Request("http://bbs.ruliweb.com/nin/board/300027/list?page={}".format(i))
            yield scrapy.Request("http://bbs.ruliweb.com/nin/board/300028/list?page={}".format(i))
            yield scrapy.Request("http://bbs.ruliweb.com/nin/board/300052/list?page={}".format(i))
            yield scrapy.Request("http://bbs.ruliweb.com/nin/board/300405/list?page={}".format(i))
            yield scrapy.Request("http://bbs.ruliweb.com/nin/board/300400/list?page={}".format(i))
            yield scrapy.Request("http://bbs.ruliweb.com/nds/board/300005/list?page={}".format(i))
            yield scrapy.Request("http://bbs.ruliweb.com/nds/board/300056/list?page={}".format(i))
            yield scrapy.Request("http://bbs.ruliweb.com/nds/board/300055/list?page={}".format(i))
            yield scrapy.Request("http://bbs.ruliweb.com/nds/board/300054/list?page={}".format(i))
            yield scrapy.Request("http://bbs.ruliweb.com/nds/board/300053/list?page={}".format(i))
            yield scrapy.Request("http://bbs.ruliweb.com/nds/board/300403/list?page={}".format(i))
            yield scrapy.Request("http://bbs.ruliweb.com/nds/board/300057/list?page={}".format(i))
            yield scrapy.Request("http://bbs.ruliweb.com/nds/board/300409/list?page={}".format(i))
            yield scrapy.Request("http://bbs.ruliweb.com/nds/board/300449/list?page={}".format(i))
            yield scrapy.Request("http://bbs.ruliweb.com/pc/board/300006/list?page={}".format(i))
            yield scrapy.Request("http://bbs.ruliweb.com/pc/board/300007/list?page={}".format(i))
            yield scrapy.Request("http://bbs.ruliweb.com/pc/board/300058/list?page={}".format(i))
            yield scrapy.Request("http://bbs.ruliweb.com/pc/board/300425/list?page={}".format(i))
            yield scrapy.Request("http://bbs.ruliweb.com/pc/board/300461/list?page={}".format(i))
            yield scrapy.Request("http://bbs.ruliweb.com/pc/board/300410/list?page={}".format(i))
            yield scrapy.Request("http://bbs.ruliweb.com/pc/board/300142/list?page={}".format(i))
            yield scrapy.Request("http://bbs.ruliweb.com/pc/board/1007/list?page={}".format(i))
            yield scrapy.Request("http://bbs.ruliweb.com/pc/board/320019/list?page={}".format(i))
            yield scrapy.Request("http://bbs.ruliweb.com/pc/board/320023/list?page={}".format(i))
            yield scrapy.Request("http://bbs.ruliweb.com/pc/board/320025/list?page={}".format(i))
            yield scrapy.Request("http://bbs.ruliweb.com/pc/board/320027/list?page={}".format(i))
            yield scrapy.Request("http://bbs.ruliweb.com/pc/board/320032/list?page={}".format(i))
            yield scrapy.Request("http://bbs.ruliweb.com/pc/board/300535/list?page={}".format(i))
            yield scrapy.Request("http://bbs.ruliweb.com/pc/board/300534/list?page={}".format(i))
            yield scrapy.Request("http://bbs.ruliweb.com/pc/board/300538/list?page={}".format(i))
            yield scrapy.Request("http://bbs.ruliweb.com/pc/board/1003/list?page={}".format(i))
            yield scrapy.Request("http://bbs.ruliweb.com/mobile/board/1004/list?page={}".format(i))
            yield scrapy.Request("http://bbs.ruliweb.com/mobile/board/300008/list?page={}".format(i))
            yield scrapy.Request("http://bbs.ruliweb.com/mobile/board/300009/list?page={}".format(i))
            yield scrapy.Request("http://bbs.ruliweb.com/mobile/board/300010/list?page={}".format(i))
            yield scrapy.Request("http://bbs.ruliweb.com/mobile/board/600002/list?page={}".format(i))
            yield scrapy.Request("http://bbs.ruliweb.com/mobile/board/300034/list?page={}".format(i))
            yield scrapy.Request("http://bbs.ruliweb.com/mobile/board/300059/list?page={}".format(i))
            yield scrapy.Request("http://bbs.ruliweb.com/mobile/board/300141/list?page={}".format(i))
            yield scrapy.Request("http://bbs.ruliweb.com/mobile/board/300536/list?page={}".format(i))
            yield scrapy.Request("http://bbs.ruliweb.com/mobile/board/300540/list?page={}".format(i))
            yield scrapy.Request("http://bbs.ruliweb.com/mobile/board/320001/list?page={}".format(i))
            yield scrapy.Request("http://bbs.ruliweb.com/mobile/board/320008/list?page={}".format(i))
            yield scrapy.Request("http://bbs.ruliweb.com/mobile/board/320048/list?page={}".format(i))
            yield scrapy.Request("http://bbs.ruliweb.com/mobile/board/300036/list?page={}".format(i))
            yield scrapy.Request("http://bbs.ruliweb.com/mobile/board/300035/list?page={}".format(i))
            yield scrapy.Request("http://bbs.ruliweb.com/av/board/300011/list?page={}".format(i))
            yield scrapy.Request("http://bbs.ruliweb.com/av/board/300013/list?page={}".format(i))
            yield scrapy.Request("http://bbs.ruliweb.com/av/board/300231/list?page={}".format(i))
            yield scrapy.Request("http://bbs.ruliweb.com/av/board/320035/list?page={}".format(i))
            yield scrapy.Request("http://bbs.ruliweb.com/av/board/320036/list?page={}".format(i))
            yield scrapy.Request("http://bbs.ruliweb.com/av/board/320033/list?page={}".format(i))
            yield scrapy.Request("http://bbs.ruliweb.com/av/board/300041/list?page={}".format(i))
            yield scrapy.Request("http://bbs.ruliweb.com/av/board/300040/list?page={}".format(i))
            # yield scrapy.Request("http://bbs.ruliweb.com/av/board/300011/list?page={}".format(i))
            # yield scrapy.Request("http://bbs.ruliweb.com/av/board/300011/list?page={}".format(i))
            # yield scrapy.Request("http://bbs.ruliweb.com/av/board/300011/list?page={}".format(i))
            # yield scrapy.Request("http://bbs.ruliweb.com/av/board/300011/list?page={}".format(i))














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



