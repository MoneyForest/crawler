# -*- coding: utf-8 -*-
import scrapy
import json
from .. import utils
from crawler.items import Player

class PlayerSpider(scrapy.Spider):
    name = 'player'

    def __init__(self):
        self.allowed_domains = ['npb.jp']
        self.start_urls = ['http://npb.jp/bis/teams/']

    def parse(self, response):
        yield scrapy.Request(self.start_urls[0], self.crawl_npb_url)

    def crawl_npb_url(self, response):
        TEAMS_URLS = response.xpath("//*[@id='team_list']/div/ul/li/a/@href")

        for n, TEAM_URL in enumerate(TEAMS_URLS):
            if utils.is_development() and n > 0: return

            URL = response.urljoin(TEAM_URL.extract())
            yield scrapy.Request(URL, self.crawl_team_url)

    def crawl_team_url(self, response):
        PLAYERS_URLS = response.xpath("//*[@class='rosterRegister']/a/@href")

        for n, PLAYER_URL in enumerate(PLAYERS_URLS):
            if utils.is_development() and n > 0: return

            URL = response.urljoin(PLAYER_URL.extract())
            yield scrapy.Request(URL, self.parse_player_item)


    def parse_player_item(self, response):

        def player_item(player, str):
            with open('xpath/player_xpath.json', 'r') as f:
                player[str] = response.xpath(json.load(f)[str]).extract()

        player = Player()
        player_item(player, 'no')
        player_item(player, 'team')
        player_item(player, 'name')
        player_item(player, 'kana')
        player_item(player, 'position')
        player_item(player, 'bat_and_throw')
        player_item(player, 'height_and_weight')
        player_item(player, 'birth')
        player_item(player, 'carrer')
        player_item(player, 'draft')

        print(player)