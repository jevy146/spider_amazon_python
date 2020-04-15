# -*- coding: utf-8 -*-
# @Time    : 2020/1/8 11:52
# @Author  : 结尾！！
# @FileName: 取出对应ASIN的信息并保存到excel中.py
# @Software: PyCharm

import pymongo
import xlwings as xw
import redis

conn = redis.Redis(host='192.168.31.104', port=6379, )

app = xw.App(visible=True, add_book=False)
wb = xw.Book('./ONJ58对手ASIN.xlsx')  # 更改相应的Excel
sht=wb.sheets['弱ASIN']
print(sht.range('A1').value)
ASIN_LIST=sht.range('A1').expand('down').value
print(ASIN_LIST)
print(len(ASIN_LIST))

#从MongoDB中取出对应的ASIN信息，写入excel中
#1.建立连接
connection=pymongo.MongoClient(host='127.0.0.1',port=27017)
#2.连接数据库
db=connection.amazon_us
#3.连接表
db_table=db.Asin_Body

# info=db_table.find_one({"ASIN":'B00GO2YKEU'},{'_id':0})
# print(info['ASIN_body'])

for index,asin in enumerate(ASIN_LIST):
    info=db_table.find_one({"ASIN":asin},{'_id':0})
    if info:
        # print(asin,info['ASIN_body'])
        if len(info['ASIN_body'])==0:
            sht.range(f'C{index+1}').value='null'
        sht.range(f'C{index+1}').value=info['ASIN_body']
        try:
            print('排名',asin,info['ranking'])
            if type(info['ranking'])==list:
                if len(info['ranking'])>2:
                    sht.range(f'B{index+1}').value=info['ranking'][1]
                else:
                    sht.range(f'B{index+1}').value=info['ranking'][0]
            else:
                sht.range(f'B{index + 1}').value = info['ranking']
        except:
            pass
    else:
        sht.range(f'C{index+1}').value='没有查找到'

        each='https://www.amazon.com/dp/'+asin
        print('没有查找到', asin)
        conn.lpush('USA_Detail:start_urls',each)
