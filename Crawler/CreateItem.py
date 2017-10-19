"""
Item 객체에 데이터를 구성해주는 클래스
Create : 2017.10.09

"""

import requests
from datetime import datetime
from bs4 import BeautifulSoup

from Crawler.TextTypeEnum import *

def replaceText(text, texttype):
    if texttype == TextType.LINK:
        replacedText = text.replace('\t','').replace('\n', '').replace('\r', '').replace(',', '')
    elif texttype == TextType.DATE:
        replacedText = text.replace('\t', '').replace('\n', '').replace('\r', '').replace('\xa0','')\
            .replace(',', '').replace('/','').replace('.','-').replace("(","").replace('  ',' ')\
            .replace(")","").replace('DATE : ','').replace('READ : ','')\
            .replace('일','').replace('월','').replace('화','').replace('수','').replace('목','').replace('금','').replace('토', '')\
            .replace("작성 : ", "")
    elif texttype == TextType.INT:
        replacedText = text.replace('\t', '').replace('\n', '').replace('\r', '').replace(',', '')\
            .replace('조회: ','').replace('READ : ','').replace('조회: ','').replace('추천 ','').replace('/','')
    elif texttype == TextType.TEXT:
        replacedText = text.replace('\xa0','').replace('\t', '').replace('\n', '').replace('\r', '')
    else:
        replacedText = text.replace('\t', '').replace('\n', '').replace('\r', '')
    return replacedText

def createItemUseXpath(select, xpath, texttype):
    origin = select.xpath(xpath).extract()
    conversion = replaceText(" ".join(origin), texttype)
    return conversion

def createItemUseBs4(url, name, attr,texttype, encoding):
    JoinPostUrl = BeautifulSoup(requests.get(url).content, "html.parser", from_encoding=encoding)
    try:
        origin = JoinPostUrl.find(name=name, attrs=attr).text.strip()
        conversion = replaceText(origin, texttype)
    except AttributeError as e:
        print(e)
        conversion = ""
    return conversion

def getCurrentTime(returntype):
    currentTime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")  # type of String
    if returntype == TextType.STRING:
        return currentTime
    else:
        currentTime = datetime.strptime(currentTime,"%Y-%m-%d %H:%M:%S")
        return currentTime

def getPostTime(postdate, returntype):
    if returntype == TextType.STRING:
        return postdate
    else:
        postTime = datetime.strptime(postdate,"%Y-%m-%d %H:%M:%S")
        return postTime

def createItem_pop(postdate, postrecommened, posthits):
    # 한시간당 가중치 감소(시간으로 조회수 나눔)
    postOpeningTime = (getCurrentTime("datetime") - getPostTime(postdate, "datetime")).total_seconds() / 3600

    # 인기도 계산 -> 저장
    if (postOpeningTime <= 0):
        postOpeningTime = 1
        postPop = int(postrecommened) + ((int(posthits) / postOpeningTime))
        return postPop
    else:
        postPop = int(postrecommened) + ((int(posthits) / postOpeningTime))
        return postPop

