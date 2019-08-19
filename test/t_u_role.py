# -*- coding: utf-8 -*-
import hashlib

from mainapp import app
from utils.crypt import pwd
from models.user import *


def add_user():
    u1 = User(phone='11111111112', auth_key=pwd('123'), nick_name='tom', photo='img/2.jpg')
    db.session.add(u1)
    db.session.commit()


def add_role():
    r1 = Role(name='系统管理员')
    r2 = Role(name='普通用户')
    db.session.add_all((r1, r2))
    db.session.commit()


def user_role():
    # db.Table()不能作为模型类使用
    # db.session.add_all(
    #     (user_role(user_id=1, role_id=1), user_role(user_id=2, role_id=1), user_role(user_id=2, role_id=2)))
    u = User.query.get(1)


if __name__ == '__main__':
    app.app_context().push()
    db.init_app(app)
    user_role()
