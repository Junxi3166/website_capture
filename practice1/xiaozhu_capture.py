#!/usr/bin/env python
# _*_ coding:utf-8 _*_
# __created by junxi__

from bs4 import BeautifulSoup
import requests
import time

url = 'http://bj.xiaozhu.com/fangzi/1508951935.html'

def get_houseinfo(url):
    wb_data = requests.get(url)
    soup = BeautifulSoup(wb_data.text,'lxml')
    titles = soup.select('h4 > em')                                  # 标题
    addrs = soup.select('span.pr5')                                  # 地址
    day_rents = soup.select('#pricePart > div.day_l > span')         # 日租金
    first_images = soup.select('#curBigImage')                       # 第一张房源图片链接
    landlord_images = soup.select('div.member_pic > a > img')        # 房东图片链接
    landlord_names = soup.select('a.lorder_name')                    # 房东名字
    sex = soup.select('div.member_ico1')                             # 房东性别
    if not sex:
        landlord_sexs = "男"
    else:
        landlord_sexs = "女"


    for title,addr,day_rent,first_image,landlord_image,landlord_sex,landlord_name in zip(titles,addrs,day_rents,
        first_images,landlord_images,landlord_sexs,landlord_names):
        data = {
            'title': title.get_text(),
            'addr': addr.get_text().strip(),
            'day_rent': day_rent.get_text(),
            'first_image': first_image.get('src'),
            'landlord_image': landlord_image.get('src'),
            'landlord_sex': landlord_sex,
            'landlord_name': landlord_name.get_text(),
        }
        print(data)



# 如何批量获取链接

page_link = []  # <- 每个详情页的链接都存在这里，解析详情的时候就遍历这个列表然后访问就好啦~

def get_page_link(page_number):
    for each_number in range(1,page_number+1):        # 每页24个链接,这里输入的是页码
        full_url = 'http://bj.xiaozhu.com/search-duanzufang-p{}-0/'.format(each_number)
        wb_data = requests.get(full_url)
        soup = BeautifulSoup(wb_data.text,'lxml')
        for link in soup.select('a.resule_img_a'):  # 找到这个 class 样为resule_img_a 的 a 标签即可
            page_link.append(link.get('href'))
            for single_url in page_link:
                get_houseinfo(single_url)
                time.sleep(1.5)


get_page_link(1)














