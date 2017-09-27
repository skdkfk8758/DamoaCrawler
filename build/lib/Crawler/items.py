# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class DamoaItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()

    source = scrapy.Field()
    attribute = scrapy.Field()
    title = scrapy.Field()
    link = scrapy.Field()
    date = scrapy.Field()
    hits = scrapy.Field()
    recommened = scrapy.Field()
    last_update = scrapy.Field()
    pop = scrapy.Field()
    text = scrapy.Field()

    pass
