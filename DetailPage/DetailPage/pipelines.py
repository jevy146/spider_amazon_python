# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class DetailpagePipeline(object):
    def process_item(self, item, spider):
        return item



from scrapy.exporters import CsvItemExporter
import os
import csv
class DetailItemPipeline(object):

    def __init__(self):
        os.chdir("./detail_out")  #新建一个文件夹，用来保存爬取的详情页信息的，
        self.file = csv.writer(open('fishing_rod_case.csv', 'a', newline='', encoding='utf-8'))
        ## 设置文件名称，进行保存。。

        self.file.writerow('ASIN，ASIN_body，commodity_item，brandName，price，comments，star_level，ranking，DATE'.split('，'))

    def process_item(self, item, spider): #不写表头了，
        data = []
        for each in dict(item).values():
            if each:
                data.append(each)
            else:
                data.append('null')
        self.file.writerow(data)
        return item

    #以下为固定地点监测写法,监测爬虫关闭
    def close_spider(self,spider):
        os.chdir("../")
        print('存储CSV文件结束')
