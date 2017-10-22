# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class PokemonItem(scrapy.Item):
    index = scrapy.Field()
    name = scrapy.Field()
    total = scrapy.Field()
    hp = scrapy.Field()
    attack = scrapy.Field()
    defense = scrapy.Field()
    sp_attack = scrapy.Field()
    sp_defense = scrapy.Field()
    speed = scrapy.Field()