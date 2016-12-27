#!/usr/bin/env python
# _*_ coding:utf-8 _*_
# __created by junxi__

from bs4 import BeautifulSoup
import requests,time,urllib.request


# 'http://weheartit.com/inspirations/beach?page=8' full url
url = 'http://weheartit.com/inspirations/taylorswift?scrolling=true&page='

download_links = []
folder_path = 'C:/Users/xiaoxinsoso/Pictures/python测试图片/'

# 下载单个url页面中图片
def get_image(url):
    wb_data = requests.get(url)
    soup = BeautifulSoup(wb_data.text,'lxml')
    images = soup.select('div.entry-preview > a > img')
    for image in images:
        download_links.append(image.get('src'))
    for item in download_links:
        # 下载图片
        urllib.request.urlretrieve(item,folder_path + item[-24:].replace('/','-'))
        print('Done')


# 批量下载多个url页面中图片
def get_more_pages(num):
    for one in range(1,num + 1):
        get_image(url+str(one))
        time.sleep(1)


get_more_pages(20)
