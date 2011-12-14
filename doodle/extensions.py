#!/usr/bin/env python
#coding=utf-8

from autumn.db.connection import autumn_db
from weibopy.auth import OAuthHandler
from config import host, user, passwd, db_name, port
from config import APP_KEY, APP_SECRET, BACK_URL

db = autumn_db.conn.connect('mysql', host=host, user=user, passwd=passwd, db=db_name, port=port, charset='utf8')
auth_client = OAuthHandler( APP_KEY, APP_SECRET, BACK_URL)

def db_check(db):
    try:
        db.ping()
    except:
        db = autumn_db.conn.connect('mysql', host=host, user=user, passwd=passwd, db=db_name, port=port, charset='utf8')
    return db

def weibo_txt(fans, screen_name, constellation, rate):
    if fans:
        if rate > 60:
            message = '@' + screen_name + u' 虽然不知道你的生日，但从你的性格我可以猜出你是#'+ constellation +u'座#的。想知道你默默关注的人是个什么星座吗？快来#猜猜你#测一下吧 '
        if rate == 60:
            message = '@' + screen_name + u' 虽然不知道你的生日，但从你的性格我可以猜出你是#'+ constellation +u'座#的。想知道你默默关注的人是个什么星座吗？快来#猜猜你#测一下吧 '
        if rate < 60:
            message = '@' + screen_name + u' 亲，你知道吗，今日非常适宜才子佳人相会，不过先要知道你是不是#' + constellation +u'座#的？如果你想知道我是个什么星座的，那就来#猜猜你#测一下吧 '
    else:
        message = u'真是神奇的网站，任何微博用户，甚至苍井空的星座都可以猜到啊！！！'
    
    return message

