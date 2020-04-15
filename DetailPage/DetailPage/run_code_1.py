# @File  : run_code_1.py
# @Author: Jie Wei
#@time: 2019/9/6 14:55

from scrapy import cmdline
cmdline.execute("scrapy crawl USA_Detail".split(" "))#有日志的输出。
