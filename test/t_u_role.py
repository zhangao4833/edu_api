# -*- coding: utf-8 -*-
import hashlib

from mainapp import app
from utils.crypt import pwd
from models.user import *


def add_user():
    u1 = User(phone='11111111113', auth_key=pwd('123123123'), nick_name='tom', photo='img/3.jpg')
    db.session.add(u1)
    db.session.commit()


def add_role():
    r1 = Role(name='系统管理员')
    r2 = Role(name='普通用户')
    db.session.add_all((r1, r2))
    db.session.commit()


def add_privilege():
    db.session.add_all((Privilege(name='delete_user'), Privilege(name='create_user'), Privilege(name='read_user'),
                        Privilege(name='update_user'), Privilege(name='create_db'),
                        Privilege(name='drop_db')))
    db.session.commit()


def add_user_role():
    # db.Table()不能作为模型类使用
    # db.session.add_all(
    #     (user_role(user_id=1, role_id=1), user_role(user_id=2, role_id=1), user_role(user_id=2, role_id=2)))
    u = User.query.get(1)
    u.roles.append(Role.query.get(1))
    u.roles.append(Role.query.get(2))
    db.session.commit()


def query_user_role(user_id=1):
    u = User.query.get(user_id)
    for u_r in u.roles:
        print(u_r.name)


def add_role_privilege():
    admin = Role.query.filter(Role.name.__eq__('系统管理员')).one()
    print(admin)
    # print(Privilege.query.all())
    for p in Privilege.query.all():
        admin.privileges.append(p)
    db.session.commit()
def query_role_privilege(role_name='系统管理员'):
    for r in Role.query.filter(Role.name.__eq__(role_name)).one().privileges:
        print(r.name)


if __name__ == '__main__':
    app.app_context().push()
    db.init_app(app)
    add_user()
    # add_role()
    # add_user_role()
    # query_user_role()
    # add_privilege()
    # add_role_privilege()
    # query_role_privilege()