# -*- coding: utf-8 -*-
import os
import datetime as dt

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

def reshape_born(s):
    birthday = dt.datetime.strptime(s, '%Y年%m月%d日')
    return birthday.strftime('%Y-%m-%d')

def reshape_age(s):
    birth_year = s.split('年')[0]
    season_year = 2019
    age = int(season_year) - int(birth_year)
    return age
