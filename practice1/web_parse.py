#!/usr/bin/env python
# _*_ coding:utf-8 _*_
# __created by junxi__

from bs4 import BeautifulSoup
# 打开要筛选的html文件
with open('D:/program/python_practice/practice1/new_index.html','r') as wb_data:
    Soup = BeautifulSoup(wb_data, 'lxml')
    images = Soup.select('body > div.main-content > ul > li > img')
    titles = Soup.select('body > div.main-content > ul > li > div.article-info > h3 > a')
    descs  = Soup.select('body > div.main-content > ul > li > div.article-info > p.description')
    rates  = Soup.select('body > div.main-content > ul > li > div.rate > span')
    cates  = Soup.select('body > div.main-content > ul > li > div.article-info > p.meta-info')
    # print(images,titles,descs,rates,cates,sep='\n----------------\n')

info = []
# 把标签中的文件筛选，通过字典的方式展示出来
for title,image,desc,rate,cate in zip(titles,images,descs,rates,cates):
    data = {
        'title': title.get_text(),
        'rate' : rate.get_text(),
        'desc' : desc.get_text(),
        'cate' : list(cate.stripped_strings),   # cate.stripped_strings 获得一个副级标签下的所有子标签的文本信息
        'image': image.get('src'),
    }
    info.append(data)


for i in info:
    if float(i['rate']) > 3:    # 如果评分大于3的内容打印出来
        print(i['title'],i['cate'])











'''
body > div.main-content > ul > li:nth-child(1) > img
body > div.main-content > ul > li:nth-child(1) > div.article-info > h3 > a
body > div.main-content > ul > li:nth-child(1) > div.article-info > p.meta-info > span:nth-child(2)
body > div.main-content > ul > li:nth-child(1) > div.rate > span
body > div.main-content > ul > li:nth-child(1) > div.article-info > p.description
'''

