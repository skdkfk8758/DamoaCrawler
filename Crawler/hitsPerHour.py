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
        sql = "select mydate, hits, recommened from totalposts where source=%s"

        sum = 0

        for name in ["clien", "humoruniv", "ygosu", "ruli", "giggle", "bobaedream"]:
            try:
                self.cursor.execute(sql, name)

                results = self.cursor.fetchall()

                for result in results:
                    timeTmp = result[0].strftime("%Y-%m-%d %H:%M:%S")  # type of String
                    time = (getCurrentTime("datetime") - getPostTime(timeTmp,"datetime")).total_seconds() / 3600
                    hit = result[1]
                    recc = result[2]
                    sum = sum+(hit/time)

                    z = (((hit/100)/time) + (recc/time))

                    pop = 1 / 1 + math.exp((-z))

                    # print("z : "  +  str(z))
                    print(name + " poptmp : " + str(pop-1))
                    # print(name + " pop : " + str((pop/8.58)))

                # print(sum)
                # print(len(results))
                # print(sum/len(results))

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

    ban = ["www", ".c"]
    ss = ["www.naver.com", "aaa.sadas.ss"]

    for s in ss:
        if "www" in s:
            pass
        else:
            print(s)
