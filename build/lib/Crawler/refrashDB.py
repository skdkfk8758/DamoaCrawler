
"""

1달이상 게시물 삭제

"""

import pymysql
from datetime import datetime
from Crawler.filterItem import *
from Crawler.spiders.Setting import *

class refrashDB:

    # DB접속을 위해 커넥션 얻는 부분
    def __init__(self):
        try:
            self.conn = pymysql.connect(host="gb1541.synology.me", port = 32768, user="root", password="rmstlr1234", db="Damoa",
                                    charset="utf8")
            self.cursor = self.conn.cursor(pymysql.cursors.DictCursor)

        except pymysql.Error:
            print(pymysql.Error.args)
            print("DB Connection Error")

    # DB에 데이터 저장
    def searchDB(self, spiderName):

        sql = "select * from totalposts where source = %s"

        self.cursor.execute(sql, spiderName)

        result = self.cursor.fetchall()

        dateTmp_curr = datetime.strptime(datetime.now().strftime('%Y-%m-%d %H:%M:%S'), '%Y-%m-%d %H:%M:%S')

        for rs in result:
            timeTmp1 = datetime.strptime(str(rs['mydate']), "%Y-%m-%d %H:%M:%S")
            timeGap = (dateTmp_curr - timeTmp1).total_seconds()

            if timeGap > SIX_MONTH: # 일정기간 지난 게시물 삭제
                self.deleteRecord(rs['link'])

    def deleteRecord(self, link):
        sql = "delete from totalposts where link = %s"

        self.cursor.execute(sql, link)

        self.conn.commit()




