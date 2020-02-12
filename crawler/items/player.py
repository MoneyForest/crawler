# -*- coding: utf-8 -*-
import scrapy


class Player(scrapy.Item):
    npb_id = scrapy.Field()
    no = scrapy.Field()
    team_ja = scrapy.Field()
    team_en = scrapy.Field()
    name = scrapy.Field()
    kana = scrapy.Field()
    position = scrapy.Field()
    bats = scrapy.Field()
    throws = scrapy.Field()
    height = scrapy.Field()
    weight = scrapy.Field()
    born = scrapy.Field()
    age = scrapy.Field()
    carrer = scrapy.Field()
    draft = scrapy.Field()
    draft_year = scrapy.Field()
    draft_no = scrapy.Field()
    blood_type = scrapy.Field()
    salary = scrapy.Field()
