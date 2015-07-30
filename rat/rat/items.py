# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class Post_Item(scrapy.Item):
    url_link = scrapy.Field()
    rep_num = scrapy.Field()
    title = scrapy.Field()
    first_time = scrapy.Field()
    last_time = scrapy.Field()
    author = scrapy.Field()
    body = scrapy.Field()
