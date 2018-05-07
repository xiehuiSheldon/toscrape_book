# toscrape_book
toscrape_book所有资料

## 任务：
爬取 http://books.toscrape.com/ 网站中商品：书本的详细资料。

## 步骤：
1. 明确爬取的信息，其中每本书信息包括：
* 书名
* 价格
* 评价等级
* 产品编码
* 库存量
* 评价数量
2. 页面分析：  
主要使用Selector，找到需要信息的位置，熟练xpath和css。
3. 编码实现：
* 继承Spider创建BookSpider类
* 为Spider取名
* 指定起始爬取点
* 实现书籍列表页面的解析函数
* 实现书籍页面的解析函数
注意：用到LinkExtractor和熟练callback使用。
4. 存储或导出数据，有以下方法：
* 导出为json,csv文件
* 导出为excel文件
* 存储到MongoDB
* 使用pymysql存储到MySQL数据库
* 使用异步方式多线程访问数据库的模块adbapi，存储到MySQL数据库
