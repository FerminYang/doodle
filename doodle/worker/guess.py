#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import re
import random
from flask import g, session
from config import constellations

def guess(id):
    ##########个别明星特殊处理###################
    if id == 1304194202:
        return 2, 100, None
    if id == 1315469422:
        return 8, 100, None
    if id == 1739928273:
        return 10, 100, None
    #############################################

    #获取微博列表
    #count为每页消息数量，page为从1开始计数的页码
    count = 200
    page = 1
    try:
        timeline = g.api.user_timeline( id = id,
                                      count = count, 
                                      page = page)
    except:
        return -1, 0, u"你妹的微博，又掉链子了(>_<)"

    text_list = []
    rt_text_list = []
    for status in timeline:

        text = status.text.split("//")[0]

        retweeted_status = getattr( status, 
                         "retweeted_status", None )
        if retweeted_status:
            rt_text = retweeted_status.text
        else:
            rt_text = ""

        p = re.compile(u'@猜猜你' + '|' + u'#猜猜你#')
        if len(p.findall(text)) or len(p.findall(rt_text)):
            continue

        text_list.append(text)
        rt_text_list.append(rt_text)

    text_all = '|'.join(text_list)
    rt_text_all = '|'.join(rt_text_list)
    
    text_all = re.sub(u"@[\u2E80-\u9FFF1-9a-zA-Z\-_]*", "", text_all)
    text_all = re.sub(u"[处處]女[作地情节膜秀]|非处女|[骑騎舞][狮獅]子", "", text_all)
    rt_text_all = re.sub(u"@[\u2E80-\u9FFF1-9a-zA-Z\-_]*", "", rt_text_all)
    rt_text_all = re.sub(u"[处處]女[作地情节膜秀]|非处女|[骑騎舞][狮獅]子", "", rt_text_all)

    p = re.compile(u"[俺我][^不]{0,3}是.{0,5}[摩魔水双雙白牡双雙狮獅处處天射][羯瓶鱼魚羊子女蝎蠍手]")
    is_me = p.findall(text_all)
    p = re.compile(u"[俺我].{0,3}不是[摩魔水双雙白牡双雙狮獅处處天射][羯瓶鱼魚羊子女蝎蠍手]")
    is_not_me = p.findall(text_all)


    for constellation in constellations:
        p = re.compile(constellation[1])
        if constellation[1] == u'摩羯':
            p = re.compile(u'摩羯' + '|' + u'魔羯' +  '|' + u'山羊')
        if constellation[1] == u'水瓶':
            p = re.compile(u'水瓶' + '|' + u'宝瓶' +  '|' + u'寶瓶')
        if constellation[1] == u'双鱼':
            p = re.compile(u'双鱼' + '|' + u'雙魚')
        if constellation[1] == u'白羊':
            p = re.compile(u'白羊' + '|' + u'牡羊')
        if constellation[1] == u'双子':
            p = re.compile(u'双子' + '|' + u'雙子')
        if constellation[1] == u'狮子':
            p = re.compile(u'狮子' + '|' + u'獅子')
        if constellation[1] == u'处女':
            p = re.compile(u'处女' + '|' + u'處女' +  '|' + u'室女')
        if constellation[1] == u'天蝎':
            p = re.compile(u'天蝎' + '|' + u'天蠍')
        if constellation[1] == u'射手':
            p = re.compile(u'射手' + '|' + u'人馬')

        if len(is_me) > 0:
            for x in is_me:
                constellation[2] += 7 * len(p.findall(x)) 
        if len(is_not_me) > 0:
            for x in is_not_me:
                m = len(p.findall(x))
                constellation[2] -= 13 * len(p.findall(x))

        constellation[2] += 3 * len(p.findall(text_all))

        if rt_text_all != "":
            constellation[2] += len(p.findall(rt_text_all))
    constellations.sort(key=lambda i:i[2], reverse=True)
    if constellations[0][2] > constellations[1][2]:   
        return constellations[0][0], 90, None
	if constellations[0][2] > 0 and constellations[0][2] == constellations[1][2]:
		return constellations[0][0], 60, None
    x = id % 12
    #x = int(random.randint(0, 11))
    return constellations[x][0], 30, None
