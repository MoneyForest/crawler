# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

class Player(scrapy.Item):
    name = scrapy.Field()
    kana = scrapy.Field()
    age = scrapy.Field()
    no = scrapy.Field()
    team = scrapy.Field()
    position = scrapy.Field()
    bats = scrapy.Field()
    throws = scrapy.Field()
    pass
