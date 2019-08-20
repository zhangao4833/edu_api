# -*- coding: utf-8 -*-
import os

PRO_DIR = os.path.dirname(os.path.abspath(__file__))
BASE_DIR = os.path.join(PRO_DIR, 'mainapp')
STATIC_DIR = os.path.join(BASE_DIR, 'static')
USER_DIR = os.path.join(STATIC_DIR, 'user')

class Dev:
    ENV = 'development'
    DEBUG = True

    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:root@10.36.174.19:3306/imooc?charset=utf8'
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    SQLALCHEMY_ECHO = True
