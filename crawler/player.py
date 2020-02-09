# -*- coding: utf-8 -*-
import scrapy

class Player(scrapy.Item):
    npb_id = scrapy.Field()
    no = scrapy.Field()
    team = scrapy.Field()
    name = scrapy.Field()
    kana = scrapy.Field()
    position = scrapy.Field()
    bat = scrapy.Field()
    throw = scrapy.Field()
    height = scrapy.Field()
    weight = scrapy.Field()
    birth = scrapy.Field()
    carrer = scrapy.Field()
    draft = scrapy.Field()
    draft_year = scrapy.Field()
    draft_no = scrapy.Field()
