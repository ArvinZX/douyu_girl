# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from datetime import datetime
import scrapy
from scrapy.pipelines.images import ImagesPipeline

from douyu.settings import IMAGES_STORE

import os

class DouyuPipeline(object):
    def process_item(self, item, spider):
        item['source'] = spider.name
        item['utc_time'] = str(datetime.utcnow())
        return item

class DouyuImagesPipeline(ImagesPipeline):
    #scrapy封装的   通过图片的链接 自动下载 图片
    def get_media_requests(self,item,info):
        """获取链接"""
        room_src = item['room_src']
        """发送图片下载请求，结果会保存在 settings 中的 IMAGES_STORE 的制定路径中"""
        yield scrapy.Request(url=room_src)

    """这个也是固定的写法，其中results是上面下载的 图片的 结果"""
    def item_completed(self,results,item,info):
        # print(results)
        # print("*"*60)
        image_path = [v['path'] for k,v in results if k]

        #旧的保存地址
        old_path = IMAGES_STORE + image_path[0]

        #新的保存地址
        new_path = IMAGES_STORE + item['nick_name'] + '.jpg'

        try:
            os.rename(old_path,new_path)
        except:
            print("[info]:图片已被修改")

        return item



