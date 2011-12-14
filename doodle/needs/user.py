#!/usr/bin/env python
#coding=utf-8

from flask import g, render_template, session

def need_login(func):
    def is_logined(*args, **kwargs):
        if g.user:
            return func(*args, **kwargs)
        else:
            if 'id' in session:
                del session['id']
                session.permanent = False
            g.user = None
            g.weibo = None
            return render_template('errors/need_login.html')
    return is_logined
