#!/usr/bin/env python
# _*_ coding:utf-8 _*_
# __created by junxi__

from multiprocessing import Pool
from channel_extract import channel_list
from page_parsing import get_links_from


def get_all_links_from(channel):
    for num in range(1,121):
        get_links_from(channel,num)


if __name__ == '__main__':
    # 创建进程池
    pool = Pool()       # processes=4,默认自动分配资源
    pool.map(get_all_links_from,channel_list.split())       # map把集合中的数据依次一个个的放进函数中


