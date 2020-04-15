# -*- coding: utf-8 -*-
# @Time    : 2020/1/16 9:16
# @Author  : 结尾！！
# @FileName: 从redis中取出数据保存到Excel.py
# @Software: PyCharm

import json
import redis
import pandas as pd
from redis import StrictRedis
#方法一
redis_conn=StrictRedis(host='192.168.31.104',port=6379,db=0,decode_responses=True)  #decode_responses=True解决出数据带b的问题
redis_len=redis_conn.llen('comments_info:items')
print(redis_len)
print(redis_conn.exists('USA_Detail:items'))
data=[]
for each in redis_conn.lrange('USA_Detail:items',0,redis_len):
    print(each)
    each=json.loads(each)  # 将json对象转换为Python对象
    data.append(each)
df1=pd.DataFrame(data)
print(df1.shape)
df1.to_excel('./detail_page/fanny_pack.xlsx',header=True,index=None,encoding='utf-8')


#方法二 以删除的形式
# redis_conn=redis.Redis(host='192.168.31.104',port=6379,db=0,)  #decode_responses=True解决出数据带b的问题
# redis_len=redis_conn.llen('comments_info:items')
#
# data_info=[]
# for each in range(redis_len):  #单纯的循环取数据
#     source, data = redis_conn.blpop("comments_info:items")
#     print('source',source)
#     print('data++1',type(data), data)  #<class 'bytes'>   b'{"url": "https://www.
#     data = json.loads(data)# 将已编码的 JSON 字符串解码为 Python 对象
#     print('data--2', type(data),data)  #<class 'dict'>  {'url': 'https://www.amazon
#     data_info.append(data)
# df1=pd.DataFrame(data_info)
# print(df1.shape)
# df1.to_excel('./detail_page/英国评论0116_1.xlsx',header=True,index=None,encoding='utf-8')