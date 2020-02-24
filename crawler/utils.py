# -*- coding: utf-8 -*-
import os


def is_development():
    return os.environ['ENV'] == 'development'


def to_space(s):
    dic = str.maketrans({'\u3000': ' ', '・': ' '})
    return s.translate(dic)


def stlip(s):
    dic = str.maketrans({'\r': '', '\n': '', ' ': ''})
    return s.translate(dic)
