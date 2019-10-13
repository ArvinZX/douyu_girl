# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class DouyuItem(scrapy.Item):
    #房间号
    room_rid = scrapy.Field()
    #房间名
    room_name = scrapy.Field()
    #图片链接
    room_src = scrapy.Field()
    #主播昵称
    nick_name = scrapy.Field()
    #人气
    room_hn = scrapy.Field()
    #获取时间
    utc_time = scrapy.Field()
    #数据源
    source = scrapy.Field()
