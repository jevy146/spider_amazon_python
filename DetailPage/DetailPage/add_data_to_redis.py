# -*- coding: utf-8 -*-

# @File    : add_data_to_redis.py
# @Date    : 2019-10-25
# @Author  : ${杨杰伟}


import redis

conn = redis.Redis(host='192.168.31.104', port=6379, )

# LINK_DETAIL = ['', '',
#                'https://www.amazon.com/dp/B074V28V5Z']
#
# import pymysql
#
# # 打开数据库连接
# connection = pymysql.connect(
#     host='192.168.31.104',
#     # host='localhost',
#     user='root',
#     password='1234',
#     db='amazon_us',  ## 同不同数据库，针对不同的表  例如："hanxin"
#     charset='utf8')  # 连接数据库
# cursor = connection.cursor()  # 创建游标
# # sql_1 = "select keyword,link_detail from amazon_us_link limit 300,10;"  # 从第一行开始截取3个，1,2,3，
# sql_1 = "select keyword,link_detail from amazon_us_link ;"  # 从第一行开始截取3个，1,2,3，
# cursor.execute(sql_1)
# link_detail = cursor.fetchall()  ## 获取所有数据 返回的是一个元组
# # print(link_detail)
# for i in link_detail:
#     print(i)

# link_detail=['https://www.amazon.de/dp/B00WJZOJNS', 'https://www.amazon.de/dp/B0002HOUL6',
#                'https://www.amazon.de/dp/B0083TWTT0']
# for num,each in link_detail:
#     print(each)
# #     # json_1=json.dumps(each)
#     conn.lpush('USA_Detail:start_urls',each)


# conn.lpush('USA_Detail:start_urls','https://www.amazon.com/dp/B07T771SPH')
#
# r=redis.Redis(host='192.168.31.104',port=6379,)  #代码显示的是没有密码
# print(r.keys())
# '''lpush USA_Detail:start_urls '''
#
