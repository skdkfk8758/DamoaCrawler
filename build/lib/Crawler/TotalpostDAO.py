
"""

DB에 접근 및 입력, 삭제, 수정하는 클래스
중복된 내용은 DB에 갱신하고
내용이 없으면 추가됨

2017.10.06
    - DB : link에 index 만들어서 checkDate() 속도 향상

"""

import pymysql
from Crawler.spiders.Setting import *
from Crawler.DBConfig import *

class TotalpostDAO:

    # DB접속을 위해 커넥션 얻는 부분
    def __init__(self):
        try:
            self.conn = pymysql.connect(host = HOST, port = PORT, user = USER, password = PASSWORD, db = DB,charset = CHARSET)
            self.cursor = self.conn.cursor()

        except pymysql.Error as e:
            print("DB Connection Error")

    def insertOrUpdateItemToDB(self, item):

        sql = "call checkDataForInsertOrUpdate(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"

        tmpList = dict(item).values()
        listToTuple =tuple(tmpList)

        try:
            self.cursor.execute(sql,listToTuple)
        except pymysql.Error as e:
            print("Insert Error : " + str(e))

        self.conn.commit()

    def DBClose(self):
        self.cursor.close()
        self.conn.close()

    def deleteOldData(self):

        sql = "call deleteOldData(%s)"

        try:
            self.cursor.execute(sql, (SIX_MONTH,))
        except pymysql.Error as e:
            print("Delete Error : " + str(e))

        self.conn.commit()
        self.cursor.close()
        self.conn.close()