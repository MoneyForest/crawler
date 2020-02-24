# -*- coding: utf-8 -*-
from crawler import utils
import os


def test_is_development():
    assert isinstance(utils.is_development(), bool)
    os.environ['ENV'] = 'development'
    assert utils.is_development()
    os.environ['ENV'] = 'production'
    assert not utils.is_development()


def test_to_strip():
    s = '\u3000・'
    assert '  ' == utils.to_space(s)


def test_stlip():
    s = ' \r\n'
    assert '' == utils.stlip(s)
