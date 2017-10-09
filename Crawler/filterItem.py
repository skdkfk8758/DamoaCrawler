from datetime import datetime


def filterItem(item):

    if "공지" in item["attribute"] or "이용" in item["title"]:
        # print("filter")
        pass
    else:
        dateTmp_post = datetime.strptime(item['date'], '%Y-%m-%d %H:%M:%S')
        dateTmp_curr = datetime.strptime(datetime.now().strftime('%Y-%m-%d %H:%M:%S'), '%Y-%m-%d %H:%M:%S')

        # 한시간당 가중치 감소(시간으로 조회수 나눔)
        timeTmp = (dateTmp_curr - dateTmp_post).total_seconds() / 60

        # if timeTmp>1:
        #     # 1분 이상 게시물의 분당 조회수 계산
        #
        #     #  오래된 게시물에 가산점 = 조회수/10000
        #     addHPH = int(item["hits"]) / 10000
        #
        #     # 분당 조회수 계산
        #     hitsPerMin = ((int(item['hits']) / timeTmp)) + addHPH
        #     # print(str(hitsPerMin) + "\n")
        #
        #     if hitsPerMin>=1 and len(item["text"])>=50:
        #         # 분당 조회수가 1이상히고 텍스트 길이가 50 이상이면 의미있는 게시물로 추정
        #         # print(originItem)
        #         # print(originItem["title"])
        #         # print(item["title"])
        #         return item

        return item