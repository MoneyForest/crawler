# -*- coding: utf-8 -*-
import json
import datetime as dt
from . import utils


def parse_player_params(player, response):
    with open('crawler/xpath/player.json', 'r') as f:
        player_json = json.load(f)
        for key in player_json.keys():
            val = ''.join(response.xpath(player_json[key]).extract())
            if len(val) != 0:
                player[key] = utils.stlip_space_crlf(val)
            elif key not in player:
                player[key] = ''


def reshape_player_params(player):
    player['npb_id'] = reshape_npb_id(player['npb_id'])
    player['team_en'] = reshape_team_en(player['team_en'])
    player['height'] = reshape_height(player['height'])
    player['weight'] = reshape_weight(player['weight'])
    player['born'] = reshape_born(player['born'])
    player['age'] = reshape_age(player['age'])
    player['throws'] = reshape_throw(player['throws'])
    player['bats'] = reshape_bat(player['bats'])
    player['draft_year'] = reshape_draft_year(player['draft_year'])
    player['draft_no'] = reshape_draft_no(player['draft_no'])
    player['blood_type'] = reshape_blood_type(player['blood_type'])
    player['salary'] = reshape_salary(player['salary'])


def reshape_npb_id(s):
    return s.split('/')[-1].split('_')[1].split('.')[0]


def reshape_team_en(s):
    with open('crawler/npb.json', 'r') as f:
        return json.load(f)[s]


def reshape_height(s):
    return s.split('／')[0].split('cm')[0]


def reshape_weight(s):
    return s.split('／')[1].split('kg')[0]


def reshape_throw(s):
    return s.split('投')[0]


def reshape_bat(s):
    return s.split('投')[1].split('打')[0]


def reshape_draft_year(s):
    return s.split('年')[0]


def reshape_draft_no(s):
    if not s:
        return
    return s.split('ドラフト')[1].split('位')[0].split('巡目')[0]


def reshape_born(s):
    birthday = dt.datetime.strptime(s, '%Y年%m月%d日')
    return birthday.strftime('%Y-%m-%d')


def reshape_age(s):
    birth_year = s.split('年')[0]
    season_year = 2019
    age = int(season_year) - int(birth_year)
    return str(age)


def reshape_blood_type(s):
    return s.split('型')[0]


def reshape_salary(s):
    return s.split('万円')[0].replace('億', '')


def build_sanspo_url(team_ja, no):
    with open('crawler/npb.json', 'r') as f:
        npb_json = json.load(f)
        base_url = "https://www.sanspo.com/baseball/professional/player/"
        return base_url + npb_json[team_ja] + "/" + no + ".html"


def is_same_player(player, player_name):
    return player_name in player['name']
