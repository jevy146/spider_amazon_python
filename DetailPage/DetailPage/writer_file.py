# -*- coding: utf-8 -*-

# @File    : writer_file.py
# @Date    : 2019-10-26
# @Author  : ${杨杰伟}

fileOb = open('saveString.txt','w') #打开一个文件若没有就新建一个
fileOb.write('hellow file') #文件写入str
fileOb.close() #关闭文件
