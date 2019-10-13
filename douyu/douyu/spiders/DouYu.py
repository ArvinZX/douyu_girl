# -*- coding: utf-8 -*-
import scrapy
from douyu.items import DouyuItem
import json


class DouyuSpider(scrapy.Spider):
    name = 'DouYu'
    allowed_domains = ['douyu.com']
    start_urls = ['https://m.douyu.com/api/room/list?page=1&type=yz']
    offset = 1

    def parse(self, response):
        data_list = json.loads(response.body.decode())['data']['list']
        for data in data_list:
            item = DouyuItem()
            item['room_rid'] = data['rid']
            item['room_name'] = data['roomName']
            item['room_src'] = data['roomSrc']
            item['nick_name'] = data['nickname']
            item['room_hn'] = data['hn']
            yield item
        if self.offset == 122:
            return
        self.offset += 1
        yield scrapy.Request(url='https://m.douyu.com/api/room/list?page='+ str(self.offset)+'&type=yz',callback=self.parse)
