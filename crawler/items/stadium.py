# -*- coding: utf-8 -*-
import scrapy

class Stadium(scrapy.Item):
    full_name = scrapy.Field()
    location = scrapy.Field()
    opened_at = scrapy.Field()
    capacity = scrapy.Field()
    field_size = scrapy.Field()
    first_matched_at = scrapy.Field()
    matches = scrapy.Field()
    homerun = scrapy.Field()
    home_team = scrapy.Field()
