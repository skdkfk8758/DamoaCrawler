"""
추천도 계산

TMC*w + A*w + S*w + P*w + G*w

TMC : 사용자 태그와 텍스트사이 카운트 합
A : 속성점수 -> 사용자가 원하는 속성인지 판단
S : 게시물점수(좋아요) ??
P : 게시물 인기도(DB에 있음)
G : 게시물이 갱신된 시간? ??

w : 가중치

"""

import pymysql


class Chuchendo:

    userTag = ['질문', '답변']

    TMC = 0

    # DB 접속
    def __init__(self):
        try:
            self.conn = pymysql.connect(host="gb1541.synology.me", port=32768, user="root", password="rmstlr1234",
                                        db="Damoa",
                                        charset="utf8")
            self.cursor = self.conn.cursor(pymysql.cursors.DictCursor)

        except pymysql.Error:
            print("DB Connection Error")

    # DB에서 속성 가져와 게시판속성 정규화
    def selectAttrs(self):
        sql = "select * from totalposts"

        self.cursor.execute(sql)

        result = self.cursor.fetchone()

        print(result['posttext'])

        for tag in self.userTag:
            print(tag)
            print(result['posttext'].count(tag))
            self.TMC = self.TMC + result['posttext'].count(tag)

        print('TMC : ' + str(self.TMC))
        print('pop : ' + str(result['popurarity']))

        print('추천도 : ' + str(self.TMC*0.5 + result['popurarity']*0.5))

    # 의미없는 게시물 - 텍스트가 없는 게시물,
    def testSelect(self):
        # sql = "select * from totalposts where posttext = ''"
        sql = "select * from totalposts where hits>=100"

        self.cursor.execute(sql)

        result = self.cursor.fetchall()
        print(result.__len__())



if __name__ == '__main__':
    # Chuchendo().selectAttrs()
    Chuchendo().testSelect()


