# -*- coding: utf-8 -*-
import pymysql
from twisted.enterprise import adbapi


class BookPipeline(object):
    review_rating_map = {
        'One': 1,
        'Two': 2,
        'Three': 3,
        'Four': 4,
        'Five': 5,
    }

    def process_item(self, item, spider):
        rating = item.get('review_rating')
        if rating:
            item['review_rating'] = self.review_rating_map[rating]
        return item


# 普通mysql数据库的连接方法
class MySQLPipeline:

    def open_spider(self, spider):
        # 这里的和配置文件的区别是，配置文件的是真正的，这里的是默认的
        db = spider.settings.get('MYSQL_DB_NAME', 'scrapy_default')
        host = spider.settings.get('MYSQL_HOST', 'localhost')
        port = spider.settings.get('MYSQL_PORT', 3306)
        user = spider.settings.get('MYSQL_USER', 'root')
        passwd = spider.settings.get('MYSQL_PASSWORD', 'root')
        self.db_conn = pymysql.connect(host=host, port=port, db=db, user=user, passwd=passwd, charset='utf8')
        self.db_cur = self.db_conn.cursor()

    def close_spider(self, spider):
        self.db_conn.commit()
        self.db_conn.close()

    def process_item(self, item, spider):
        self.insert_db(item)
        return item

    def insert_db(self, item):
        values = (
            item['upc'],
            item['name'],
            item['price'],
            item['review_rating'],
            item['review_num'],
            item['stock'],
        )

        sql = 'insert into books values (%s,%s,%s,%s,%s,%s)'
        self.db_cur.execute(sql, values)


# Twisted中adbapi连接池访问MySQL数据库
class MySQLAsyncPipeline:

    def open_spider(self, spider):
        # 这里的和配置文件的区别是，配置文件的是真正的，这里的是默认的
        db = spider.settings.get('MYSQL_DB_NAME', 'scrapy_default')
        host = spider.settings.get('MYSQL_HOST', 'localhost')
        port = spider.settings.get('MYSQL_PORT', 3306)
        user = spider.settings.get('MYSQL_USER', 'root')
        passwd = spider.settings.get('MYSQL_PASSWORD', 'root')

        self.dbpool = adbapi.ConnectionPool('pymysql', host=host, db=db, port=port,
                                            user=user, passwd=passwd, charset='utf8')

    def close_spider(self, spider):
        self.dbpool.close()


    # process_item与insert_db分离是因为process_item可以执行增删改查，在方法里面调用方法，可以有效解耦
    def process_item(self, item, spider):
        self.dbpool.runInteraction(self.insert_db, item)
        return item

    # tx为一个Transaction对象，其接口与Cursor对象类似
    def insert_db(self, tx, item):
        values = (
            item['upc'],
            item['name'],
            item['price'],
            item['review_rating'],
            item['review_num'],
            item['stock'],
        )

        sql = 'insert into books values (%s,%s,%s,%s,%s,%s)'
        tx.execute(sql, values)