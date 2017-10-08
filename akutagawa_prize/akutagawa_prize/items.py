# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class AkutagawaPrizeItem(scrapy.Item):
    no = scrapy.Field()         # 開催数
    year = scrapy.Field()       # 受賞年
    name = scrapy.Field()       # 受賞者
    title = scrapy.Field()      # 受賞作
    magazine = scrapy.Field()   # 掲載誌
