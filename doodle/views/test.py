#! /usr/bin/env python
#coding=utf-8

import datetime
from flask import Module, render_template, jsonify, request
from autumn.db.query import Query
from models import Weibo

test = Module(__name__)

@test.route('/')
def index():
    return render_template('test.html')

@test.route('/query', methods=['POST', 'GET'])
def query():
    name = ('童晓白','tinyfool')
    print name
    sql = 'select * from weibo where screen_name in %s' %str(name)
    print 'sql = %s' %sql
    sql = 'select * from weibo where screen_name in("童晓白","tinyfool")'
    print 'sql = %s' %sql
    q = Query(model=Weibo).sql(sql)
    for qu in q:
        print 'qu = %s' %qu['screen_name']
    return render_template('query.html')

@test.route('/jquery', methods=['POST', 'GET'])
def jquery():
    if request.method == 'POST':
        a =5
        return jsonify(result=a)
