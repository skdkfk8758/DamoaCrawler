"""
Item 객체에 데이터를 구성해주는 클래스
Create : 2017.10.09

"""

import requests
import math
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
            .replace("작성 : ", "").replace(".","-")
    elif texttype == TextType.INT:
        replacedText = text.replace('\t', '').replace('\n', '').replace('\r', '').replace(',', '')\
            .replace('조: ','').replace('READ : ','').replace('회: ','').replace('추천 ','').replace('/','').replace("수","").replace("조회","").replace("댓글","")\
            .replace('조', '')
    elif texttype == TextType.TEXT:
        replacedText = text.replace('\xa0','').replace('\t', '').replace('\n', '').replace('\r', '')
    elif texttype == TextType.CLIEN:
        replacedText = text.replace('f', '').replace('a', '').replace('b', '').replace('l', '').replace('i', '').replace('n', '')\
            .replace('o', '').replace('d', '').replace('t', '').replace('u', '').replace('p','')
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
        print("Attr Error : " + str(e))
        conversion = ""
    return conversion

def createItemUseBs4_PostImage(url):
    JoinPostUrl = BeautifulSoup(requests.get(url).content, "html.parser")
    try:
        img = JoinPostUrl.find("img").get("src")
        conversion = img
    except AttributeError as e:
        print("Attr Error : " + str(e))
        conversion = None
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

def createItem_pop(postDate, postRecommened, postHits):
    time = int((getCurrentTime("datetime") - getPostTime(postDate, "datetime")).total_seconds() / 3600)
    hit = int(postHits)
    recc = int(postRecommened)

    if time < 1:
        time = 1
        pop = (((hit / 100) / time) + (recc / time))

    else:
        pop = (((hit / 100) / time) + (recc / time))

    return (math.sqrt(pop))
    # return pop

