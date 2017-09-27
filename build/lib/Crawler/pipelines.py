# -*- coding: utf-8 -*-

"""
clien 파이프라인

크롤링한 내용을 db에 저장하기 위한 작업 진행

"""

import time # 시간측정을 위한 모듈
from Crawler.TotalpostDAO import TotalpostDAO

class DamoaPipeline(object):

    start = 0
    end = 0
    # DB접속을 위한 객체 생성
    dao = TotalpostDAO()

    # 스파이더 시작하면 수행되는 부분
    def open_spider(self, spider):

        self.start = time.time()
        print(spider.name + " Spider Start")

    # 스파이더 종료되면 수행되는 부분
    def close_spider(self, spider):
        print(spider.name + " Spider Stop")
        self.end = time.time()
        print(spider.name +" "+ str(self.end - self.start))

    # 스파이더 진행 후 데이터베이스에 저장
    # def process_item(self, item, spider):

        # print("start DB")
        # self.dao.checkDB(item)
        # print("end DB")






