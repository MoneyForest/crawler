# -*- coding: utf-8 -*-
import scrapy
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
            URL = response.urljoin(TEAM_URL.extract())
            yield scrapy.Request(URL, self.crawl_team_url)

            if utils.is_development() and n > 1: return

    def crawl_team_url(self, response):
        PLAYERS_URLS = response.xpath("//*[@class='rosterRegister']/a/@href")

        for n, PLAYER_URL in enumerate(PLAYERS_URLS):
            URL = response.urljoin(PLAYER_URL.extract())
            yield scrapy.Request(URL, self.parse_player_item)

            if utils.is_development() and n > 1: return

    def parse_player_item(self, response):
        NO_XPATH = "//*[@id='pc_v_no']/text()"
        TEAM_XPATH = "//*[@id='pc_v_team']/text()"
        NAME_XPATH = "//*[@id='pc_v_name']/text()"
        KANA_XPATH = "//*[@id='pc_v_kana']/text()"
        POSITION_XPATH = "//*[@id='pc_bio']/table/tbody/tr[1]/td/text()"
        BAT_AND_THROW_XPATH = "//*[@id='pc_bio']/table/tbody/tr[2]/td/text()"
        HEIGHT_AND_WEIGHT_XPATH = "//*[@id='pc_bio']/table/tbody/tr[3]/td/text()"
        BIRTH_XPATHv = "//*[@id='pc_bio']/table/tbody/tr[4]/td/text()"
        CARRER_XPATH = "//*[@id='pc_bio']/table/tbody/tr[5]/td/text()"
        DRAFT_XPATH = "//*[@id='pc_bio']/table/tbody/tr[6]/td/text()"

        player = Player()
        player['no'] = extract_first(NO_XPATH, response)
        player['team'] = extract_first(NO_XPATH, response)
        player['name'] = extract_first(NO_XPATH, response)
        player['kana'] = extract_first(NO_XPATH, response)
        player['position'] = extract_first(NO_XPATH, response)
        player['bat_and_throw'] = extract_first(NO_XPATH, response)
        player['height_and_weight'] = extract_first(NO_XPATH, response)
        player['birth'] = extract_first(NO_XPATH, response)
        player['carrer'] = extract_first(NO_XPATH, response)
        player['draft'] = extract_first(NO_XPATH, response)

        print(player.no)

        def extract_first(xpath, response):
            return response.xpath(xpath).extract()

        pass
