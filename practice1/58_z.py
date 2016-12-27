#!/usr/bin/env python
# _*_ coding:utf-8 _*_
# __created by junxi__


from bs4 import BeautifulSoup
import requests,time

# 转转
url = 'http://zhuanzhuan.58.com/detail/782628495217426436z.shtml'

wb_data = requests.get(url)
soup = BeautifulSoup(wb_data.text,'lxml')

title = soup.title.text
price = soup.select('div.content span.price_now > i')[0].text
seller = soup.select('p.personal_name')[0].text
area = soup.select('div.palce_li > span > i')[0].text
# print(title)
data = {
    'title': title.strip('\r\n '),
    'price': price,
    'seller': seller,
    'area': area,
}
print(data)
