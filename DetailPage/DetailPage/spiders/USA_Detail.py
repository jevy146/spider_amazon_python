# -*- coding: utf-8 -*-
import time

import redis
import scrapy
from scrapy.selector import Selector
from DetailPage.items import DetailpageItem
import copy
import random
from scrapy_redis.spiders import RedisSpider


'''使用标椎格式框架写的分布式爬虫，设置redis_key,框架会自动从数据库中提取对列发送请求。'''


class UsaDetailSpider(RedisSpider):
    name = 'USA_Detail'
    allowed_domains = ['amazon.de']
    # start_urls = ['http://www.amazon.com/']

    redis_key = "USA_Detail:start_urls"

    def __init__(self, *args, **kwargs):
        # Dynamically define the allowed domains list.
        domain = kwargs.pop('domain', '')
        self.allowed_domains = filter(None, domain.split(','))
        super(UsaDetailSpider, self).__init__(*args, **kwargs)

    def make_requests_from_url(self, url):

        print('*************')

        return scrapy.Request(url,
                # headers = self.headers,
                dont_filter = True)



    def parse(self, response):  #不写start_urls了

        if response.status == 302:  #谷歌浏览器出现url重定向的问题，验证cookie，将url引到其他第链接了
            return

        commodity_info = DetailpageItem()
        if response.status == 200:
            selector = Selector(response)
            commodity_info["ASIN"] = response.url .split("/")[-1]  # 商品ASIN
            try:
                address = selector.xpath('//*[@id="glow-ingress-line2"]/text()').extract_first()  # 获取邮编的地址，，
                print("查看详情页的邮编。", address)  # 查看邮编地址。。。
            except:
                address="null"
            if address ==None :
                # print(response.text)
                if 'Robot Check' or 'Bot Check' in response.text:
                    '''将数据保存到redis重新爬取'''
                    print('有验证码。。。',response.url)
                    URL=response.url
                    conn = redis.Redis(host='192.168.31.104', port=6379, )
                    conn.lpush('USA_Detail:start_urls', URL)
                    print('将链接重新加入到redis数据库中', URL)
                    time.sleep(random.randint(2,5))

                    import win32api,win32con
                    win32api.MessageBox(0, "帅哥  scrapy爬虫 自动关闭", "提醒",win32con.MB_OK)
                    self.crawler.engine.close_spider(self, '有验证码，主动关闭爬虫')
                    return


            '''爬取变体'''
            try:

                asin_kinds = response.xpath('//*[@id="variation_color_name"]/ul//li/@data-defaultasin').extract()

                if len(asin_kinds) !=0:
                    asin_kinds = asin_kinds
                    # commodity_info["ASIN_body"] = asin_kinds
                else:
                    asin_kinds = response.xpath('//*[@id="variation_color_name"]//option/@value').extract()
                    # commodity_info["ASIN_body"] = asin_kinds
            except:
                asin_kinds = 'null'
            commodity_info["ASIN_body"] = asin_kinds

            try:
                img_src = selector.xpath('//*[@id="imgTagWrapperId"]//@src').extract()[0].strip()
                print('img_src_1', img_src)
            except:
                img_src = selector.xpath('//*[@id="landingImage"]/@src').extract()[0].strip()
                print('img_src_2', img_src)
                # img_src = selector.xpath('//*[@id="landingImage"]/@src').extract()[0]
                # print('img_src', img_src)
                # # str2 = img_src.split(',')[-1]
                # img_data = base64.b64decode(str2)
            commodity_info['img'] = img_src  # 保存图片完整的的链接。
            yield commodity_info


'''            tr_list_3=selector.xpath('//*[@id="productDetails_detailBullets_sections1"]//tr[6]//text()').extract()  #输出ASIN 和ASIN码
'''
