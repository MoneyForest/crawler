# -*- coding: utf-8 -*-
import os


def is_development():
    return os.environ['ENV'] == 'development'


def stlip_space_crlf(s):
    dic = str.maketrans({' ': '', '\n': '', '\r': '', '\u3000': ' ', '・': ' '})
    return s.translate(dic)
