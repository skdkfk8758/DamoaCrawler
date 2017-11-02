# -*- coding: utf-8 -*-

"""
크롤링한 내용을 db에 저장하기 위한 작업 진행

2017.10.14
 - 스파이더 종료 로그기록 남김

"""

import time # 시간측정을 위한 모듈
from Crawler.TotalpostDAO import TotalpostDAO
from Crawler.refrashDB import refrashDB
import datetime
import subprocess

class DamoaPipeline(object):

    start = 0
    end = 0

    dao = TotalpostDAO()
    refDB = refrashDB()

    def open_spider(self, spider):
        self.start = time.time()

    def close_spider(self, spider):
        self.end = time.time()
        # self.dao.deleteOldData()

        f = open("Finished_LOG.log", "a")
        f.write("\n"+" <" + spider.name + "> " + "start : " + str(datetime.datetime.now()) + "runtime : " + str(self.end - self.start))
        f.close()
        subprocess.call("curl http://localhost:6800/schedule.json -d project=Damoa -d spider={}".format(spider.name), shell=True)

    def process_item(self, item, spider):
        self.dao.insertOrUpdateItemToDB(item)







