#!/usr/bin/env python
# _*_ coding:utf-8 _*_
# __created by junxi__

from bs4 import BeautifulSoup
import requests,time

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                'Chrome/52.0.2743.116 Safari/537.36'
}
# url = 'http://bj.58.com/pingbandiannao/21972416366734x.shtml'
url = 'http://bj.58.com/pingbandiannao/27569124243383x.shtml'
wb_data = requests.get(url)
soup = BeautifulSoup(wb_data.text, 'lxml')



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



# 获取浏览量
def get_views_from():
    id = url.split('/')[-1].strip('x.shtml')
    api = 'http://jst1.58.com/counter?infoid={}'.format(id)
    js = requests.get(api)
    views = js.text.split('=')[-1]
    # print(views)
    return views


def get_item_info(page_num):

    urls = get_links_from(page_num)
    for url in urls:
        wb_data = requests.get(url)
        soup = BeautifulSoup(wb_data.text, 'lxml')

        colour = soup.select('div.su_con > span')[1].get_text().strip()                                    # 成色
        date = soup.select('li.time')[0].get_text()                                                        # 发布日期
        try:
            if soup.select('div.breadCrumb.f12 > span > a')[2].get_text():
                class_info = soup.select('div.breadCrumb.f12 > span > a')[2].get_text()
        except IndexError:
            class_info = None
            # print('没有三级分类')

        area1 = soup.select('span.c_25d > a')[0].get_text() if soup.find_all('span','c_25d') else None      # 区域1: 大区
        area2 = soup.select('span.c_25d > a')[1].get_text() if soup.find_all('span','c_25d') else None      # 区域2: 村镇
        #area = list(soup.select('.c_25d')[0].stripped_strings) if soup.find_all('span','c_25d') else None
        titles = soup.select('div.col_sub.mainTitle > h1')[0].get_text()                                    # 标题
        prices = soup.select('div.su_con > span')[0].get_text()                                             # 价格
        imagea = soup.select('div.descriptionImg > a > img')
        images = [image.get('src') for image in imagea]                                                     # 图片链接
        # print(('%s-%s') % (area1,area2))
        data = {
            'cates': '个人' if page_num == 0 else '商家',
            'class_info': class_info,
            'date': date,
            'titles': titles,
            'colour': colour,
            'prices': prices,
            'area': ('%s-%s' % (area1, area2)),
            # 'area': area,
            'images': images,
        }
        print(data)

# get_views_from(1)

# get_links_from(1)

get_item_info(1)