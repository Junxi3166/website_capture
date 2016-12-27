#!/usr/bin/env python
# _*_ coding:utf-8 _*_
# __created by junxi__

from bs4 import BeautifulSoup
path = './1_2_homework_required/index.html'  # 这里使用了相对路径,只要你本地有这个文件就能打开

with open(path, 'r') as wb_data:    # 使用with open打开本地文件
    soup = BeautifulSoup(wb_data, 'lxml')  # 解析网页内容
    # print(soup)
    images = soup.select('body > div > div > div.col-md-9 > div > div > div > img')
    prices = soup.select('body > div > div > div.col-md-9 > div > div > div > div.caption > h4.pull-right')
    titles = soup.select('body > div > div > div.col-md-9 > div > div > div > div.caption > h4 > a')
    rate_nums = soup.select('body > div > div > div.col-md-9 > div > div > div > div.ratings > p.pull-right')
    rate_stars = soup.select('body > div > div > div.col-md-9 > div > div > div > div.ratings > p:nth-of-type(2)')

for image,price,title,rate_num,rate_star in zip(images,prices,titles,rate_nums,rate_stars):
    data = {
        'title': title.get_text(),  # 使用get_text()方法取出文本
        'image': image.get('src'),  # 使用get 方法取出带有src的图片链接
        'price': price.get_text(),
        'rate_num': rate_num.get_text(),
        'rate_star': len(rate_star.find_all("span", class_='glyphicon glyphicon-star')),
        # 观察发现,每一个星星会有一次<span class="glyphicon glyphicon-star"></span>,
        # 所以我们统计有多少次,就知道有多少个星星了;
        # 使用find_all 统计有几处是★的样式,第一个参数定位标签名,第二个参数定位css 样式,具体可以参考BeautifulSoup
        # 文档示例http://www.crummy.com/software/BeautifulSoup/bs4/doc.zh/#find-all;
        # 由于find_all()返回的结果是列表,我们再使用len()方法去计算列表中的元素个数,也就是星星的数量
    }
    print(data)