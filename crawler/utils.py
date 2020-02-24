# -*- coding: utf-8 -*-
import os


def is_development():
    return os.environ['ENV'] == 'development'


def stlip(s):
    dic = str.maketrans({' ': '', '\u3000': '',  '\r': '', '\n': '', '・': ''})
    return s.translate(dic)
