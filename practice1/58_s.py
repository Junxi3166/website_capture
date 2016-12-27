#!/usr/bin/env python
# _*_ coding:utf-8 _*_
# __created by junxi__

from bs4 import BeautifulSoup
import requests,time

# 商家
url = 'http://bj.58.com/pingbandiannao/21972416366734x.shtml'
# 手机端url
# url = 'http://m.58.com/bj/pingbandiannao/26088204291258x.shtml'
# headers = {
#    'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 9_1 like Mac OS X) AppleWebKit/601.1.46 '
#                   '(KHTML, like Gecko) Version/9.0 Mobile/13B143 Safari/601.1'
# }

wb_data = requests.get(url)
soup = BeautifulSoup(wb_data.text,'lxml')

# 从页面获取链接
def get_links_from(page_num=0):     # 0是个人转转, 1是商家
    urls = []
    list_view = 'http://bj.58.com/pbdn/{}/pn2'.format(str(page_num))
    wb_data = requests.get(list_view)
    soup = BeautifulSoup(wb_data.text,'lxml')
    for link in soup.select('td.t a.t'):
        urls.append(link.get('href').split('?')[0])
        # print(urls)
    return urls

# 获取浏览数
def get_views_from(url):
    id = url.split('/')[-1].strip('x.shtml')
    api = 'http://jst1.58.com/counter?infoid={}'.format(id)
    js = requests.get(api)
    views = js.text.split('=')[-1]
    # print(views)
    return views

# 获取信息
def get_item_info(page_num):
    urls = get_links_from(page_num)
    for url in urls:
        wb_data = requests.get(url)
        soup = BeautifulSoup(wb_data.text,'lxml')
        title = soup.title.text
        price = soup.select('#content span.price')[0].text
        date = soup.select('.time')[0].text
        area = list(soup.select('.c_25d')[0].stripped_strings) if soup.find_all('span','c_25d') else None
        # print(area)
        data = {
            'title': title,
            'price': price,
            'date': date,
            'area': area,
            'cate': '个人' if page_num == 0 else '商家',
            'views': get_views_from(url),
        }
        print(data)

get_item_info(1)
# get_links_from()
# get_views_from()

