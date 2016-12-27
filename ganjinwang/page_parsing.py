#!/usr/bin/env python
# _*_ coding:utf-8 _*_
# __created by junxi__

from bs4 import BeautifulSoup
import requests,time,pymongo

client = pymongo.MongoClient('localhost',27017)
ganji = client['ganji']
url_list = ganji['url_list_ganji']
item_info = ganji['item_info_ganji']
prefix = 'http://bj.ganji.com/shouji/'

# spider 1  获取1页中所有商品详情页的url, 写入到mongodb中
def get_links_from(channel,pages,who_sells='a2'):
    # http://bj.ganji.com/shouji/a1o1       a1是个人, 因为手机和平板频道个人都改为转转了, 其他频道没改不方便抓取, 所以抓取商家页面
    # http://bj.ganji.com/shouji/a2o1       a2是商家, 默认a2是第一页, 第二页是a2o1, 第三页是a2o2
    list_view = '{}{}o{}'.format(channel,str(who_sells),str(pages))
    wb_data = requests.get(list_view)
    time.sleep(1)
    soup = BeautifulSoup(wb_data.text,'lxml')
    if soup.find('a','ft-tit'):
        for link in soup.select('a.ft-tit'):
            item_link = link.get('href')
            title = link.get_text()
            url_list.insert_one({'title': title, 'url': item_link})
            print(title,item_link)
    else:
        pass
        # Nothing !


#从mongodb中获取所有url信息
def get_mongo_links():
    links = []
    for item in url_list.find({},{'url': 1, '_id': 0}):
            links.append(item['url'])
    return links
    # print(links)

# get_mongo_links()





# spider 2  商家详情页信息抓取
def get_item_info(url):
    # url = 'http://bj.ganji.com/shouji/2444082302x.htm'            正常页面
    # url = 'http://jjcljj.5858.com/?adtype=1'                      页面不存在
    # url = 'http://bj.ganji.com/jiaju/888888x.htm'                 Nothing!!!
    wb_data = requests.get(url)
    time.sleep(1)
    soup = BeautifulSoup(wb_data.text,'lxml')
    no_longer_exist = 'error-tips1' in soup.prettify()

    if no_longer_exist:     # 如果页面显示不存在,结果为(True)
        pass
        # print('页面不存在')
    else:
        if not soup.find_all('ul', 'det-infor'):
            pass
            # print('nothings!!!')
        else:
            date = soup.select('.pr-5')[0].text.strip('\n ').strip('\xa0发布')
            title = soup.select('.title-name')[0].text
            type = soup.select('ul.det-infor > li > span > a')[0].text
            price = soup.select('.f22.fc-orange.f-type')[0].text
            area = str([a.text for a in soup.select('ul.det-infor > li > a')]).replace(',', '-').replace("'", "")
            # new_old_degree = soup.select('')
            # item_info.insert_one({'title': title, 'type': type, 'price': price, 'date': date, 'area': area})
            print({'title': title, 'type': type, 'price': price, 'date': date, 'area': area})


get_item_info('http://bj.ganji.com/jiaju/669766102x.htm')







# 查看不存在页面的详细信息
# url = 'http://bj.ganji.com/shouji/1234x.htm'
# wb_data = requests.get(url)
# soup = BeautifulSoup(wb_data.text,'lxml')
# print(soup.prettify())
# no_longer_exist = '404' in soup.find('script',type="text/javascript").get('src').split('/')
# no_longer_exist = 'error-tips1' in soup.prettify()
# print(no_longer_exist)





