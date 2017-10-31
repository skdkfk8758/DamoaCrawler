
"""
Ruliweb Spider
Create : 2017.06.16

MAX_PAGE -> DamoaCrawler.spiders.spider_Setting에 있음

2017.10.06
 - 게시판 리스트 업데이트

2017.10.09
 - 코드정리

"""

import scrapy

from Crawler.filterItem import *
from Crawler.items import DamoaItem
from Crawler.spiders.Setting import *
from Crawler.CreateItem import *

class Spider(scrapy.Spider):
    name = 'ruli' # spider name

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
            yield scrapy.Request("http://bbs.ruliweb.com/sports/board/300276/list?page={}".format(i))
            yield scrapy.Request("http://bbs.ruliweb.com/sports/board/300446/list?page={}".format(i))
            yield scrapy.Request("http://bbs.ruliweb.com/sports/board/300248/list?page={}".format(i))
            yield scrapy.Request("http://bbs.ruliweb.com/sports/board/300253/list?page={}".format(i))
            yield scrapy.Request("http://bbs.ruliweb.com/sports/board/300254/list?page={}".format(i))
            yield scrapy.Request("http://bbs.ruliweb.com/sports/board/300252/list?page={}".format(i))
            yield scrapy.Request("http://bbs.ruliweb.com/sports/board/300250/list?page={}".format(i))
            yield scrapy.Request("http://bbs.ruliweb.com/sports/board/300251/list?page={}".format(i))
            yield scrapy.Request("http://bbs.ruliweb.com/sports/board/300247/list?page={}".format(i))
            yield scrapy.Request("http://bbs.ruliweb.com/sports/board/300249/list?page={}".format(i))
            yield scrapy.Request("http://bbs.ruliweb.com/sports/board/300256/list?page={}".format(i))
            yield scrapy.Request("http://bbs.ruliweb.com/sports/board/300257/list?page={}".format(i))
            yield scrapy.Request("http://bbs.ruliweb.com/sports/board/300258/list?page={}".format(i))
            yield scrapy.Request("http://bbs.ruliweb.com/sports/board/300255/list?page={}".format(i))
            yield scrapy.Request("http://bbs.ruliweb.com/sports/board/300310/list?page={}".format(i))
            yield scrapy.Request("http://bbs.ruliweb.com/sports/board/300301/list?page={}".format(i))
            yield scrapy.Request("http://bbs.ruliweb.com/sports/board/300302/list?page={}".format(i))
            yield scrapy.Request("http://bbs.ruliweb.com/sports/board/300306/list?page={}".format(i))
            yield scrapy.Request("http://bbs.ruliweb.com/sports/board/300304/list?page={}".format(i))
            yield scrapy.Request("http://bbs.ruliweb.com/sports/board/300497/list?page={}".format(i))
            yield scrapy.Request("http://bbs.ruliweb.com/sports/board/300305/list?page={}".format(i))
            yield scrapy.Request("http://bbs.ruliweb.com/sports/board/300303/list?page={}".format(i))
            yield scrapy.Request("http://bbs.ruliweb.com/sports/board/300565/list?page={}".format(i))
            yield scrapy.Request("http://bbs.ruliweb.com/sports/board/300309/list?page={}".format(i))
            yield scrapy.Request("http://bbs.ruliweb.com/sports/board/300300/list?page={}".format(i))
            yield scrapy.Request("http://bbs.ruliweb.com/sports/board/300307/list?page={}".format(i))
            yield scrapy.Request("http://bbs.ruliweb.com/hobby/board/300116/list?page={}".format(i))
            yield scrapy.Request("http://bbs.ruliweb.com/hobby/board/300228/list?page={}".format(i))
            yield scrapy.Request("http://bbs.ruliweb.com/hobby/board/600001/list?page={}".format(i))
            yield scrapy.Request("http://bbs.ruliweb.com/hobby/board/300431/list?page={}".format(i))
            yield scrapy.Request("http://bbs.ruliweb.com/hobby/board/300109/list?page={}".format(i))
            yield scrapy.Request("http://bbs.ruliweb.com/hobby/board/300110/list?page={}".format(i))
            yield scrapy.Request("http://bbs.ruliweb.com/hobby/board/300111/list?page={}".format(i))
            yield scrapy.Request("http://bbs.ruliweb.com/hobby/board/300112/list?page={}".format(i))
            yield scrapy.Request("http://bbs.ruliweb.com/hobby/board/300113/list?page={}".format(i))
            yield scrapy.Request("http://bbs.ruliweb.com/hobby/board/300100/list?page={}".format(i))
            yield scrapy.Request("http://bbs.ruliweb.com/hobby/board/300261/list?page={}".format(i))
            yield scrapy.Request("http://bbs.ruliweb.com/hobby/board/300260/list?page={}".format(i))
            yield scrapy.Request("http://bbs.ruliweb.com/hobby/board/300310/list?page={}".format(i))
            yield scrapy.Request("http://bbs.ruliweb.com/hobby/board/300104/list?page={}".format(i))
            yield scrapy.Request("http://bbs.ruliweb.com/hobby/board/300572/list?page={}".format(i))
            yield scrapy.Request("http://bbs.ruliweb.com/hobby/board/300117/list?page={}".format(i))
            yield scrapy.Request("http://bbs.ruliweb.com/hobby/board/300114/list?page={}".format(i))
            yield scrapy.Request("http://bbs.ruliweb.com/hobby/board/300095/list?page={}".format(i))
            yield scrapy.Request("http://bbs.ruliweb.com/hobby/board/300227/list?page={}".format(i))
            yield scrapy.Request("http://bbs.ruliweb.com/hobby/board/300225/list?page={}".format(i))
            yield scrapy.Request("http://bbs.ruliweb.com/hobby/board/300226/list?page={}".format(i))
            yield scrapy.Request("http://bbs.ruliweb.com/hobby/board/300176/list?page={}".format(i))
            yield scrapy.Request("http://bbs.ruliweb.com/hobby/board/320047/list?page={}".format(i))
            yield scrapy.Request("http://bbs.ruliweb.com/hobby/board/320042/list?page={}".format(i))
            yield scrapy.Request("http://bbs.ruliweb.com/hobby/board/320046/list?page={}".format(i))
            yield scrapy.Request("http://bbs.ruliweb.com/hobby/board/300118/list?page={}".format(i))
            yield scrapy.Request("http://bbs.ruliweb.com/hobby/board/300082/list?page={}".format(i))
            yield scrapy.Request("http://bbs.ruliweb.com/hobby/board/300083/list?page={}".format(i))
            yield scrapy.Request("http://bbs.ruliweb.com/hobby/board/300080/list?page={}".format(i))
            yield scrapy.Request("http://bbs.ruliweb.com/hobby/board/320045/list?page={}".format(i))
            yield scrapy.Request("http://bbs.ruliweb.com/hobby/board/300087/list?page={}".format(i))
            yield scrapy.Request("http://bbs.ruliweb.com/hobby/board/500021/list?page={}".format(i))
            yield scrapy.Request("http://bbs.ruliweb.com/hobby/board/300086/list?page={}".format(i))
            yield scrapy.Request("http://bbs.ruliweb.com/hobby/board/300092/list?page={}".format(i))
            yield scrapy.Request("http://bbs.ruliweb.com/hobby/board/320040/list?page={}".format(i))
            yield scrapy.Request("http://bbs.ruliweb.com/hobby/board/300075/list?page={}".format(i))
            yield scrapy.Request("http://bbs.ruliweb.com/hobby/board/300076/list?page={}".format(i))
            yield scrapy.Request("http://bbs.ruliweb.com/hobby/board/300489/list?page={}".format(i))
            yield scrapy.Request("http://bbs.ruliweb.com/hobby/board/300098/list?page={}".format(i))
            yield scrapy.Request("http://bbs.ruliweb.com/hobby/board/320048/list?page={}".format(i))
            yield scrapy.Request("http://bbs.ruliweb.com/hobby/board/320008/list?page={}".format(i))
            yield scrapy.Request("http://bbs.ruliweb.com/hobby/board/320001/list?page={}".format(i))
            yield scrapy.Request("http://bbs.ruliweb.com/hobby/board/320033/list?page={}".format(i))
            yield scrapy.Request("http://bbs.ruliweb.com/hobby/board/320036/list?page={}".format(i))
            yield scrapy.Request("http://bbs.ruliweb.com/hobby/board/300041/list?page={}".format(i))
            yield scrapy.Request("http://bbs.ruliweb.com/hobby/board/320035/list?page={}".format(i))
            yield scrapy.Request("http://bbs.ruliweb.com/hobby/board/320039/list?page={}".format(i))
            yield scrapy.Request("http://bbs.ruliweb.com/hobby/board/300040/list?page={}".format(i))
            yield scrapy.Request("http://bbs.ruliweb.com/hobby/board/500022/list?page={}".format(i))
            yield scrapy.Request("http://bbs.ruliweb.com/hobby/board/320044/list?page={}".format(i))
            yield scrapy.Request("http://bbs.ruliweb.com/hobby/board/300182/list?page={}".format(i))
            yield scrapy.Request("http://bbs.ruliweb.com/hobby/board/300513/list?page={}".format(i))
            yield scrapy.Request("http://bbs.ruliweb.com/hobby/board/320043/list?page={}".format(i))
            yield scrapy.Request("http://bbs.ruliweb.com/hobby/board/300246/list?page={}".format(i))
            yield scrapy.Request("http://bbs.ruliweb.com/hobby/board/1008/list?page={}".format(i))
            yield scrapy.Request("http://bbs.ruliweb.com/hobby/board/1009/list?page={}".format(i))
            yield scrapy.Request("http://bbs.ruliweb.com/market/board/320101/list?page={}".format(i))
            yield scrapy.Request("http://bbs.ruliweb.com/market/board/320102/list?page={}".format(i))
            yield scrapy.Request("http://bbs.ruliweb.com/market/board/320103/list?page={}".format(i))
            yield scrapy.Request("http://bbs.ruliweb.com/community/board/300143?cate=497/list?page={}".format(i))
            yield scrapy.Request("http://bbs.ruliweb.com/community/board/184318/list?page={}".format(i))
            yield scrapy.Request("http://bbs.ruliweb.com/community/board/184404/list?page={}".format(i))
            yield scrapy.Request("http://bbs.ruliweb.com/community/board/184032/list?page={}".format(i))
            yield scrapy.Request("http://bbs.ruliweb.com/community/board/300018/list?page={}".format(i))
            yield scrapy.Request("http://bbs.ruliweb.com/community/board/300146/list?page={}".format(i))
            yield scrapy.Request("http://bbs.ruliweb.com/community/board/300237/list?page={}".format(i))
            yield scrapy.Request("http://bbs.ruliweb.com/community/board/300236/list?page={}".format(i))
            yield scrapy.Request("http://bbs.ruliweb.com/community/board/300238/list?page={}".format(i))
            yield scrapy.Request("http://bbs.ruliweb.com/community/board/300245/list?page={}".format(i))
            yield scrapy.Request("http://bbs.ruliweb.com/community/board/300241/list?page={}".format(i))
            yield scrapy.Request("http://bbs.ruliweb.com/community/board/300171/list?page={}".format(i))
            yield scrapy.Request("http://bbs.ruliweb.com/community/board/300217/list?page={}".format(i))
            yield scrapy.Request("http://bbs.ruliweb.com/community/board/300216/list?page={}".format(i))
            yield scrapy.Request("http://bbs.ruliweb.com/community/board/300218/list?page={}".format(i))
            yield scrapy.Request("http://bbs.ruliweb.com/community/board/300220/list?page={}".format(i))
            yield scrapy.Request("http://bbs.ruliweb.com/community/board/300219/list?page={}".format(i))
            yield scrapy.Request("http://bbs.ruliweb.com/community/board/300214/list?page={}".format(i))
            yield scrapy.Request("http://bbs.ruliweb.com/community/board/300215/list?page={}".format(i))
            yield scrapy.Request("http://bbs.ruliweb.com/community/board/300105/list?page={}".format(i))
            yield scrapy.Request("http://bbs.ruliweb.com/community/board/300106/list?page={}".format(i))
            yield scrapy.Request("http://bbs.ruliweb.com/community/board/300546/list?page={}".format(i))
            yield scrapy.Request("http://bbs.ruliweb.com/community/board/182802/list?page={}".format(i))
            yield scrapy.Request("http://bbs.ruliweb.com/community/board/300160/list?page={}".format(i))
            yield scrapy.Request("http://bbs.ruliweb.com/community/board/300185/list?page={}".format(i))
            yield scrapy.Request("http://bbs.ruliweb.com/community/board/300162/list?page={}".format(i))
            yield scrapy.Request("http://bbs.ruliweb.com/community/board/300161/list?page={}".format(i))
            yield scrapy.Request("http://bbs.ruliweb.com/community/board/300281/list?page={}".format(i))
            yield scrapy.Request("http://bbs.ruliweb.com/community/board/300163/list?page={}".format(i))
            yield scrapy.Request("http://bbs.ruliweb.com/community/board/300164/list?page={}".format(i))
            yield scrapy.Request("http://bbs.ruliweb.com/community/board/300165/list?page={}".format(i))
            yield scrapy.Request("http://bbs.ruliweb.com/community/board/300436/list?page={}".format(i))
            yield scrapy.Request("http://bbs.ruliweb.com/community/board/300178/list?page={}".format(i))
            yield scrapy.Request("http://bbs.ruliweb.com/community/board/300179/list?page={}".format(i))
            yield scrapy.Request("http://bbs.ruliweb.com/community/board/300180/list?page={}".format(i))
            yield scrapy.Request("http://bbs.ruliweb.com/community/board/300184/list?page={}".format(i))
            yield scrapy.Request("http://bbs.ruliweb.com/community/board/300187/list?page={}".format(i))
            yield scrapy.Request("http://bbs.ruliweb.com/community/board/300269/list?page={}".format(i))
            yield scrapy.Request("http://bbs.ruliweb.com/community/board/300570/list?page={}".format(i))
            yield scrapy.Request("http://bbs.ruliweb.com/community/board/100241/list?page={}".format(i))
            yield scrapy.Request("http://bbs.ruliweb.com/community/board/100156/list?page={}".format(i))
            yield scrapy.Request("http://bbs.ruliweb.com/community/board/300438/list?page={}".format(i))
            yield scrapy.Request("http://bbs.ruliweb.com/community/board/300233/list?page={}".format(i))
            yield scrapy.Request("http://bbs.ruliweb.com/community/board/300229/list?page={}".format(i))
            yield scrapy.Request("http://bbs.ruliweb.com/community/board/300234/list?page={}".format(i))
            yield scrapy.Request("http://bbs.ruliweb.com/community/board/300235/list?page={}".format(i))
            yield scrapy.Request("http://bbs.ruliweb.com/community/board/300242/list?page={}".format(i))
            yield scrapy.Request("http://bbs.ruliweb.com/community/board/300243/list?page={}".format(i))
            yield scrapy.Request("http://bbs.ruliweb.com/community/board/300230/list?page={}".format(i))
            yield scrapy.Request("http://bbs.ruliweb.com/community/board/300244/list?page={}".format(i))
            yield scrapy.Request("http://bbs.ruliweb.com/community/board/300232/list?page={}".format(i))
            yield scrapy.Request("http://bbs.ruliweb.com/community/board/300168/list?page={}".format(i))
            yield scrapy.Request("http://bbs.ruliweb.com/community/board/300188/list?page={}".format(i))
            yield scrapy.Request("http://bbs.ruliweb.com/community/board/300263/list?page={}".format(i))
            yield scrapy.Request("http://bbs.ruliweb.com/community/board/300264/list?page={}".format(i))
            yield scrapy.Request("http://bbs.ruliweb.com/community/board/300265/list?page={}".format(i))
            yield scrapy.Request("http://bbs.ruliweb.com/community/board/300266/list?page={}".format(i))
            yield scrapy.Request("http://bbs.ruliweb.com/community/board/300267/list?page={}".format(i))
            yield scrapy.Request("http://bbs.ruliweb.com/community/board/300189/list?page={}".format(i))
            yield scrapy.Request("http://bbs.ruliweb.com/community/board/300198/list?page={}".format(i))
            yield scrapy.Request("http://bbs.ruliweb.com/community/board/300190/list?page={}".format(i))
            yield scrapy.Request("http://bbs.ruliweb.com/community/board/300191/list?page={}".format(i))
            yield scrapy.Request("http://bbs.ruliweb.com/community/board/300192/list?page={}".format(i))
            yield scrapy.Request("http://bbs.ruliweb.com/community/board/300193/list?page={}".format(i))
            yield scrapy.Request("http://bbs.ruliweb.com/community/board/300194/list?page={}".format(i))
            yield scrapy.Request("http://bbs.ruliweb.com/community/board/300195/list?page={}".format(i))
            yield scrapy.Request("http://bbs.ruliweb.com/community/board/300196/list?page={}".format(i))
            yield scrapy.Request("http://bbs.ruliweb.com/community/board/300197/list?page={}".format(i))
            yield scrapy.Request("http://bbs.ruliweb.com/community/board/300199/list?page={}".format(i))
            yield scrapy.Request("http://bbs.ruliweb.com/community/board/300200/list?page={}".format(i))
            yield scrapy.Request("http://bbs.ruliweb.com/community/board/300201/list?page={}".format(i))
            yield scrapy.Request("http://bbs.ruliweb.com/community/board/300202/list?page={}".format(i))
            yield scrapy.Request("http://bbs.ruliweb.com/community/board/300203/list?page={}".format(i))
            yield scrapy.Request("http://bbs.ruliweb.com/community/board/300204/list?page={}".format(i))
            yield scrapy.Request("http://bbs.ruliweb.com/community/board/300205/list?page={}".format(i))
            yield scrapy.Request("http://bbs.ruliweb.com/community/board/300206/list?page={}".format(i))
            yield scrapy.Request("http://bbs.ruliweb.com/community/board/300207/list?page={}".format(i))
            yield scrapy.Request("http://bbs.ruliweb.com/community/board/300208/list?page={}".format(i))
            yield scrapy.Request("http://bbs.ruliweb.com/community/board/300209/list?page={}".format(i))
            yield scrapy.Request("http://bbs.ruliweb.com/community/board/300210/list?page={}".format(i))
            yield scrapy.Request("http://bbs.ruliweb.com/community/board/300211/list?page={}".format(i))
            yield scrapy.Request("http://bbs.ruliweb.com/community/board/300212/list?page={}".format(i))
            yield scrapy.Request("http://bbs.ruliweb.com/community/board/300213/list?page={}".format(i))
            yield scrapy.Request("http://bbs.ruliweb.com/twitch/board/300562/list?cate=1211&page={}".format(i))
            yield scrapy.Request("http://bbs.ruliweb.com/twitch/board/300562/list?cate=542&page={}".format(i))
            yield scrapy.Request("http://bbs.ruliweb.com/twitch/board/300562/list?cate=525&page={}".format(i))
            yield scrapy.Request("http://bbs.ruliweb.com/twitch/board/300562/list?cate=519&page={}".format(i))
            yield scrapy.Request("http://bbs.ruliweb.com/twitch/board/320105/list?page={}".format(i))
            yield scrapy.Request("http://bbs.ruliweb.com/twitch/board/300041/list?page={}".format(i))
            yield scrapy.Request("http://bbs.ruliweb.com/family/212/board/300277/list?page={}".format(i))
            yield scrapy.Request("http://bbs.ruliweb.com/family/212/board/1010/list?page={}".format(i))
            yield scrapy.Request("http://bbs.ruliweb.com/family/212/board/300063/list?page={}".format(i))
            yield scrapy.Request("http://bbs.ruliweb.com/family/212/board/300064/list?page={}".format(i))
            yield scrapy.Request("http://bbs.ruliweb.com/family/212/board/300065/list?page={}".format(i))
            yield scrapy.Request("http://bbs.ruliweb.com/family/212/board/300512/list?page={}".format(i))
            yield scrapy.Request("http://bbs.ruliweb.com/family/212/board/300066/list?page={}".format(i))
            yield scrapy.Request("http://bbs.ruliweb.com/family/212/board/300068/list?page={}".format(i))
            yield scrapy.Request("http://bbs.ruliweb.com/family/212/board/300067/list?page={}".format(i))
            yield scrapy.Request("http://bbs.ruliweb.com/family/212/board/300069/list?page={}".format(i))
            yield scrapy.Request("http://bbs.ruliweb.com/family/212/board/300071/list?page={}".format(i))
            yield scrapy.Request("http://bbs.ruliweb.com/family/242/board/300017/list?page={}".format(i))
            yield scrapy.Request("http://bbs.ruliweb.com/family/242/board/300558/list?page={}".format(i))
            yield scrapy.Request("http://bbs.ruliweb.com/family/242/board/300084/list?page={}".format(i))
            yield scrapy.Request("http://bbs.ruliweb.com/family/242/board/300085/list?page={}".format(i))
            yield scrapy.Request("http://bbs.ruliweb.com/family/232/board/300016/list?page={}".format(i))
            yield scrapy.Request("http://bbs.ruliweb.com/family/232/board/300078/list?page={}".format(i))
            yield scrapy.Request("http://bbs.ruliweb.com/family/232/board/300079/list?page={}".format(i))
            yield scrapy.Request("http://bbs.ruliweb.com/family/232/board/300077/list?page={}".format(i))
            yield scrapy.Request("http://bbs.ruliweb.com/family/232/board/300081/list?page={}".format(i))
            yield scrapy.Request("http://bbs.ruliweb.com/family/211/board/300015/list?page={}".format(i))
            yield scrapy.Request("http://bbs.ruliweb.com/family/211/board/300277/list?cate=12&page={}".format(i))
            yield scrapy.Request("http://bbs.ruliweb.com/family/211/board/300277/list?cate=13&page={}".format(i))
            yield scrapy.Request("http://bbs.ruliweb.com/family/211/board/300277/list?cate=114&page={}".format(i))
            yield scrapy.Request("http://bbs.ruliweb.com/family/211/board/300277/list?cate=949&page={}".format(i))
            yield scrapy.Request("http://bbs.ruliweb.com/family/211/board/300277/list?cate=11&page={}".format(i))
            yield scrapy.Request("http://bbs.ruliweb.com/family/211/board/300073/list?page={}".format(i))
            yield scrapy.Request("http://bbs.ruliweb.com/family/211/board/300074/list?page={}".format(i))
            yield scrapy.Request("http://bbs.ruliweb.com/family/211/board/300089/list?page={}".format(i))
            yield scrapy.Request("http://bbs.ruliweb.com/family/211/board/300090/list?page={}".format(i))
            yield scrapy.Request("http://bbs.ruliweb.com/family/211/board/300430/list?page={}".format(i))
            yield scrapy.Request("http://bbs.ruliweb.com/family/211/board/300088/list?page={}".format(i))
            yield scrapy.Request("http://bbs.ruliweb.com/family/211/board/300557/list?page={}".format(i))
            yield scrapy.Request("http://bbs.ruliweb.com/family/211/board/500006/list?page={}".format(i))
            yield scrapy.Request("http://bbs.ruliweb.com/family/211/board/300545/list?page={}".format(i))
            yield scrapy.Request("http://bbs.ruliweb.com/family/211/board/300546/list?page={}".format(i))
            yield scrapy.Request("http://bbs.ruliweb.com/family/211/board/500023/list?page={}".format(i))
            yield scrapy.Request("http://bbs.ruliweb.com/family/211/board/300224/list?page={}".format(i))
            yield scrapy.Request("http://bbs.ruliweb.com/family/211/board/300222/list?page={}".format(i))
            yield scrapy.Request("http://bbs.ruliweb.com/family/211/board/300441/list?page={}".format(i))
            yield scrapy.Request("http://bbs.ruliweb.com/family/211/board/300544/list?page={}".format(i))
            yield scrapy.Request("http://bbs.ruliweb.com/family/211/board/300548/list?page={}".format(i))
            yield scrapy.Request("http://bbs.ruliweb.com/family/211/board/300552/list?page={}".format(i))
            yield scrapy.Request("http://bbs.ruliweb.com/family/211/board/183774/list?page={}".format(i))
            yield scrapy.Request("http://bbs.ruliweb.com/family/211/board/500024/list?page={}".format(i))
            yield scrapy.Request("http://bbs.ruliweb.com/family/211/board/500025/list?page={}".format(i))
            yield scrapy.Request("http://bbs.ruliweb.com/family/211/board/500005/list?page={}".format(i))
            yield scrapy.Request("http://bbs.ruliweb.com/family/211/board/300389/list?page={}".format(i))
            yield scrapy.Request("http://bbs.ruliweb.com/family/211/board/500007/list?page={}".format(i))
            yield scrapy.Request("http://bbs.ruliweb.com/family/211/board/500008/list?page={}".format(i))
            yield scrapy.Request("http://bbs.ruliweb.com/family/211/board/182802/list?page={}".format(i))
            yield scrapy.Request("http://bbs.ruliweb.com/family/211/board/300330/list?page={}".format(i))
            yield scrapy.Request("http://bbs.ruliweb.com/family/211/board/500009/list?page={}".format(i))
            yield scrapy.Request("http://bbs.ruliweb.com/family/211/board/500010/list?page={}".format(i))
            yield scrapy.Request("http://bbs.ruliweb.com/family/211/board/300566/list?page={}".format(i))
            yield scrapy.Request("http://bbs.ruliweb.com/family/211/board/500011/list?page={}".format(i))
            yield scrapy.Request("http://bbs.ruliweb.com/family/211/board/300173/list?page={}".format(i))
            yield scrapy.Request("http://bbs.ruliweb.com/family/211/board/300569/list?page={}".format(i))
            yield scrapy.Request("http://bbs.ruliweb.com/family/211/board/300070/list?page={}".format(i))
            yield scrapy.Request("http://bbs.ruliweb.com/family/211/board/500032/list?page={}".format(i))
            yield scrapy.Request("http://bbs.ruliweb.com/family/211/board/500026/list?page={}".format(i))
            yield scrapy.Request("http://bbs.ruliweb.com/family/211/board/500027/list?page={}".format(i))
            yield scrapy.Request("http://bbs.ruliweb.com/family/211/board/500028/list?page={}".format(i))
            yield scrapy.Request("http://bbs.ruliweb.com/family/211/board/500029/list?page={}".format(i))
            yield scrapy.Request("http://bbs.ruliweb.com/family/211/board/500030/list?page={}".format(i))
            yield scrapy.Request("http://bbs.ruliweb.com/family/211/board/500031/list?page={}".format(i))
            yield scrapy.Request("http://bbs.ruliweb.com/family/249/board/300119/list?page={}".format(i))
            yield scrapy.Request("http://bbs.ruliweb.com/family/249/board/300136/list?page={}".format(i))
            yield scrapy.Request("http://bbs.ruliweb.com/family/249/board/176262/list?page={}".format(i))
            yield scrapy.Request("http://bbs.ruliweb.com/family/249/board/300420/list?page={}".format(i))
            yield scrapy.Request("http://bbs.ruliweb.com/family/249/board/300121/list?page={}".format(i))
            yield scrapy.Request("http://bbs.ruliweb.com/family/249/board/300130/list?page={}".format(i))
            yield scrapy.Request("http://bbs.ruliweb.com/family/249/board/300131/list?page={}".format(i))
            yield scrapy.Request("http://bbs.ruliweb.com/family/249/board/300122/list?page={}".format(i))
            yield scrapy.Request("http://bbs.ruliweb.com/family/249/board/300123/list?page={}".format(i))
            yield scrapy.Request("http://bbs.ruliweb.com/family/249/board/300127/list?page={}".format(i))
            yield scrapy.Request("http://bbs.ruliweb.com/family/249/board/300128/list?page={}".format(i))
            yield scrapy.Request("http://bbs.ruliweb.com/family/249/board/300129/list?page={}".format(i))
            yield scrapy.Request("http://bbs.ruliweb.com/family/249/board/300139/list?page={}".format(i))
            yield scrapy.Request("http://bbs.ruliweb.com/family/249/board/300138/list?page={}".format(i))
            yield scrapy.Request("http://bbs.ruliweb.com/family/249/board/300132/list?page={}".format(i))
            yield scrapy.Request("http://bbs.ruliweb.com/family/249/board/300133/list?page={}".format(i))
            yield scrapy.Request("http://bbs.ruliweb.com/family/249/board/300140/list?page={}".format(i))
            yield scrapy.Request("http://bbs.ruliweb.com/family/249/board/300126/list?page={}".format(i))
            yield scrapy.Request("http://bbs.ruliweb.com/family/249/board/300125/list?page={}".format(i))

    def parse(self, response):
        for select in response.xpath('//tr[@class="table_body"]'):
            item = DamoaItem()

            item['source'] = self.name

            titleXpath = "td[@class='subject']/div[@class='relative']/a/text()"
            item['title'] = createItemUseXpath(select, titleXpath, texttype="")

            linkXpath = "td/div[@class='relative']/a/@href"
            item['link'] = createItemUseXpath(select, linkXpath, texttype=TextType.LINK)

            attrXpath = "td[@class='divsn']/a/text()"
            item['attribute'] = createItemUseXpath(select, attrXpath, texttype="")

            tagName = "span"
            tagAttr = {"class": "regdate"}
            item['date'] = createItemUseBs4(item['link'], tagName, tagAttr, texttype=TextType.DATE, encoding="CP949")

            hitsXpath = "td[@class='hit']/text()"
            item['hits'] = createItemUseXpath(select, hitsXpath, texttype=TextType.INT)

            recommenedXpath = "td[@class='recomd']/text()"
            item['recommened'] = createItemUseXpath(select, recommenedXpath, texttype=TextType.INT)

            item['last_update'] = getCurrentTime("string")

            item['pop'] = createItem_pop(item['date'], item['recommened'], item['hits'])

            tagName = "div"
            tagAttrs = {"class": "view_content"}
            item['text'] = createItemUseBs4(item['link'], tagName, tagAttrs, encoding="CP949", texttype=TextType.TEXT)

            if filterItem(item) != None:
                yield filterItem(item)


