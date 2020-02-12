# -*- coding: utf-8 -*-
import scrapy
import json
from .. import utils
from crawler.items.stadium import Stadium

class StadiumSpider(scrapy.Spider):
    name = 'stadium'

    def __init__(self):
        self.allowed_domains = ['npb.jp']
        self.start_urls = ['http://npb.jp/stadium/franchise.html']

    def parse(self, response):
        yield scrapy.Request(self.start_urls[0], self.crawl_npb_url)

    def crawl_npb_url(self, response):
        STADIUM_URLS = response.xpath("//*[@id='st_list']/a/@href")

        for n, STADIUM_URL in enumerate(STADIUM_URLS):
            if utils.is_development() and n > 0: return

            URL = response.urljoin(STADIUM_URL.extract())
            yield scrapy.Request(URL, self.crawl_stadium_url)

    def crawl_stadium_url(self, response):
        def parse_stadium_item(stadium):
            with open('crawler/xpath/stadium.json', 'r') as f:
                stadium_json = json.load(f)
                for key in stadium_json.keys():
                    val = ''.join(response.xpath(stadium_json[key]).extract())
                    stadium[key] = utils.stlip_space_crlf(val)

        stadium = Stadium()
        parse_stadium_item(stadium)
