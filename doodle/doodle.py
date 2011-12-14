#!/usr/bin/env python
#coding=utf-8

from flask import Flask, Module, request, session, \
json, url_for, render_template, redirect, flash, g
from extensions import db, db_check
from config import SECRET_KEY
import views
from  models import User, Weibo

DEFAULT_APP_NAME = 'doodle'

DEFAULT_MODULES = (
    (views.home, ''),
    (views.auth, '/auth'),
    (views.test, '/test')
)

def create_app(config=None, modules=None):
    if modules is None:
        modules = DEFAULT_MODULES   
    
    app = Flask(DEFAULT_APP_NAME)
    app.secret_key = SECRET_KEY
    
    configure_modules(app, modules) 
    configure_before_handlers(app)
    configure_teardown_handlers(app)
    configure_errorhandlers(app)

    return app

def configure_modules(app, modules):
    for module, url_prefix in modules:
        app.register_module(module, url_prefix=url_prefix)

def configure_before_handlers(app):

    @app.before_request
    def before_request():
        db_check(db) 
        if 'id' in session:
            g.user = User.get(id=session['id'])[0]
            g.weibo = Weibo.get(id=session['id'])[0]
        else:
            g.user = None
            g.weibo = None 

        g.api = None

def configure_teardown_handlers(app):

    @app.teardown_request
    def teardown_request(exception):
        pass

def configure_errorhandlers(app):

    @app.errorhandler(401)
    def unauthorized(error):
        if request.is_xhr:
            return json.dumps({'error':'Login required'})
        flash('Please login to see this page', 'error')
        return redirect(url_for('login', next=request.path))
  
    @app.errorhandler(403)
    def forbidden(error):
        if request.is_xhr:
            return jsonify({'error':'Sorry, page not allowed'})
        return render_template('errors/403.html', error=error)

    @app.errorhandler(404)
    def page_not_found(error):
        if request.is_xhr:
            return json.dumps({'error':'Sorry, page not found'})
        return render_template('errors/404.html', error=error)

    @app.errorhandler(500)
    def server_error(error):
        if request.is_xhr:
            return json.dumps({'error':'Sorry, an error has occurred'})
        return render_template('errors/500.html', error=error)

def configure_modules(app, modules):
    for module, url_prefix in modules:
        app.register_module(module, url_prefix=url_prefix)

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True, host='0.0.0.0', port=7777)
