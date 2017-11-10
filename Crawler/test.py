import pymysql
import matplotlib.pyplot as plt

class TotalpostDAO:
    # DB접속을 위해 커넥션 얻는 부분
    def __init__(self):
        try:
            self.conn = pymysql.connect(
                host="damoa.cfgh1vs9ndmp.ap-northeast-2.rds.amazonaws.com",
                port=3306,
                user="root",
                password="sxcv5012",
                db="Damoa",
                charset="utf8mb4")
            self.cursor = self.conn.cursor()

        except pymysql.Error as e:
            print("DB Connection Error")

    def asd(self):
        sql = "select title, hits, recommened from totalposts where source=%s"

        hitSum = 0
        recoSum = 0

        pops = []

        for name in ["humoruniv",
                     "ygosu",
                     "ruli",
                     "giggle",
                     "bobaedream",
                     "82cook",
                     "fmkorea",
                     "gameshot",
                     "hwbattle",
                     "quasarzone",
                     "thisisgame",
                     "underkg"
                     ]:
            try:
                self.cursor.execute(sql, name)

                results = self.cursor.fetchall()

                for rs in results:
                    hit = rs[1]
                    reco = rs[2]
                    title = rs[0]

                    hitSum = hitSum + hit
                    recoSum = recoSum + reco

                    hpp = hitSum / len(results)
                    rpp = recoSum / len(results)
                    hpr = (hitSum / len(results)) / (recoSum / len(results))

                    pop = (hit / hpr) + reco

                print(
                    # "pop :", pop,
                      # "recoSum :", recoSum,
                      "avg(hit/post) :", hpp,
                      "avg(reco/post) :", rpp,
                      "avg(hit/reco) : ", hpr,
                       name, len(results))


            except pymysql.Error as e:
                print("SELECT Error : " + str(e))

        self.conn.commit()


if __name__ == '__main__':

    dd = TotalpostDAO()

    # for i in range(20):
    dd.asd()
        # print("\n")