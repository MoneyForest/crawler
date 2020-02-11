# -*- coding: utf-8 -*-
import scrapy
import json
from .. import utils
from crawler.items.player import Player

class PlayerSpider(scrapy.Spider):
    name = 'player'

    def __init__(self):
        self.allowed_domains = ['npb.jp']
        self.start_urls = ['http://npb.jp/bis/teams/']

    def parse(self, response):
        yield scrapy.Request(self.start_urls[0], self.crawl_npb_url)

    def crawl_npb_url(self, response):
        TEAM_URLS = response.xpath("//*[@id='team_list']/div/ul/li/a/@href")

        for n, TEAM_URL in enumerate(TEAM_URLS):
            if utils.is_development() and n > 0: return

            URL = response.urljoin(TEAM_URL.extract())
            yield scrapy.Request(URL, self.crawl_team_url)

    def crawl_team_url(self, response):
        PLAYER_URLS = response.xpath("//*[@class='rosterRegister']/a/@href")

        for n, PLAYER_URL in enumerate(PLAYER_URLS):
            if utils.is_development() and n > 0: return

            URL = response.urljoin(PLAYER_URL.extract())
            yield scrapy.Request(URL, self.crawl_player_url)

    def crawl_player_url(self, response):

        def parse_player_item(player):
            with open('xpath/player.json', 'r') as f:
                player_json = json.load(f)
                for key in player_json.keys():
                    val = ''.join(response.xpath(player_json[key]).extract())
                    player[key] = utils.stlip_space_crlf(val)

        def reshape_player_item(player):
            player['npb_id'] = utils.reshape_npb_id(player['npb_id'])
            player['height'] = utils.reshape_height(player['height'])
            player['weight'] = utils.reshape_weight(player['weight'])
            player['born'] = utils.reshape_born(player['born'])
            player['age'] = utils.reshape_age(player['age'])
            player['throws'] = utils.reshape_throw(player['throws'])
            player['bats'] = utils.reshape_bat(player['bats'])
            player['draft_year'] = utils.reshape_draft_year(player['draft_year'])
            player['draft_no'] = utils.reshape_draft_no(player['draft_no'])

        player = Player()
        parse_player_item(player)
        reshape_player_item(player)
        print(player)
