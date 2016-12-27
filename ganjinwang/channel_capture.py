#!/usr/bin/env python
# _*_ coding:utf-8 _*_
# __created by junxi__

from bs4 import BeautifulSoup
import requests

url = 'http://bj.ganji.com/wu/'
# http://bj.ganji.com/shouji/o1       o1是个人第一页, 因为手机和平板等频道个人都改为转转了, 其他频道没改不方便抓取, 所以抓取商家页面
# http://bj.ganji.com/shouji/a2o1     a2o1是商家是第一页
prefix = 'http://bj.ganji.com'


# 导航类目链接
def get_channel_url(url):
    wb_data = requests.get(url)
    soup = BeautifulSoup(wb_data.text,'lxml')
    titles = soup.select('dl.fenlei > dt > a')
    links = soup.select('dl.fenlei > dt > a')
    channel_list = []
    for link in links:
        page_url = prefix + link.get('href')
        channel_list.append(page_url)
    return channel_list


# for i in get_channel_url(url):
#     print(i)