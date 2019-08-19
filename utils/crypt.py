# -*- coding: utf-8 -*-
import hashlib


def pwd(text):
    md5_ = hashlib.md5()
    md5_.update(text.encode('utf-8'))
    md5_.update('@jack#nk*&^jkw'.encode('utf-8'))
    return md5_.hexdigest()


if __name__ == '__main__':
    print(pwd('123123123'))
