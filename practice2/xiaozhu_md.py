#!/usr/bin/env python
# _*_ coding:utf-8 _*_
# __created by junxi__

from bs4 import BeautifulSoup
import requests,time,pymongo


url = 'http://bj.xiaozhu.com/fangzi/1138219165.html'
# url = 'http://bj.xiaozhu.com/fangzi/3866118430.html'
# url = 'http://bj.xiaozhu.com/search-duanzufang-p1-0/'
client = pymongo.MongoClient('localhost',27017)                        # 连接 mongodb
xiaozhu = client['xiaozhu']                                            # mongodb 库名
pig_tab = xiaozhu['pig_tab']                                           # mongodb 表名
# 从 mongodb 查询租金大于500的租房信息
for item in pig_tab.find({'day_rents': {'$gte': '500'}}):
    print(item)

# 获取单个短租房信息
def get_one_info(url):
    client = pymongo.MongoClient('localhost',27017)                    # 连接 mongodb
    xiaozhu = client['xiaozhu']                                        # mongodb 库名
    pig_tab = xiaozhu['pig_tab']                                       # mongodb 表名
    wb_data = requests.get(url)
    soup = BeautifulSoup(wb_data.text,'lxml')
    titles = soup.select('h4 > em')[0].text                            # 标题
    addrs = soup.select('span.pr5')[0].text.strip('\n ')               # 地址
    day_rents = soup.select('#pricePart > div.day_l > span')[0].text   # 日租金
    # first_images = soup.select('#curBigImage')                       # 第一张房源图片链接
    # landlord_images = soup.select('div.member_pic > a > img')        # 房东图片链接
    landlord_names = soup.select('a.lorder_name')[0].text              # 房东名字
    sex = soup.select('div.member_ico1')
    if not sex:
        landlord_sexs = "男"
    else:
        landlord_sexs = "女"
    data = {
        'titles': titles,
        'addrs': addrs,
        'day_rents': day_rents,
        'landlord_names': landlord_names,
        'landlord_sex': landlord_sexs,
    }
    pig_tab.insert_one(data)
    for item in pig_tab.find():
        print(item)


# 如何批量获取链接
def get_page_link(page_number):
    page_link = []    # <- 每个详情页的链接都存在这里，解析详情的时候就遍历这个列表然后访问就好啦~
    for each_number in range(1,page_number+1):        # 每页24个链接,这里输入的是页码
        full_url = 'http://bj.xiaozhu.com/search-duanzufang-p{}-0/'.format(each_number)
        wb_data = requests.get(full_url)
        soup = BeautifulSoup(wb_data.text,'lxml')
        for link in soup.select('a.resule_img_a'):  # 找到这个 class 样为resule_img_a 的 a 标签即可
            page_link.append(link.get('href'))
    return page_link


# 获取单个或多个页面所有租房信息, 默认获取第一页
def more_page_info(page_number=1):
    for single_url in get_page_link(page_number):
        get_one_info(single_url)



# more_page_info(3)





