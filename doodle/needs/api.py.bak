#!/usr/bin/env python
#coding=utf-8

from flask import g, render_template, session
from extensions import auth_client
from weibopy.api import API

def need_api(func):
    def api_verify(*args, **kwargs):
        if g.api:
            return func(*args, **kwargs)
        else:
            if g.weibo:
                if g.weibo.at_key and g.weibo.at_secret:
                    auth_client.setToken(g.weibo.at_key, g.weibo.at_secret)
                    api =  API(auth_client)
                    weibo = api.verify_credentials()
                    if weibo:
                        g.api = api
                        return func(*args, **kwargs)
     
        if 'id' in session:
            del session['id']
            session.permanent = False
        g.user = None
        g.weibo = None
        return render_template('errors/need_api.html')
    return api_verify
