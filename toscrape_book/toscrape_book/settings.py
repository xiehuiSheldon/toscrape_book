# -*- coding: utf-8 -*-

BOT_NAME = 'toscrape_book'

SPIDER_MODULES = ['toscrape_book.spiders']
NEWSPIDER_MODULE = 'toscrape_book.spiders'

ROBOTSTXT_OBEY = True


# 写入excel
FEED_URI = 'export_data/%(name)s/%(time)s.xls'
FEED_FORMAT = 'excel'
FEED_EXPORT_ENCODING = 'utf-8'
FEED_EXPORT_FIELDS = ['upc', 'name', 'price', 'stock', 'review_rating', 'review_num']
FEED_EXPORTERS = {'excel': 'toscrape_book.my_exporters.ExcelItemExporter'}

'''

MYSQL_DB_NAME = 'scrapy_db'
MYSQL_HOST = 'localhost'
MYSQL_USER = 'root'
MYSQL_PASSWORD = ''


# 把MySQLPipeline和MySQLAsyncPipeline用上也可以！会插入两次，所有主键不能是upc
ITEM_PIPELINES = {
    'toscrape_book.pipelines.BookPipeline': 300,
    'toscrape_book.pipelines.MySQLPipeline': 401,
    'toscrape_book.pipelines.MySQLAsyncPipeline': 501,
}

'''