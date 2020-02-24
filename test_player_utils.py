# -*- coding: utf-8 - *-
from crawler.items.player import Player
from crawler import player_utils as pu
import datetime as dt


def mock_player():
    player = Player()
    player["npb_id"] = 'http://p.npb.jp/players_photo/2020/180/db/011_51155136.jpg'
    player["team_en"] = "横浜DeNAベイスターズ"
    player["height"] = "170cm／76kg"
    player["weight"] = "170cm／76kg"
    player["bats"] = "左投左打"
    player["throws"] = "左投左打"
    player["draft_year"] = "2017年ドラフト1位'"
    player["draft_no"] = "2017年ドラフト1位'"
    player["born"] = "1995年1月29日"
    player["age"] = "1995年1月29日"
    return player


def test_replace_none_to_space():
    player = Player()
    player["npb_id"] = ''
    player["no"] = None
    pu.replace_none_to_space(player)
    assert player["npb_id"] == ' ' and player["no"] == ' '


def test_reshape_npb_id():
    player = mock_player()
    reshape_npb_id = pu.reshape_npb_id(player["npb_id"])
    assert reshape_npb_id == '51155136'


def test_reshape_team_en():
    player = mock_player()
    reshape_team_en = pu.reshape_team_en(player["team_en"])
    assert reshape_team_en == 'dena'


def test_reshape_height():
    player = mock_player()
    reshape_height = pu.reshape_height(player["height"])
    assert reshape_height == '170'


def test_reshape_weight():
    player = mock_player()
    reshape_weight = pu.reshape_weight(player["weight"])
    assert reshape_weight == '76'


def test_reshape_bats():
    player = mock_player()
    reshape_bats = pu.reshape_bats(player["bats"])
    assert reshape_bats == '左'


def test_reshape_throws():
    player = mock_player()
    reshape_throws = pu.reshape_throws(player["throws"])
    assert reshape_throws == '左'


def test_reshape_draft_year():
    player = mock_player()
    reshape_draft_year = pu.reshape_draft_year(player["draft_year"])
    assert reshape_draft_year == '2017'


def test_reshape_draft_no():
    player = mock_player()
    reshape_draft_no = pu.reshape_draft_no(player["draft_no"])
    assert reshape_draft_no == '1'


def test_reshape_born():
    player = mock_player()
    reshape_born = pu.reshape_born(player["born"])
    assert reshape_born == '1995-01-29'


def test_reshape_age():
    player = mock_player()
    reshape_age = pu.reshape_age(player["age"])
    assert_age = int(dt.datetime.today().year) - 1995
    assert reshape_age == str(assert_age)


def test_reshape_seasons():
    reshape_seasons = pu.reshape_seasons([0]*10)
    assert reshape_seasons == 8


def test_init_player_table():
    table = pu.init_player_table()
    assert table.table_name == 'player'


def test_table_keys():
    player = Player()
    player["npb_id"] = '51155136'
    player["team_en"] = "dena"
    table_keys = pu.table_keys(player)
    assert table_keys == {'npb_id': '51155136', 'team_en': 'dena'}


def test_is_not_array_param():
    is_not_array_param = pu.is_not_array_param('no')
    assert is_not_array_param
    is_not_array_param = pu.is_not_array_param('seasons')
    assert not is_not_array_param
