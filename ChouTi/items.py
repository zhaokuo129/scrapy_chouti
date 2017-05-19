# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy

class ChoutiItem(scrapy.Item):
    # define the fields for your item here like:
    img_url = scrapy.Field()
    file_name = scrapy.Field()
    content = scrapy.Field()

# class XiaoHuaItem(scrapy.Item):
#     # define the fields for your item here like:
#     img_url = scrapy.Field()
#     file_name = scrapy.Field()
#     content = scrapy.Field()

