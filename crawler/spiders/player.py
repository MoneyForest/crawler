# -*- coding: utf-8 -*-
import scrapy
import json
from .. import utils
from .. import player_utils
from crawler.items.player import Player

class PlayerSpider(scrapy.Spider):
    name = 'player'

    def __init__(self):
        self.allowed_domains = ['npb.jp', 'www.sanspo.com']
        self.start_urls = ['http://npb.jp/bis/teams/']
        self.player = Player()

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

        player_utils.parse_player_params(self.player, response)
        player_utils.reshape_player_params(self.player)

        SANSPO_URL = player_utils.build_sanspo_url(
            self.player['team_en'], self.player['no'])

        yield scrapy.Request(SANSPO_URL, self.crawl_sanspo_player_url)

    def crawl_sanspo_player_url(self, response):
        pass
