#!/usr/bin/env python
#coding=utf-8

from flask import g
from autumn.model import Model
from weibo import Weibo
import datetime

class User(Model):

    class Meta:
        defaults = {'constellation_id': 0,
                    'guesser_count': 0,
                    'guessed_count': 0,
                    'score': 0,
                    'rate': 0,
                    'user_count': 0,
                    'user_hit': 0,
                    'user_miss': 0,
                    'star_count': 0,
                    'star_miss': 0,
                    'notice': 0,
                    'role': 0,
                    'status': 0,
                    'login_ip': '' 
                   }

    @classmethod
    def login(cls, weibo):
        '''记录用户登录信息'''
        q = User.get(id=weibo.id)[0]
        now = datetime.datetime.now()
        if q:
            q.login_datetime = now
            if not q.signin_datetime:
                q.signin_datetime = now
            q.save()
        else:
            i = User(id=weibo.id, login_datetime=now, signin_datetime=now)
            i.save()

    @classmethod
    def guesser(cls, id):
        '''猜星座记录+1'''
        q = User.get(id=id)[0]
        if q:
            q.guesser_count += 1
            q.save()
        else:
            i = User(id=weibo.id, guess_count=1)
            i.save()
        g.user = User.get(id=id)[0]

    @classmethod
    def guessed(cls, id):
        '''被猜星座记录+1'''
        q = User.get(id=id)[0]
        if q:
            q.guessed_count += 1
            q.save()
        else:
            i = User(id=id, guessed_count=1)
            i.save()
        if id == g.weibo.id:
            g.user = User.get(id=id)[0]
