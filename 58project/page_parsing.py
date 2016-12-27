#!/usr/bin/env python
# _*_ coding:utf-8 _*_
# __created by junxi__

from bs4 import BeautifulSoup
import requests,time,pymongo

client = pymongo.MongoClient('localhost',27017)
ceshi = client['ceshi']
url_list = ceshi['url_list1']
# url_list = ceshi['url_list0']
item_info = ceshi['item_info1']


# spider 1  获取1页中所有商品详情页的url, 写入到mongodb中
def get_links_from(channel,pages,who_sells=1):
    # http://bj.58.com/diannao/1/pn2/   1是商家
    # http://bj.58.com/diannao/0/pn2/   0是转转
    list_view = '{}{}/pn{}'.format(channel,str(who_sells),str(pages))
    wb_data = requests.get(list_view)
    time.sleep(1)
    soup = BeautifulSoup(wb_data.text,'lxml')
    if soup.find('td','t'):
        for link in soup.select('td.t a.t'):
            item_link = link.get('href').split('?')[0]
            url_list.insert_one({'url': item_link})
            print(item_link)
    else:
        pass
        # Nothing !

# get_links_from('http://bj.58.com/shouji/',2,1)
# get_links_from('http://bj.58.com/shouji/',2,0)

# spider 2  商家详情页信息抓取
def get_item_info(url):
    wb_data = requests.get(url)
    time.sleep(1)
    soup = BeautifulSoup(wb_data.text,'lxml')
    no_longer_exist = '404' in soup.find('script',type="text/javascript").get('src').split('/')
    if no_longer_exist:     # 如果页面为404,结果为(True)
        pass
    else:
        title = soup.title.text.strip("【图】\r\n ")
        price = soup.select('span.price.c_f50')[0].text
        date = soup.select('.time')[0].text
        area = soup.select('.c_25d a') if soup.find_all('span','c_25d') else None
        if len(area) == 3:                          # 两级地址,价格里面有借钱买
            area1 = ('%s-%s') % (area[1].text,area[2].text)
        elif len(area) == 2:
            if  area[0].get('target') == '_blank':  # 一级地址，价格里有借钱买
                area1 = ('%s') % (area[1].text)
            else:                                   # 两级地址,价格里面没有借钱买
                area1 = ('%s-%s') % (area[0].text,area[1].text)
        else:
            area1 = None
        item_info.insert_one({'title': title,'price': price,'date': date,'area': area1})
        print({'title': title,'price': price,'date': date,'area': area1})


# get_item_info('http://bj.58.com/pingbandiannao/26727826953024x.shtml')    # 两级地址,价格里面没有借钱买
# get_item_info('http://bj.58.com/shouji/27968150305589x.shtml')            # 两级地址,价格里面有借钱买
# get_item_info('http://bj.58.com/shouji/27968049061581x.shtml')            # 一级地址，价格里有借钱买
# get_item_info('http://bj.58.com/shouji/27449939974828x.shtml')            # 没有地址，价格里有借钱买
# get_item_info('http://bj.58.com/shouji/24605954621114x.shtml')            # 404地址


# 查看404页面的详细信息
# url = 'http://bj.58.com/shouji/24605954621114x.shtml'
# wb_data = requests.get(url)
# soup = BeautifulSoup(wb_data.text,'lxml')
# print(soup.prettify())
# no_longer_exist = '404' in soup.find('script',type="text/javascript").get('src').split('/')
# print(no_longer_exist)


