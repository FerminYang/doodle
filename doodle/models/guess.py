#!/usr/bin/env python
#coding=utf-8

from autumn.model import Model
from weibo import Weibo
from user import User
import datetime

class Guess(Model):

    class Meta:
        defaults = {'rate': 0,
                    'count': 0}

    @classmethod
    def set(cls, guesser_id, guessed_id, constellation_id, rate):
        '''记录猜星座记录'''
        q = Guess.get(guesser_id=guesser_id, guessed_id=guessed_id)[0]
        now = datetime.datetime.now()
        if q:
            q.constellation_id = constellation_id
            q.rate = rate
            q.datetime = now
            q.count = q.count + 1
            q.save()
        else:
            i = Guess(guesser_id=guesser_id, guessed_id=guessed_id, constellation_id=constellation_id, rate=rate, datetime = now, count=1)
            i.save()
            User.guesser(id=guesser_id)
            User.guessed(id=guessed_id) 
