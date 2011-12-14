#! /usr/bin/env python
#coding=utf-8

from flask import Module, request, flash, g, render_template, render_template_string, jsonify
from models import Guess, Weibo
import worker.guess
from needs import need_api, need_login
from config import constellations
from extensions import weibo_txt

home = Module(__name__)

@home.route('/', methods=['POST', 'GET'])
def index():
    if g.user:
        return render_template('home.html')
    return render_template('index.html')
        
@home.route('/guess', methods=['POST', 'GET'])
@need_login
@need_api
def guess():
        guessed_name = request.args.get('guessed_name').strip()
        if guessed_name:
                guessed_user, fans = None, False
                try:
                  guessed_user = g.api.get_user(id = guessed_name)
                except:
                    return render_template('guess.html', error=u"纳尼！查无此人)^O^( 你们真的认识吗")
                try:
                    fans = g.api.exists_friendship(user_a = guessed_user.id, user_b = g.weibo.id).friends
                except:
                    return render_template('guess.html', error=u"获取好友关系失败，请稍候再试")
        else:
            return render_template_string('guess.html', error=u"微博昵称不能为空")

        if guessed_user:
            constellation_id, rate, error = worker.guess(id=guessed_user.id)
            if rate <= 30:
                constellation_id, rate, error = worker.guess(id=guessed_user.id)            
            constellation = constellations[constellation_id][1]

            if error:
                return render_template_string('guess.html', error=error)

            Guess.set(guesser_id=g.user.id, guessed_id=guessed_user.id, constellation_id=constellation_id, rate=rate)
            Weibo.set(weibo=guessed_user)
            guessed_weibo = Weibo.get(id=guessed_user.id)[0]
            message = weibo_txt(fans=fans, screen_name=guessed_weibo.screen_name, constellation=constellation, rate=rate)
            rate = str(rate) + "%"
            return render_template('guess.html',constellation=constellation, rate=rate, message=message, error=None, guessed_weibo=guessed_weibo)
        else:
            return render_template_string('guess.html', error=u'无法获取该用户的微博信息')
            
