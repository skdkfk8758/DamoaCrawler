
"""

DB에 접근 및 입력, 삭제, 수정하는 클래스
중복된 내용은 DB에 갱신하고
내용이 없으면 추가됨

2017.10.06
    - DB : link에 index 만들어서 checkDate() 속도 향상

"""

import pymysql
from datetime import datetime
from Crawler.filterItem import *

class TotalpostDAO:

    # DB접속을 위해 커넥션 얻는 부분
    def __init__(self):
        try:
            self.conn = pymysql.connect(host="gb1541.synology.me", port = 32768, user="root", password="rmstlr1234", db="Damoa",charset="utf8")
            # self.conn = pymysql.connect(host="damoadb.c7efoq9ndida.us-east-1.rds.amazonaws.com", port = 3306, user="skdkfk8758", password="sxcv5012", db="damoa", charset='utf8')
            self.cursor = self.conn.cursor()

        except pymysql.Error:
            # print(pymysql.Error.args)
            print("DB Connection Error")

    # DB에 데이터 저장
    def insertDB(self, item):

        # print(filterItem(item))

        sql = """insert into
                totalposts
                (source ,title, link, attr, postdate, hits, recommened, lastupdate, pop, text)
                values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""

        # item 값을 db에 저장하기 위해 튜플로 바꾸는 작업
        tmpList = dict(item).values()
        listTotuple = tuple(tmpList)
        # ----------------------------------

        self.cursor.execute(sql, listTotuple)
        self.conn.commit()

    # DB에서 중복된 내용을 체크해서 같은 게시물은 추가하지않고 갱신함
    def checkDB(self, item):

        # print(item['source'] + item["title"])

        sql = "select count(*) from totalposts where title=%s and text=%s"
        # sql = "select count(*) from totalposts"2

        # link를 가지고 DB에 레코드 존재하는지 확인
        self.cursor.execute(sql,(item['title'],item['text']))
        # self.cursor.execute(sql,)

        result = self.cursor.fetchone()

        # link 기준으로 레코드 수 세서 1개 이상이면 갱신하고 없으면 추가
        # 1시간 이상 지났으면 업데이트
        if list(result)[0] <= 0:
            self.insertDB(item)
        else:
            if self.checkDate(item)>=1:
                self.updateDB(item)


    # DB에서 마지막갱신일과 게시물 게시일을 비교해서 1시간 이상 지났는지 체크
    def checkDate(self, item):

        check = 0

        sql = "select postdate, lastupdate from totalposts where link=%s"

        # link를 가지고 DB에 레코드 존재하는지 확인
        self.cursor.execute(sql, (item['link'],))

        result = self.cursor.fetchone()

        try:
            timeTmp1 = datetime.strptime(str(result['lastupdate']), "%Y-%m-%d %H:%M:%S")
            timeTmp2 = datetime.strptime(str(result['postdate']), "%Y-%m-%d %H:%M:%S")
            timeGap = (timeTmp1-timeTmp2).total_seconds()/3600

            if timeGap <= 1:
                check = 0
            else :
                check = 1
            return check
        except:
            return check

    # DB 갱신
    def updateDB(self, item):

        sql = """update totalposts
        set source = %s, attr = %s, title = %s, link = %s, postdate = %s, hits = %s,
        recommened = %s, lastupdate = %s, pop = %s, text = %s
        where and link = %s"""

        tmpItemList = [item['source'], item['attribute'], item['title'], item['link'],
                       item['date'], item['hits'], item['recommened'], item['last_update'], item['pop'],
                       item['text'], item['link']]

        self.cursor.execute(sql, tmpItemList)

        self.conn.commit()

