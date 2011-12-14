#! /usr/bin/env python
#coding=utf-8

from flask import Module, request, flash, redirect, session, render_template
from weibopy.api import API
from extensions import auth_client
from models import User, Weibo

auth = Module(__name__)

def _get_referer_url(request):
    referer_url = request.args.get('next','/')
    host = request.path
    if referer_url.startswith('http') and host not in referer_url:
        referer_url = '/' # 避免外站直接跳到登录页而发生跳转错误
    return referer_url

@auth.route('/weibo', methods=['POST', 'GET'])
def weibo():
    # 保存最初的登录url，以便认证成功后跳转回来
    back_to_url = _get_referer_url(request)
    session['login_back_to_url'] = back_to_url
    #获取授权页面网址.
    auth_url = auth_client.get_authorization_url()
    # 保存request_token，用户登录后需要使用它来获取access_token
    session['oauth_request_token'] = auth_client.request_token
    # 跳转到登录页面
    return redirect(auth_url)

@auth.route('/callback')
def callback():
    '''用户成功登录授权后，会回调此方法，获取access_token，完成授权'''
    verifier = request.args.get('oauth_verifier', None)
    # 设置之前保存在session的request_token
    if 'oauth_request_token' in session:
        request_token = session['oauth_request_token']
        del session['oauth_request_token']
    else:
        return render_template('index.html')

    auth_client.set_request_token(request_token.key, request_token.secret)
    access_token = auth_client.get_access_token(verifier)
    at_key = access_token.key
    at_secret = access_token.secret
    #设定用户令牌密钥
    auth_client.setToken( at_key, at_secret )
    #绑定用户验证信息.
    api = API(auth_client)
    #获取微博信息
    weibo = api.verify_credentials()
    if weibo is False or weibo is None:
        flash(u'杯具啊，你木有开通微博吧(⊙﹏⊙)a', 'error')
        return render_template('index.html')

    #记录用户登录信息，更新用户微博资料
    User.login(weibo=weibo)
    Weibo.set(weibo=weibo, at_key=at_key, at_secret=at_secret)
    #设置session
    session['id'] = weibo.id
    session.permanent = True
    # 跳转回最初登录前的页面
    back_to_url = session.get('login_back_to_url', '/')
    return redirect(back_to_url)

@auth.route('/logout', methods=['POST', 'GET'])
def logout():
    '''用户退出，直接删除seesion['id']，清除session记录'''
    if 'id' in session: 
        del session['id']
        session.permanent = False
        back_to_url = _get_referer_url(request)
        return redirect(back_to_url)
