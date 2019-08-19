# -*- coding: utf-8 -*-
import hashlib

from mainapp import app
from utils.crypt import pwd
from models.user import *

if __name__ == '__main__':
    app.app_context().push()
    db.init_app(app)
    u1 = User(phone='11111111112', auth_key=pwd('123'), nick_name='tom', photo='img/2.jpg')
    db.session.add(u1)
    db.session.commit()
