#!/usr/bin/env python
# -*- coding:utf-8 -*-

import redis
import pymongo
import json
import time
def process_item():
    # 创建redis数据库连接
    rediscli = redis.Redis(host = "127.0.0.1", port = 6379, db = "0")

    # 创建MongoDB数据库连接
    mongocli = pymongo.MongoClient(host = "127.0.0.1", port = 27017)

    # 创建mongodb数据库名称
    dbname = mongocli["amazon_us"]
    # 创建mongodb数据库youyuan的表名称
    sheetname = dbname["Asin_Body"]
    offset = 0

    while True:
        # redis 数据表名 和 数据
        source, data = rediscli.blpop("USA_Detail:items")
        offset += 1
        # 将json对象转换为Python对象
        data = json.loads(data)
        print(data)
        # 将数据插入到sheetname表里
        sheetname.insert(data)
        print (offset)
        time.sleep(0)

if __name__ == "__main__":
    process_item()
