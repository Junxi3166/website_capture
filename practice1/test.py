#!/usr/bin/env python
# _*_ coding:utf-8 _*_
# __created by junxi__

# 内容替换
data = 'http://data.whicdn.com/images/264748015/superthumb.jpg'
# print(data[-24:].replace('/','-'))

# 以 / 分割
a = data.split('/')[-2] + data.split('/')[-1]
# print(a)

# 列表去重, 并按照原来排序
ids = [1,4,3,3,4,2,3,4,5,6,1]
news_ids = list(set(ids))
news_ids.sort(key=ids.index)
# print(news_ids)

for i in range(1,3):
    print(i)

ll = len(['<a href="http://bj.58.com/">北京58同城</a>', '<a href="http://bj.58.com/sale.shtml">北京二手市场</a>'])
# print(ll)

a = '46003,2013/11/02 15:21:56,/mmsns/M6CLCDD0GAysp3sbCxsCeKXxhDI4xHkt0sf8ick'
b = a.split(',',len(a))
# print(b)

list = ['海淀', '-', '学院路']
l1 = list.remove('-')
# print(l1)

