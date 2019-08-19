# -*- coding: utf-8 -*-
from flask import render_template, request, redirect, url_for

from mainapp import app
from mainapp.views import user_v
from flask_script import Manager
from models.user import db
from utils import cache


@app.before_request
def check_login():
    # 判断request中是否包含token
    # 验证token是否有效
    if request.path != '/user/login/':
        token = request.cookies.get('token')
        if not token:
            return redirect(url_for('userBlue.login'))
        user_id = cache.get_user_id(token)
        if not user_id:
            return redirect(url_for('userBlue.login'))
@app.route('/')
def index():
    return render_template('index.html')



@app.route('/create_db/')
def create_database():
    db.create_all()
    return '创建数据库中的所有模型表成功'


@app.route('/drop_db/')
def drop_database():
    db.drop_all()
    return '删除数据库中的所有模型表成功'


if __name__ == '__main__':
    app.register_blueprint(user_v.blue, url_prefix='/user')
    db.init_app(app)
    manage = Manager(app)
    manage.run()
