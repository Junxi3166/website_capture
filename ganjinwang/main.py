#!/usr/bin/env python
# _*_ coding:utf-8 _*_
# __created by junxi__

from multiprocessing import Pool
from channel_capture import get_channel_url
from page_parsing import get_links_from, get_item_info, get_mongo_links

url = 'http://bj.ganji.com/wu/'


# 获取赶集二手频道下所有链接
def get_all_links_from(channel):
    for num in range(1,121):
        get_links_from(channel, num)


# 获取赶集所有二手商品详情页信息
def get_all_items_from(url):
    get_item_info(url)


# if __name__ == '__main__':
#     pool = Pool()       # 默认自动分配资源
#     pool.map(get_all_links_from, get_channel_url(url))       # map把集合中的数据依次一个个的放进函数中


if __name__ == '__main__':
    pool = Pool()       # 默认自动分配资源
    pool.map(get_all_items_from, get_mongo_links())       # map把集合中的数据依次一个个的放进函数中
