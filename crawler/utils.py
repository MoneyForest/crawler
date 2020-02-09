# -*- coding: utf-8 -*-
import os

def is_development():
    return os.environ['ENV'] == 'development'

def stlip_space_crlf(s):
    dic = str.maketrans({' ': '', '\n': '', '\r': '', '\u3000': ' ', '・': ' '})
    return s.translate(dic)

def reshape_npb_id(s):
    return s.split('_')[2].split('.')[0]

def reshape_height(s):
    return s.split('／')[0]

def reshape_weight(s):
    return s.split('／')[1]

def reshape_throw(s):
    return s.split('投')[0]

def reshape_bat(s):
    return s.split('投')[1].split('打')[0]

def reshape_draft_year(s):
    return s.split('年')[0]

def reshape_draft_no(s):
    return s.split('ドラフト')[1].split('位')[0]
