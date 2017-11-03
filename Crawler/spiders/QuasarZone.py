
"""
퀘이사존 Spider
Create :  2017.10.21

MAX_PAGE -> Damoa.spiders.Setting에 있음

"""

import scrapy

from Crawler.filterItem import *
from Crawler.items import DamoaItem
from Crawler.spiders.Setting import *
from Crawler.CreateItem import *

class Spider(scrapy.Spider):
    name = 'quasarzone' # spider name

    def start_requests(self):
        for i in range(1, MAX_PAGE, 1):
            yield scrapy.Request("http://quasarzone.co.kr/bbs/board.php?bo_table=qn_game&sca=PC%EA%B2%8C%EC%9E%84&page={}".format(i))
            yield scrapy.Request("http://quasarzone.co.kr/bbs/board.php?bo_table=qn_game&sca=%EC%BD%98%EC%86%94%EA%B2%8C%EC%9E%84&page={}".format(i))
            yield scrapy.Request("http://quasarzone.co.kr/bbs/board.php?bo_table=qn_game&sca=%EB%A9%80%ED%8B%B0%ED%94%8C%EB%9E%AB%ED%8F%BC&page={}".format(i))
            yield scrapy.Request("http://quasarzone.co.kr/bbs/board.php?bo_table=qn_game&sca=%EC%97%85%EA%B3%84%EB%8F%99%ED%96%A5&page={}".format(i))
            yield scrapy.Request("http://quasarzone.co.kr/bbs/board.php?bo_table=qn_game&sca=%EA%B8%B0%ED%83%80&page={}".format(i))
            yield scrapy.Request("http://quasarzone.co.kr/bbs/board.php?bo_table=qn_hardware&sca=CPU%2FMB%2FRAM&page={}".format(i))
            yield scrapy.Request("http://quasarzone.co.kr/bbs/board.php?bo_table=qn_hardware&sca=%EA%B7%B8%EB%9E%98%ED%94%BD%EC%B9%B4%EB%93%9C&page={}".format(i))
            yield scrapy.Request("http://quasarzone.co.kr/bbs/board.php?bo_table=qn_hardware&sca=케이스&page={}".format(i))
            yield scrapy.Request("http://quasarzone.co.kr/bbs/board.php?bo_table=qn_hardware&sca=%EC%BF%A8%EB%A7%81%EC%86%94%EB%A3%A8%EC%85%98&page={}".format(i))
            yield scrapy.Request("http://quasarzone.co.kr/bbs/board.php?bo_table=qn_hardware&sca=%EC%A0%80%EC%9E%A5%EC%9E%A5%EC%B9%98&page={}".format(i))
            yield scrapy.Request("http://quasarzone.co.kr/bbs/board.php?bo_table=qn_hardware&sca=%ED%8C%8C%EC%9B%8C&page={}".format(i))
            yield scrapy.Request("http://quasarzone.co.kr/bbs/board.php?bo_table=qn_hardware&sca=%ED%82%A4%EB%B3%B4%EB%93%9C%2F%EB%A7%88%EC%9A%B0%EC%8A%A4&page={}".format(i))
            yield scrapy.Request("http://quasarzone.co.kr/bbs/board.php?bo_table=qn_hardware&sca=%EC%9D%8C%ED%96%A5%EA%B8%B0%EA%B8%B0&page={}".format(i))
            yield scrapy.Request("http://quasarzone.co.kr/bbs/board.php?bo_table=qn_hardware&sca=%EB%94%94%EC%8A%A4%ED%94%8C%EB%A0%88%EC%9D%B4&page={}".format(i))
            yield scrapy.Request("http://quasarzone.co.kr/bbs/board.php?bo_table=qn_hardware&sca=%EC%86%8C%ED%94%84%ED%8A%B8%EC%9B%A8%EC%96%B4&page={}".format(i))
            yield scrapy.Request("http://quasarzone.co.kr/bbs/board.php?bo_table=qn_hardware&sca=%EB%85%B8%ED%8A%B8%EB%B6%81&page={}".format(i))
            yield scrapy.Request("http://quasarzone.co.kr/bbs/board.php?bo_table=qn_hardware&sca=%EC%97%85%EA%B3%84%EB%8F%99%ED%96%A5&page={}".format(i))
            yield scrapy.Request("http://quasarzone.co.kr/bbs/board.php?bo_table=qn_hardware&sca=%EA%B8%B0%ED%83%80%2F%EC%A3%BC%EB%B3%80%EA%B8%B0%EA%B8%B0&page={}".format(i))
            yield scrapy.Request("http://quasarzone.co.kr/bbs/board.php?bo_table=qn_mobile&sca=%EC%95%A0%ED%94%8C&page={}".format(i))
            yield scrapy.Request("http://quasarzone.co.kr/bbs/board.php?bo_table=qn_mobile&sca=%EC%95%88%EB%93%9C%EB%A1%9C%EC%9D%B4%EB%93%9C&page={}".format(i))
            yield scrapy.Request("http://quasarzone.co.kr/bbs/board.php?bo_table=qn_mobile&sca=%EC%9C%88%EB%8F%84%EC%9A%B0&page={}".format(i))
            yield scrapy.Request("http://quasarzone.co.kr/bbs/board.php?bo_table=qn_mobile&sca=%EC%A3%BC%EB%B3%80%EA%B8%B0%EA%B8%B0&page={}".format(i))
            yield scrapy.Request("http://quasarzone.co.kr/bbs/board.php?bo_table=qn_mobile&sca=%EC%97%85%EA%B3%84%EB%8F%99%ED%96%A5&page={}".format(i))
            yield scrapy.Request("http://quasarzone.co.kr/bbs/board.php?bo_table=qn_mobile&sca=%EA%B8%B0%ED%83%80&page={}".format(i))
            yield scrapy.Request("http://quasarzone.co.kr/bbs/board.php?bo_table=qf_hwjoin&sca=%EC%9E%A1%EB%8B%B4&page={}".format(i))
            yield scrapy.Request("http://quasarzone.co.kr/bbs/board.php?bo_table=qf_hwjoin&sca=%EC%A7%88%EB%AC%B8&page={}".format(i))
            yield scrapy.Request("http://quasarzone.co.kr/bbs/board.php?bo_table=qf_pcgame&sca=%EC%9E%A1%EB%8B%B4&page={}".format(i))
            yield scrapy.Request("http://quasarzone.co.kr/bbs/board.php?bo_table=qf_pcgame&sca=%EC%A7%88%EB%AC%B8&page={}".format(i))
            yield scrapy.Request("http://quasarzone.co.kr/bbs/board.php?bo_table=qf_pcgame&sca=%EC%A0%95%EB%B3%B4&page={}".format(i))
            yield scrapy.Request("http://quasarzone.co.kr/bbs/board.php?bo_table=qf_console&sca=%EC%9E%A1%EB%8B%B4&page={}".format(i))
            yield scrapy.Request("http://quasarzone.co.kr/bbs/board.php?bo_table=qf_mobile&sca=%EC%9E%A1%EB%8B%B4&page={}".format(i))
            yield scrapy.Request("http://quasarzone.co.kr/bbs/board.php?bo_table=qf_mobile&sca=%EC%A7%88%EB%AC%B8&page={}".format(i))
            yield scrapy.Request("http://quasarzone.co.kr/bbs/board.php?bo_table=qf_mobile&sca=%EC%A0%95%EB%B3%B4&page={}".format(i))
            yield scrapy.Request("http://quasarzone.co.kr/bbs/board.php?bo_table=qf_cmr&sca=%EC%9E%A1%EB%8B%B4&page={}".format(i))
            yield scrapy.Request("http://quasarzone.co.kr/bbs/board.php?bo_table=qf_cmr&sca=%EC%A7%88%EB%AC%B8&page={}".format(i))
            yield scrapy.Request("http://quasarzone.co.kr/bbs/board.php?bo_table=qf_cmr&sca=%EC%A0%95%EB%B3%B4&page={}".format(i))
            yield scrapy.Request("http://quasarzone.co.kr/bbs/board.php?bo_table=qf_vga&sca=%EC%9E%A1%EB%8B%B4&page={}".format(i))
            yield scrapy.Request("http://quasarzone.co.kr/bbs/board.php?bo_table=qf_vga&sca=%EC%A7%88%EB%AC%B8&page={}".format(i))
            yield scrapy.Request("http://quasarzone.co.kr/bbs/board.php?bo_table=qf_vga&sca=%EC%A0%95%EB%B3%B4&page={}".format(i))
            yield scrapy.Request("http://quasarzone.co.kr/bbs/board.php?bo_table=qf_case&sca=%EC%9E%A1%EB%8B%B4&page={}".format(i))
            yield scrapy.Request("http://quasarzone.co.kr/bbs/board.php?bo_table=qf_case&sca=%EC%A7%88%EB%AC%B8&page={}".format(i))
            yield scrapy.Request("http://quasarzone.co.kr/bbs/board.php?bo_table=qf_case&sca=%EC%A0%95%EB%B3%B4&page={}".format(i))
            yield scrapy.Request("http://quasarzone.co.kr/bbs/board.php?bo_table=qf_cool&sca=%EC%9E%A1%EB%8B%B4&page={}".format(i))
            yield scrapy.Request("http://quasarzone.co.kr/bbs/board.php?bo_table=qf_cool&sca=%EC%A7%88%EB%AC%B8&page={}".format(i))
            yield scrapy.Request("http://quasarzone.co.kr/bbs/board.php?bo_table=qf_cool&sca=%EC%A0%95%EB%B3%B4&page={}".format(i))
            yield scrapy.Request("http://quasarzone.co.kr/bbs/board.php?bo_table=qf_storage&page={}".format(i))
            yield scrapy.Request("http://quasarzone.co.kr/bbs/board.php?bo_table=qf_power&page={}".format(i))
            yield scrapy.Request("http://quasarzone.co.kr/bbs/board.php?bo_table=qf_input&sca=%EC%9E%A1%EB%8B%B4&page={}".format(i))
            yield scrapy.Request("http://quasarzone.co.kr/bbs/board.php?bo_table=qf_input&sca=%EC%A7%88%EB%AC%B8&page={}".format(i))
            yield scrapy.Request("http://quasarzone.co.kr/bbs/board.php?bo_table=qf_input&sca=%EC%A0%95%EB%B3%B4&page={}".format(i))
            yield scrapy.Request("http://quasarzone.co.kr/bbs/board.php?bo_table=qf_sound&sca=%EC%9E%A1%EB%8B%B4&page={}".format(i))
            yield scrapy.Request("http://quasarzone.co.kr/bbs/board.php?bo_table=qf_sound&sca=%EC%A7%88%EB%AC%B8&page={}".format(i))
            yield scrapy.Request("http://quasarzone.co.kr/bbs/board.php?bo_table=qf_dp&sca=%EC%9E%A1%EB%8B%B4&page={}".format(i))
            yield scrapy.Request("http://quasarzone.co.kr/bbs/board.php?bo_table=qf_dp&sca=%EC%A7%88%EB%AC%B8&page={}".format(i))
            yield scrapy.Request("http://quasarzone.co.kr/bbs/board.php?bo_table=qf_net&page={}".format(i))
            yield scrapy.Request("http://quasarzone.co.kr/bbs/board.php?bo_table=qf_sw&sca=%EC%9E%A1%EB%8B%B4&page={}".format(i))
            yield scrapy.Request("http://quasarzone.co.kr/bbs/board.php?bo_table=qf_sw&sca=%EC%A7%88%EB%AC%B8&page={}".format(i))
            yield scrapy.Request("http://quasarzone.co.kr/bbs/board.php?bo_table=qf_sw&sca=%EC%A0%95%EB%B3%B4&page={}".format(i))
            yield scrapy.Request("http://quasarzone.co.kr/bbs/board.php?bo_table=qf_nb&page={}".format(i))
            yield scrapy.Request("http://quasarzone.co.kr/bbs/board.php?bo_table=qf_etc&page={}".format(i))
            yield scrapy.Request("http://quasarzone.co.kr/bbs/board.php?bo_table=qb_free&page={}".format(i))
            yield scrapy.Request("http://quasarzone.co.kr/bbs/board.php?bo_table=qb_humor&page={}".format(i))
            yield scrapy.Request("http://quasarzone.co.kr/bbs/board.php?bo_table=qb_figure&page={}".format(i))
            yield scrapy.Request("http://quasarzone.co.kr/bbs/board.php?bo_table=qb_sport&page={}".format(i))
            yield scrapy.Request("http://quasarzone.co.kr/bbs/board.php?bo_table=qb_tip&page={}".format(i))
            yield scrapy.Request("http://quasarzone.co.kr/bbs/board.php?bo_table=qb_saleinfo&sca=%ED%95%98%EB%93%9C%EC%9B%A8%EC%96%B4&page={}".format(i))
            yield scrapy.Request("http://quasarzone.co.kr/bbs/board.php?bo_table=qb_saleinfo&sca=%EA%B2%8C%EC%9E%84&page={}".format(i))
            yield scrapy.Request("http://quasarzone.co.kr/bbs/board.php?bo_table=qb_give&page={}".format(i))

    def parse(self, response):
        for select in response.xpath("//ul[@class='list-body']/li"):
            item = DamoaItem() # item객체 생성

            item['source'] = self.name

            if createItemUseXpath(select, "div[@class='wr-category fs11 hidden-xs']/text()", texttype="")== "":
                # 공지사항 패스
                continue
            else:
                titleXpath = "div[@class='wr-subject']/a/text()"
                item['title'] = createItemUseXpath(select, titleXpath, texttype="").strip()

                linkXpath = "div[@class='wr-subject']/a/@href"
                item['link'] = createItemUseXpath(select, linkXpath, texttype=TextType.LINK).strip()

                attrXpath = "div[@class='wr-category fs11 hidden-xs']/text()"
                item['attribute'] = createItemUseXpath(select, attrXpath, texttype="")

                tagName = "span"
                tagAttr = {"itemprop": "datePublished"}
                item['date'] = "".join(createItemUseBs4(item['link'], tagName, tagAttr, texttype=TextType.DATE, encoding="utf8")) + ":00"

                hitsXpath = "div[@class='wr-hit fs11 hidden-xs']/text()"
                item['hits'] = createItemUseXpath(select, hitsXpath, texttype=TextType.INT)

                recoXpath = "div[@class='wr-good count_good fs11 hidden-xs']/text()"
                item['recommened'] = createItemUseXpath(select, recoXpath, texttype=TextType.INT).strip()

                item['last_update'] = getCurrentTime(TextType.STRING)

                item['pop'] = createItem_pop(item['date'], item['recommened'], item['hits'])

                tagName = "div"
                tagAttrs = {"class": "view-content"}
                if createItemUseBs4(item['link'], tagName, tagAttrs, encoding="utf8", texttype=TextType.TEXT) == "":
                    item['text'] = "None Text"
                else:
                    item['text'] = createItemUseBs4(item['link'], tagName, tagAttrs, encoding="utf8", texttype=TextType.TEXT)

            item['image'] = createItemUseBs4_PostImage(item['link'], "data/editor")

            yield item



