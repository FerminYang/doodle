#!/usr/bin/env python
#coding=utf-8

DEBUG = True
SAE = False

SECRET_KEY = 'fdst34t43fsdarf345asf9(^(%^3efds'

APP_KEY = '3480428999'
APP_SECRET = '1a19d21622a45d0ea93ab0b3c2c507b3'
BACK_URL = 'http://caicaini.com:7777/auth/callback'

if SAE:
    import sae.const
    host = sae.const.MYSQL_HOST
    user = sae.const.MYSQL_USER
    passwd = sae.const.MYSQL_PASS
    db_name = sae.const.MYSQL_DB
    port = int(sae.const.MYSQL_PORT)    
else:
    host = 'localhost'
    user = 'root'
    passwd = '123456'
    db_name = 'doodle'
    port = 3306

constellations = [[0, u'摩羯', 0], [1, u'水瓶', 0], [2, u'双鱼', 0], [3, u'白羊', 0], [4, u'金牛', 0], [5, u'双子', 0], [6, u'巨蟹', 0], [7, u'狮子', 0], [8, u'处女', 0], [9, u'天>秤', 0], [10, u'天蝎', 0], [11, u'射手', 0]]
