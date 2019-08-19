# -*- coding: utf-8 -*-
import uuid

from flask import Blueprint
from flask import request, render_template, redirect
from models.user import User
from utils import cache
from utils.crypt import pwd
from datetime import datetime, timedelta

blue = Blueprint('userBlue', __name__)


@blue.route('/login/', methods=['GET', 'POST'])
def login():
    massege = None
    if request.method == 'POST':
        phone = request.form.get('phone')
        password = request.form.get('password')
        try:
            login_user = User.query.filter(User.phone == phone, User.auth_key == pwd(password)).one()
        except:
            login_user = None
        if login_user:
            # 登陆成功
            # 生成token
            token = uuid.uuid4().hex
            resp = redirect('/')
            resp.set_cookie('token', token, expires=(datetime.now() + timedelta(days=3)))
            cache.save_token(token, login_user.id)
            # 将token添加到redis，token-user_id
            return resp
        else:
            # 登陆失败
            massege = '查无此用户'
    return render_template('user/login.html', msg=massege)


@blue.route('/logout/')
def logout():
    # 删除redis中的token
    token = request.cookies.get('token')
    cache.clear_token(token)
    # 删除cookie
    resp = redirect('/login/')
    resp.delete_cookie('token')

    return resp
