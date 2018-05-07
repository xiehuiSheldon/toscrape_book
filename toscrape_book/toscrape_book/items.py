# -*- coding: utf-8 -*-

import scrapy

class BookItem(scrapy.Item):
    name = scrapy.Field()               # 书名
    price = scrapy.Field()              # 价格
    review_rating = scrapy.Field()      # 评价等级，1~5星
    review_num = scrapy.Field()         # 评价数目
    upc = scrapy.Field()                # 产品编号
    stock = scrapy.Field()              # 库存量
