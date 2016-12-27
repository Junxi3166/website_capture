#!/usr/bin/env python
# _*_ coding:utf-8 _*_
# __created by junxi__

import pymongo

client = pymongo.MongoClient('localhost',27017)     # 连接 mongodb
walden = client['walden']   # mongodb 库名
sheet_tab = walden['sheet_tab']     # mongodb 表名

# path = 'C:/Users/xiaoxinsoso/Desktop/walden.txt'
# with open(path,'r') as f:
#     lines = f.readlines()
#     for index,line in enumerate(lines):     # enumerate将列表组成一个索引序列, 利用它可以同时获得索引和值
#         data = {
#             'index': index,
#             'line': line,
#             'words': len(line.split()),
#         }
#         sheet_tab.insert_one(data)          # 把数据填充进去数据库
# $lt/$lte/$gt/$gte/$ne, 依次等价于</<=/>/>=/!=, (l表示less, g表示greater, e表示equal, n表示not)
for item in sheet_tab.find({'words': {'$lt': 5}}):
    print(item)

