
"""

DB에 접근 및 입력, 삭제, 수정하는 클래스
중복된 내용은 DB에 갱신하고
내용이 없으면 추가됨

"""

import pymysql
from datetime import datetime

class MonthPastDelete:

    # DB접속을 위해 커넥션 얻는 부분
    def __init__(self):
        try:
            self.conn = pymysql.connect(host="gb1541.synology.me", port = 32768, user="root", password="rmstlr1234", db="Damoa",
                                    charset="utf8")
            self.cursor = self.conn.cursor(pymysql.cursors.DictCursor)

        except pymysql.Error:
            print("DB Connection Error")

    def selectDB(self):
        sql = """select title, link, mydate from totalposts"""

        self.cursor.execute(sql)

        result = self.cursor.fetchall()

        # Ubuntu Time Chek
        dateTmp_curr = datetime.strptime(datetime.now().strftime('%Y-%m-%d %H:%M:%S'), '%Y-%m-%d %H:%M:%S')
        print(dateTmp_curr)

        # 한달이상 게시물 삭제
        for rs in result:
            dateTmp_curr = datetime.strptime(datetime.now().strftime('%Y-%m-%d %H:%M:%S'), '%Y-%m-%d %H:%M:%S')
            postDate = datetime.strptime(str(rs['mydate']), "%Y-%m-%d %H:%M:%S")
            timeGap = (dateTmp_curr - postDate).total_seconds()

            if timeGap > 2592000:
                self.deleteDB(rs["link"])

        self.conn.commit()



    def deleteDB(self, link):
        sql = """delete from totalposts where link = %s """

        self.cursor.execute(sql, link)


if __name__ == '__main__':
    monthPastDelete = MonthPastDelete()

    oldDay = 0

    dateTmp_curr = datetime.strptime(datetime.now().strftime('%Y-%m-%d %H:%M:%S'), '%Y-%m-%d %H:%M:%S')
    oldDay = datetime.now().day

    # print(oldDay)

    while 1:
        if datetime.now().day != oldDay:
            monthPastDelete.selectDB()
            oldDay = datetime.now().day
        #     print("asd")
        # else:
        #     print("123")





