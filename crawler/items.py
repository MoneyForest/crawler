# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

class Player(scrapy.Item):
    no = scrapy.Field()
    team = scrapy.Field()
    name = scrapy.Field()
    kana = scrapy.Field()
    position = scrapy.Field()
    bat_and_throw = scrapy.Field()
    height_and_weight = scrapy.Field()
    birth = scrapy.Field()
    carrer = scrapy.Field()
    draft = scrapy.Field()
