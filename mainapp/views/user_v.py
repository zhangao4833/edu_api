# -*- coding: utf-8 -*-
import os
import uuid

from flask import Blueprint, jsonify
from flask import request, render_template, redirect
from werkzeug.datastructures import FileStorage

import settings
from models import db
from models.user import User
from utils import cache
from utils.crypt import pwd
from datetime import datetime, timedelta

blue = Blueprint('userBlue', __name__)


@blue.route('/modify/', methods=['GET', 'POST'])
def modify():
    token = request.cookies.get('token')
    user_id = cache.get_user_id(token)
    msg = ''
    # 任务1： 优化登陆用户的相关信息存在redis中（缓存）
    user = User.query.get(int(user_id))
    if request.method == 'POST':
        # 头像上传
        # 获取上传的文件
        photo: FileStorage = request.files.get('user_photo')
        # print(photo.filename)
        # print(photo.content_length)
        # print(photo.content_type)
        # 验证文件是否是图片
        if not photo.content_type.startswith('image/'):
            msg = '只支持图片上传！'
        else:
            # 保存图片
            filename = uuid.uuid4().hex + os.path.splitext(photo.filename)[-1]
            filepath = os.path.join(settings.USER_DIR, filename)
            # 服务端保存上传的文件
            photo.save(filepath)
            # 更新用户
            # 保存在数据库的图片是相对static资源访问的路径
            user.photo = 'user/' + filename
            db.session.commit()
    return render_template('user/info.html', user=user, msg=msg)


@blue.route('/upload/', methods=['POST'])
def upload():
    return jsonify({
        'msg': '上传成功',
        'path': 'user/ms1.jpg'
    })


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
