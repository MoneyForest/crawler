# -*- coding: utf-8 -*-
import json
import boto3
import datetime as dt
from . import utils


def parse_player_params(player, response):
    with open('crawler/xpath/player.json', 'r') as f:
        player_json = json.load(f)
        for key in player_json.keys():
            val = response.xpath(player_json[key]).extract()
            if is_not_array_param(key):
                val = utils.to_space(utils.stlip(''.join(val)))
            if len(val) != 0:
                player[key] = val
            elif key not in player:
                player[key] = ' '


def reshape_player_params(player):
    player['npb_id'] = reshape_npb_id(player['npb_id'])
    player['team_en'] = reshape_team_en(player['team_en'])
    player['height'] = reshape_height(player['height'])
    player['weight'] = reshape_weight(player['weight'])
    player['born'] = reshape_born(player['born'])
    player['age'] = reshape_age(player['age'])
    player['throws'] = reshape_throws(player['throws'])
    player['bats'] = reshape_bats(player['bats'])
    player['draft_year'] = reshape_draft_year(player['draft_year'])
    player['draft_no'] = reshape_draft_no(player['draft_no'])
    player['seasons'] = reshape_seasons(player['seasons'])


def replace_none_to_space(player):
    for key in player.keys():
        if player[key] is None or player[key] == '':
            player[key] = ' '
    return player


def reshape_npb_id(s):
    return s.split('/')[-1].split('_')[1].split('.')[0]


def reshape_team_en(s):
    with open('crawler/npb.json', 'r') as f:
        return json.load(f)[s]


def reshape_height(s):
    return s.split('／')[0].split('cm')[0]


def reshape_weight(s):
    return s.split('／')[1].split('kg')[0]


def reshape_throws(s):
    return s.split('投')[0]


def reshape_bats(s):
    return s.split('投')[1].split('打')[0]


def reshape_draft_year(s):
    return s.split('年')[0]


def reshape_draft_no(s):
    if len(s) == 1:
        return
    else:
        return s.split('ドラフト')[1].split('位')[0].split('巡目')[0]


def reshape_born(s):
    birthday = dt.datetime.strptime(s, '%Y年%m月%d日')
    return birthday.strftime('%Y-%m-%d')


def reshape_age(s):
    birth_year = s.split('年')[0]
    season_year = dt.datetime.today().year
    age = int(season_year) - int(birth_year)
    return str(age)


def reshape_seasons(list):
    return len(list) - 2


def init_player_table():
    dynamodb = boto3.resource('dynamodb')
    return dynamodb.Table('player')


def table_keys(player):
    return {'npb_id': player['npb_id'], 'team_en': player['team_en']}


def is_not_array_param(s):
    return 'stats' not in s and 'seasons' not in s
