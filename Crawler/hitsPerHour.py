import pymysql
from Crawler.DBConfig import *
from Crawler.CreateItem import *
import math
from matplotlib import pyplot

class TotalpostDAO:

    # DB접속을 위해 커넥션 얻는 부분
    def __init__(self):
        try:
            self.conn = pymysql.connect(host = HOST, port = PORT, user = USER, password = PASSWORD, db = DB,charset = CHARSET)
            self.cursor = self.conn.cursor()

        except pymysql.Error as e:
            print("DB Connection Error")


    def asd(self):
        sql = "select hits, recommened from totalposts where source=%s"

        sum = 0

        for name in ["clien", "humoruniv", "ygosu", "ruli", "giggle", "bobaedream", "82cook", "dramameeting",
                     "fmkorea", "gameshot", "hwbattle", "quasarzone", "thisisgame", "underkg"]:
            try:
                self.cursor.execute(sql, name)

                results = self.cursor.fetchall()

                for result in results:
                    hit = result[0]
                    recc = result[1]
                    if hit < 1:
                        hit = 1
                        sum = sum + (recc/hit)
                    else:
                        sum = sum + (recc/hit)

                print(name + " " + str((sum/len(results)) * 100))

            except pymysql.Error as e:
                print("SELECT Error : " + str(e))

        self.conn.commit()

    def nogada(self):
        sql = "select post_attribute from totalposts group by post_attribute"

        self.cursor.execute(sql)

        results = self.cursor.fetchall()

        for rs in results:
            print(rs[0])


if __name__ == '__main__':

    dd = TotalpostDAO()

    dd.asd()