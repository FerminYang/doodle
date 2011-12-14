#!/usr/bin/env python
#coding=utf-8

from autumn.model import Model

class Weibo(Model):
    class Meta:
        defaults = {'at_key': '',
                    'at_secret': '',}

    @classmethod
    def set(cls, weibo, at_key='', at_secret=''):
        '''记录用户微博资料'''
        q = Weibo.get(id=weibo.id)[0]
        if q:
            if at_key and at_secret:
                q.at_key = at_key
                q.at_secret = at_secret
            q.screen_name = weibo.screen_name
            q.domain = weibo.domain
            q.profile_image_url = weibo.profile_image_url
            q.save()
        else:
            i = Weibo(id=weibo.id, at_key=at_key, at_secret=at_secret, screen_name = weibo.screen_name, domain = weibo.domain, profile_image_url = weibo.profile_image_url)
            i.save()

