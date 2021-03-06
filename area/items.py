# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy import Item,Field

class AreaItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()

    code = Field()
    area_name = Field()
    level = Field()
    code_highlevel = Field()
