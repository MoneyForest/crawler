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

        def parse_player_item(player, s):
            with open('crawler/xpath/player_xpath.json', 'r') as f:
                text = ''.join(response.xpath(json.load(f)[s]).extract())
                player[s] = utils.stlip_space_crlf(text)

        player = Player()
        parse_player_item(player, 'no')
        parse_player_item(player, 'team')
        parse_player_item(player, 'name')
        parse_player_item(player, 'kana')
        parse_player_item(player, 'position')
        parse_player_item(player, 'bat_and_throw')
        parse_player_item(player, 'height_and_weight')
        parse_player_item(player, 'birth')
        parse_player_item(player, 'carrer')
        parse_player_item(player, 'draft')

