# -*- coding: utf-8 -*-

from flask import Blueprint
from flask import request, render_template, redirect

blue = Blueprint('userBlue', __name__)


@blue.route('/login/', methods=['GET', 'POST'])
def login():
    data = {
        'cookies': request.cookies,
        'base_url': request.host_url
    }
    return render_template('user/login.html', **data)
