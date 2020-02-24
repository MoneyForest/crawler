# -*- coding: utf-8 -*-
from crawler import utils
import os


def test_is_development():
    assert isinstance(utils.is_development(), bool)
    os.environ['ENV'] = 'development'
    assert utils.is_development()
    os.environ['ENV'] = 'production'
    assert not utils.is_development()


def test_stlip():
    s = ' \u3000\r\n・'
    assert '' == utils.stlip(s)
