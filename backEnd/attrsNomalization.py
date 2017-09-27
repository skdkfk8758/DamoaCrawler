"""
게시판 속성 정규화 알고리즘


게시판 분류 해야됨 -> 세부적으로

"""

import pymysql

class attrsNorm:

    normAttrList = ['자유게시판','공지사항','콘솔게임','pc게임','모바일게임','보드게임','게임 기타게시판','회사게시판','직업게시판','차게시판',
                    '요리게시한','완구게시판','영화게시판','드라마게시판','군 게시판','도서 게시판','사람게시판','생활게시판','상품게시판',
                    '언론게시판','기타', '영상', '유머', '사진','x_시리즈', '하드웨어','소프트웨어','국가별','SNS','통신사', '웹툰',
                    '애니메이션', '음악게시판','스포츠게시판','강좌게시판','음식게시판','동물게시판']  # 정규화 시킬 속성이름

    notiListTmp = ['이용규칙', '공지사항', '새소식', '소식', '공지']  # 공지사항 게시판
    freeListTmp = ['일반', '아무거나 게시판', '아무거나 질문', '모두의공원', '잡담', '질문', '인생']  # 자유게시판

    consoleGameListTmp = ['정발', 'NGCD', 'GB', '수리', '구작', 'PSVITA', '요청', 'NS', '신작', '불량', 'GC', 'PS1',
                      'PS2', 'PS3', 'PS4', 'Xbox360', 'XboxOne', 'Xbox', 'XBOX', 'XBO', 'PS VR',
                      'PS4 소프트', 'PS4하드', 'NDS', 'Wil', 'WilU', 'XB360소프트', 'PSP', 'XB360', 'XBO소프트',
                      '3DS', 'Switch', 'NGC', 'MSX', 'SFC']     # 콘솔게임 게시판

    pcGameListTmp = [ 'NGP', 'PCO', 'PCE', '3DO', 'SS', 'e스포츠', '게임S/W', '게임H/W', '오버워치', '스타', '스타2', 'NEOGEO',
                  ' LOL', '디아3', '스팀', '클로저스']      # pc게임 게시판

    mobileGameListTmp = ['포켓몬GO','밀리언아서']      # 모바일 게임 게시판
    boardGameListTmp = ['유희왕', '카드/보드', '마작', '카드', '보드']      # 보드게임 게시판

    gameEtcListTmp = ['MD', '32X', 'MCD', '친추', '세이브', 'GBA', 'EMUL', '세이브파일', 'TCG', 'GG', '공략/팁', '게임소감', '인디게임', '데모',
                   'AC','답변',]      # 게임 기타게시판

    companyListTmp = ['제작사']    # 회사 게시판
    jobListTmp = ['기획']     # 직업게시판
    carListTmp = ['자동차']    # 차 게시판
    cookListTmp = []        # 요리 게시판
    figureListTmp = ['완구', '제작', '조립', '캐릭터', '콜캐', 'PVC', '12인치']      # 완구 게시판
    movieListTmp = ['예고편', ]    # 영화 게시판
    dramaListTmp = ['스포일러']     # 드라마 게시판
    millitaryListTmp = ['스케일']     # 군 게시판
    bookListTmp = ['신간', 'Book', '만화책']     # 도서 게시판

    personListTmp = ['MC', '친구추가', '이성', '인터뷰', '친추', '한국개그맨', '인물/패션', '한국배우', '한국가수', '방송인', '한국아이돌',
                     '선수', '미소녀']      # 사람 게시판

    livingListTmp = ['구관' '가게', '미국', '진상', '설문', '수기', '번개''비행기', '마이룸', '신체', 'A/S', '실화', '체험', '퀴즈',
                     '취미', '사설', '루머', '컴플렉스','첫인사', '탐방', '답변', '일기', '추억', '사건', '체험담', '사고', '구입',
                     '구매후기', '공포','명상법', '감상', '개조', '도서', '정모', '상담', '행사/보도', '참고/팁', '초자연현상', '요청',
                     '레어', '화장품', '미스테리', '악몽','학업', '여장', '조립', '고민', '문화/여행', '미스터리', '창업', '출석',
                     '완성', '추리', '수리', '행사', '기획','인라인', '제작', '논쟁', '소문', '참고','사랑', '감동']     # 생활 게시판

    goodsListTmp = ['인테리어', '테크닉', '교환' '캐릭터상품', '불만', 'HTC VIVE', '레고', '체험담 사용기', '만족', '가격', '모닝구', '후기',
          '구입', '구매후기', '사용후기', '신작', '육아용품', '유료나눔', '의류', '인형', '생활용품', '판매', '상품권', '초합금', '수리',
          '쇼핑', '사용기', 'MarkIII', '페크', '레저용품']     # 상품 게시판

    pressListTmp = ['전자', '사건', '사설', '루머', '인터뷰', '체험단 사용기', '사고', '기사', '요청', '방송인', '비평', '경제',
                    '제작사', '제작']    # 언론게시판

    videoListTmp = ['도서' '트위치', '유튜브', '영상', 'TV팟', '다이캐스트', '방송', '뮤직비디오', 'Blu-ray', 'DVD', '영샹', '아프리카', '특촬',
                    'LIVE', '영상물', '업체홍보', '영화/게임', '공연', '홍보', '동영상', 'MV', ]  # 영상게시판

    humorListTmp = ['웃대POLL', '기쁨', '코믹', '만담', '쫑알쫑알찡찡', '웃긴자료', '유머', '웃긴유머']  # 유머게시판

    photoListTmp = ['메카닉', '2', '풍경/자연', '일러스트', '내사진', '갤러리', '친구사진', '애인사진', '그래픽', '팬아트', '추천앨범', '직찍', '스샷', '가족사진',
                    '이미지', '사진','배경화면', ]  # 사진게시판

    xSeriesListTmp = ['잡담x', '질문x', '소감x', '정보x', 'X풍경']  # __x 시리즈게시판
    hardwareListTmp = ['아이패드', '디카', 'PC98', '휴대폰', 'H/W', '기기', 'PC', 'Mac', 'PC/가전', '하드웨어', '3D프린터', '하드관련', '하드소감',
                       'NS하드', 'PS3하드', 'XBO하드']  # 하드웨어 게시판

    softwareListTmp = ['S/W', 'NS소프트']  # 소프웨어 게시판
    countryListTmp = ['필리핀', '서양', '호주', '일본', '중국', '홍콩', '영국', '외국', '한국', '중식', '북미', '국내', '九州']  # 국가별 게시판
    snsListTmp = ['페이스북', '트위터']  # sns게시판
    phoneListTmp = ['종합', 'SKT', '이통사', '윈도우폰', 'SKYHD', 'KT', '가샤폰', '안드로이드', '앱', 'LGU', '휴대기기', 'LGU+', '아이폰',
                    'MVNO']  # 폰관련 게시판

    webtoonListTmp = ['웃대툰', '신예툰', '웹툰']  # 웹툰 게시판
    aniListTmp = ['자료', '스위치','애니', '애니/만화', '뱅가드', '만화', '헬로친구들']  # 애니매이션 게시판
    musicListTmp = ['연주', '추천음악', '음향', '팝송', '음악', 'BGM', '악기', '추천곡','감상',]  # 음악게시판
    sportsListTmp = ['야구', '농구', '축구', '스포츠', 'FC', 'MLB']  # 스포츠 게시판
    infoListTmp = ['정보', '프로그래밍', '강좌', '강좌게시판', '학습', '유용한 사이트', '자작', '논술', '정치', '뉴스', '사용기 게시판', ]  # 강좌/강의/정보 게시판
    foodListTmp = ['일식', '음식', '커피', '한식', '디저트', '분식', '패스트푸드', '양식', ]  # 음식게시판
    animalListTmp = ['고양이', '새', '파충류', '동물대학', '양서류', '강아지', '생태/동식물']  # 동물게시판

    etcListTmp = ['ETC', 'etc', '자료실', '1.5', '식완', '허억','雜談', '맥주로샤워한변태오스틴', 'オフ會', 'なんでやねん', '수련기',
                  '밍가닌퉤난퉤', '고토마키','탐방', '텍스트', '아동복은호구아이', '피냄새나는카가', '외계인', '오큘러스', 'お知らせ',
                  '소프비', '레이뽕맞은블루', '일기', '명대사', '헬로프로젝트', '앗샹','相談', '아야야', '만족', '트레이딩', '스포일러',
                  '후기', '스케일', '소감', '토론', '소문', '레진', '情報', '드림군짱', '대기자료', '네타', '추억', 'PVC', '낫치',
                  '사건', 'NG', '시스템', '한국개그맨', '라노벨', 'DD', 'BMX', '사무실', '가상리그', '소개', '쥔장', '한국배우',
                  '레고', '편성', '명상법', '감상', '개조', '옥스퍼드','한정', '촬영회', '건의', '행사/보도', '초자연현상','리뷰', '레어',
                  '방송인', '한국아이돌','인형', '생활용품', '설문', '참고', '사랑', '비평','선수', '팬픽', '쯔지렐라', '선박', '통합',
                  'Book','추천', 'N64', '과학', '매장', '심령', '듀얼','수리', '괴담', '햄스터', '기획', 'BSWA',
                  '제작사', '페릿', '제작', '제안', 'MTG', '대회', '하로키즈', '의견', '경험담', '선박']  # 기타 게시판

    listCollection = {'freeList' : freeListTmp,  'notiList' : notiListTmp, 'consoleGameList' : consoleGameListTmp,
                      'pcGameList':pcGameListTmp, 'mobileGameList':mobileGameListTmp, 'boardGameList':boardGameListTmp,
                      'gameEtcList':gameEtcListTmp,'companyList':companyListTmp, 'jobList':jobListTmp, 'carList':carListTmp,
                      'cookList':cookListTmp,'figureList':figureListTmp, 'movieList':movieListTmp, 'dramaList':dramaListTmp,
                      'millitaryList':millitaryListTmp, 'bookList':bookListTmp, 'personList':personListTmp,
                      'livingList':livingListTmp, 'goodsList':goodsListTmp, 'pressList':pressListTmp, 'etcList': etcListTmp,
                      'videoList': videoListTmp,'humorList': humorListTmp,'photoList': photoListTmp,'xSeriesList': xSeriesListTmp,
                      'hardwareList': hardwareListTmp,'softwareList' : softwareListTmp,'country' : countryListTmp,
                      'snsList' : snsListTmp,'phoneList': phoneListTmp,'webtoonList': webtoonListTmp, 'aniList': aniListTmp,
                      'musicList': musicListTmp,'sportsList':sportsListTmp,'infoList': infoListTmp,'foodList': foodListTmp,
                      'animalList': animalListTmp}   # 각 리스트들을 딕셔너리로 저장


    listCollectionKey = ['freeList', 'notiList','consoleGameList','pcGameList','mobileGameList','boardGameList','gameEtcList',
                         'companyList','jobList','carList','cookList','figureList','movieList','dramaList','millitaryList',
                         'bookList','personList','livingList','goodsList','pressList','etcList','videoList',
                         'humorList','photoList','xSeriesList','hardwareList','softwareList','country','snsList','phoneList',
                         'webtoonList','aniList','musicList','sportsList','infoList','foodList','animalList']    # 리스트컬렉션 키 집합

    tmpList = []    # 정규화되지 않은 항목 리스트
    normCompList = []   # 정규화된 항목 리스트

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
        # sql = "select * from totalposts where post_attribute = %s"
        sql = "select * from totalposts"

        # self.cursor.execute(sql,(input("asdasd : "),))
        self.cursor.execute(sql)

        result = self.cursor.fetchall()

        for item in result:
            keyPoint = 0    # 정규화된 리스트에서 요소값을 가져오기위한 변수
            for key in self.listCollectionKey:  # 컬렉션키 집합에서 키를 하나씩 가져옴
                # print(key.__len__())
                for i in range (0, self.listCollection[key].__len__(),1):   # 가져온 키값의 리스트로 접근
                    # print(self.listCollection[key])
                    if self.listCollection[key][i] in item['post_attribute']:   # 각 리스트별 요소가 DB에서 가져온 속성에 포함(같으면)되면 정규화된 속성으로 다시 저장
                        self.normCompList.append(item['title'] +" # "+ self.normAttrList[keyPoint] +' # '+ item['post_attribute'])
                keyPoint = keyPoint + 1

            # print(item['post_attribute'] + " | " + item['title'] + " | " + item['posttext'])

            # 각 리스트에서 중복확인후 없는거 골라내기위한 부분 -> 비교를위해 한번 사용 아마 불필요
            # if item['post_attribute'] in self.freeListTmp or item['post_attribute'] in self.gameListTmp \
            #         or item['post_attribute'] in self.etcListTmp or item['post_attribute'] in self.notiListTmp \
            #         or item['post_attribute'] in self.videoListTmp or item['post_attribute'] in self.humorListTmp\
            #         or item['post_attribute'] in self.photoListTmp or item['post_attribute'] in self.xSeriesListTmp \
            #         or item['post_attribute'] in self.hardwareListTmp or item['post_attribute'] in self.softwareListTmp \
            #         or item['post_attribute'] in self.countryListTmp or item['post_attribute'] in self.snsListTmp \
            #         or item['post_attribute'] in self.phoneListTmp or item['post_attribute'] in self.webtoonListTmp \
            #         or item['post_attribute'] in self.aniListTmp or item['post_attribute'] in self.musicListTmp \
            #         or item['post_attribute'] in self.sportsListTmp or item['post_attribute'] in self.infoListTmp \
            #         or item['post_attribute'] in self.foodListTmp or item['post_attribute'] in self.animalListTmp:
            #     pass
            # else:
            #     self.tmpList.append(item['post_attribute'])

        for t in self.normCompList:
            print(t)
        print(len(set(self.normCompList)))

if __name__ == '__main__':
    attrsNorm().selectAttrs()



