# -*- coding: utf-8 -*-

# Scrapy settings for DetailPage project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://doc.scrapy.org/en/latest/topics/settings.html
#     https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://doc.scrapy.org/en/latest/topics/spider-middleware.html
import random

BOT_NAME = 'DetailPage'

SPIDER_MODULES = ['DetailPage.spiders']
NEWSPIDER_MODULE = 'DetailPage.spiders'



'''设置scrapy_redis自动停的程序'''
EXTENSIONS = {
    # 'scrapy.extensions.telnet.TelnetConsole': None,
    'DetailPage.extensions.RedisSpiderSmartIdleClosedExensions': 500,
}
MYEXT_ENABLED = True      # 开启扩展
IDLE_NUMBER = 300           # 配置空闲持续时间单位为 360个 ，一个时间单位为5s






# import pymysql
# # 打开数据库连接
# connection = pymysql.connect(
#     host = '192.168.31.104',
#     #host='localhost',
#     user='root',
#     password='1234',
#     db='amazon_us',  ## 同不同数据库，针对不同的表  例如："hanxin"
#     charset='utf8')  # 连接数据库
# cursor = connection.cursor()  # 创建游标
# sql_1 = "select keyword,link_detail from amazon_us_link limit 70,5;"  #从第一行开始截取3个，1,2,3，
# cursor.execute(sql_1)
# LINK_DETAIL = cursor.fetchall()  ## 获取所有数据 返回的是一个元组
# print(LINK_DETAIL)


'''使用redis数据库，使用scrapy_redis'''

# 使用了scrapy-redis里的去重组件，不使用scrapy默认的去重
DUPEFILTER_CLASS = "scrapy_redis.dupefilter.RFPDupeFilter"
# 使用了scrapy-redis里的调度器组件，不实用scrapy默认的调度器
SCHEDULER = "scrapy_redis.scheduler.Scheduler"
# 使用队列形式
SCHEDULER_QUEUE_CLASS = "scrapy_redis.queue.SpiderQueue"
# 允许暂停，redis请求记录不丢失
SCHEDULER_PERSIST = True


REDIS_HOST = "192.168.31.104"
REDIS_PORT = 6379


'''对redis数据库中添加urls'''
'''将url和key_word 在settings文件启动的时候保存到redis数据库中'''
'''感觉数多次一句，不过是因为redis数据库可以去重，随机取数据，可以实现分布式，
前面的保存到MySQL数据库的步骤，可以改为保存到redis数据了'''
# import json
# import redis
# conn=redis.Redis(host='192.168.31.104',port=6379)
# for each in LINK_DETAIL:
#     print(each)
#     json_1=json.dumps(each)
#     conn.lpush('ASINSpider:start_urls',json_1)





# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'DetailPage (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False


DEFAULT_REQUEST_HEADERS = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'en',
    'cache-control': 'max-age=0',
    # 'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.75 Safari/537.36',

}

#对失败的HTTP进行重新请求（重试）会减慢爬取速度，因此可以禁止重试。在配置文件中编写：

RETRY_ENABLED = False
#生成随机数，浮点类型
#a = random.uniform(2, 4)
#控制随机数的精度round(数值，精度)
#print(round(a, 2))
#DOWNLOAD_DELAY = round(a, 2)  # 延缓爬取的时间。。有两位小数
RANDOMIZE_DOWNLOAD_DELAY = True
'''
https://www.cnblogs.com/xueli/p/7250537.html  对setting的解释
'''

# from scrapy.contrib.throttle import AutoThrottle
AUTOTHROTTLE_ENABLED = True
#起始的延迟
AUTOTHROTTLE_START_DELAY = 3
# #最小延迟
DOWNLOAD_DELAY = random.randint(3,5)
# #最大延迟
AUTOTHROTTLE_MAX_DELAY = 15
#每秒并发请求数的平均值，不能高于 CONCURRENT_REQUESTS_PER_DOMAIN或CONCURRENT_REQUESTS_PER_IP，调高了则吞吐量增大强奸目标站点，调低了则对目标站点更加”礼貌“
#每个特定的时间点，scrapy并发请求的数目都可能高于或低于该值，这是爬虫视图达到的建议值而不是硬限制
AUTOTHROTTLE_TARGET_CONCURRENCY = 5 # 平均每秒并发数 原先值为16
#调试
AUTOTHROTTLE_DEBUG = True
CONCURRENT_REQUESTS_PER_DOMAIN = 5 #单个域名的请求数，，原先值为16
CONCURRENT_REQUESTS_PER_IP =5 # 单个IP的并发请求数，原先值为16

# Configure maximum concurrent requests performed by Scrapy (default: 16)
# 配置Scrapy执行的最大并发请求（默认值：16）
CONCURRENT_REQUESTS = 1#类似于线程数量。。默认是16，一下子提交16个强求。。




# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://doc.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
#DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
#DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
#}

# Enable or disable spider middlewares
# See https://doc.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'DetailPage.middlewares.DetailpageSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
'''中间键'''
DOWNLOADER_MIDDLEWARES = {
# 该中间件将会收集失败的页面，并在爬虫完成后重新调度。（失败情况可能由于临时的问题，例如连接超时或者HTTP 500错误导致失败的页面）
   'scrapy.downloadermiddlewares.retry.RetryMiddleware': 80,

   'DetailPage.middlewares.DetailpageDownloaderMiddleware': 543,

# 该中间件提供了对request设置HTTP代理的支持。您可以通过在 Request 对象中设置 proxy 元数据来开启代理。
    'scrapy.downloadermiddlewares.httpproxy.HttpProxyMiddleware': 100,

}

# Enable or disable extensions
# See https://doc.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://doc.scrapy.org/en/latest/topics/item-pipeline.html

'''保存Items,将数据保存到redis中'''
ITEM_PIPELINES = {
   # 'DetailPage.pipelines.DetailpagePipeline': 300,
   # 'DetailPage.pipelines.DetailItemPipeline': 300, #保存为csv文件，
    'scrapy_redis.pipelines.RedisPipeline' : 400,
}



# Enable and configure the AutoThrottle extension (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
