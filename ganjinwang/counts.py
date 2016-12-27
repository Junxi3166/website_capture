#!/usr/bin/env python
# _*_ coding:utf-8 _*_
# __created by junxi__

import time
from page_parsing import url_list, item_info

# 统计mongodb中url个数
# while True:
#     print(url_list.find().count())
#     time.sleep(5)

# 统计mongodb中数据行数
while True:
    print(item_info.find().count())
    time.sleep(5)
