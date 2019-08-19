# -*- coding: utf-8 -*-
from flask import render_template

from mainapp import app
from mainapp.views import user_v
from flask_script import Manager
from models.user import db

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
