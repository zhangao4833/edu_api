# -*- coding: utf-8 -*-

from models import db
from sqlalchemy import Column, Integer, String, Text, ForeignKeyConstraint


class BaseModel(db.Model):
    __abstract__ = True  # 作用：不会创建作为普通模型的对应表
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(20), nullable=False, unique=True)


# 模型之间的关系不需要创建第三个模型来实现第三张关系表创建
# 创建用户和角色的关系表
user_role = db.Table('user_role', Column('user_id', Integer, db.ForeignKey('user.id')),
                     Column('role_id', Integer, db.ForeignKey('role.id')))

role_privilege = db.Table('role_privilege', Column('role_id', Integer, db.ForeignKey('role.id')),
                          Column('privilege_id', Integer, db.ForeignKey('privilege.id')))


class Privilege(BaseModel):
    __tablename__ = 'privilege'


class Role(BaseModel):
    __tablename__ = 'role'
    privileges = db.relationship(Privilege, secondary=role_privilege, backref='privileges')


class User(db.Model):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True, autoincrement=True)
    phone = Column(String(20), nullable=False, unique=True)
    auth_key = Column(String(100), nullable=False)
    nick_name = Column(String(20))
    photo = Column(String(100))
    # many_to_many多对多关系，建议使用第三关系表Table()
    # relationship() 指定关系表对象secondary
    roles = db.relationship(Role, secondary=user_role, backref='roles')
