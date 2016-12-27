#!/usr/bin/env python
# _*_ coding:utf-8 _*_
# __created by junxi__

from bs4 import BeautifulSoup
import requests,time,pymongo

client = pymongo.MongoClient('localhost',27017)
ceshi = client['ceshi']
url_list = ceshi['url_list_shoujihao']
item_info = ceshi['item_info_shoujihao']
url = 'http://bj.58.com/shoujihao/pn1/'
prefix = 'http://bj.58.com/shoujihao'


# a = 'http://jump.zhineng.58.com/jump?target=pZwY0jCfsvFJsWN3shPfUiq1pAqdph-CmytfnHEdn1T1n1TvnWTvrjK3sMPCIAd_THDLPHcQPWmdP1DOn19knHczP1b3P10vPjN1nkDQn1c1rH0zPWm1rjNOrTDYTHDYPHnkn1nkPWckPW9kTHNkTHNkTHcYnEDQTHDYP19drjmknW9OPWDKPT7_pgPYUARhITDQTHDKugF1pAqdgvw6pyQOxjDKsHDKTHTKnTDKuh7_0vNKPyP-mWbYrH0VPhRhPBYYPHIWsH9Yrj9VPHnYPjbQnAELmW6bTHcOrjT3n10vTHDOnHmLnHEQPWNknWNvrTDKnWEQTHDKna3knHc3P1bOrHcYPH01PHDzPTDKTEDKpZwY0jCfsvFJsWN3shPfUiq1pAqdph-CmytfnitKm1NfUMnQuv6rnduvp1cONbwAPM-Ku1YqTHDzPa3QrHc8nWTvsWnYTHTKPj6bnHIhuAu-uAnvmvN3P9&psid=175216657193801227987764533&entinfo=14530330620680_0&iuType=q_1&PGTID=0d3000f1-0000-1a74-e439-89258ad15822&ClickID=5'
# b = 'http://short.58.com/zd_p/abc78b43-9303-4322-81ec-8bfabe3da6b5/?target=dc-16-xgk_fegvcjemg_30211798039733q-feykn&end=end&psid=177155077193802145936414547&entinfo=27955163726122_0'
# # print(a.split('=')[-4].strip('_0&iuType'))
# print(b.split('/')[2])


# spider 1  获取58手机号类目单个页面所有帖子主题, 价格, 链接
def get_mobilenum_link(channel,pages):
    list_view = '{}/pn{}'.format(channel,str(pages+1))
    # http://bj.58.com/shoujihao/pn1/
    wb_data = requests.get(list_view)
    time.sleep(1)
    soup = BeautifulSoup(wb_data.text,'lxml')
    titles = soup.select('strong.number')
    links = soup.select('a.t')
    prices = soup.select('b.price')

    for title,price,link in zip(titles,prices,links):
        title1 = title.text
        link1 = link.get('href')
        price1 = price.text
        # http://bj.58.com/shoujihao/27971379396808x.shtml
        if link1.split('/')[2] == 'short.58.com':        # 处理链接为jump.zhineng.58.com 和 short.58.com的地址, 进行转换
            link2 = 'http://bj.58.com/shoujihao/{}x.shtml'.format(str(link1.split('=')[-1].strip('_0')))
            url_list.insert_one({'title': title1, 'price': price1, 'url': link2})
            print({'title': title1, 'price': price1, 'url': link2})
        elif link1.split('/')[2] == 'jump.zhineng.58.com':
            link3 = 'http://bj.58.com/shoujihao/{}x.shtml'.format(str(link1.split('=')[-1].strip('_0')))
            url_list.insert_one({'title': title1, 'price': price1, 'url': link3})
            print({'title': title1, 'price': price1, 'url': link3})
        else:
            url_list.insert_one({'title': title1, 'price': price1, 'url': link1.split('?')[0]})
            print({'title': title1, 'price': price1, 'url': link1.split('?')[0]})

get_mobilenum_link(prefix,1)

# 获取58手机号类目所有帖子的标题和链接, 并写入到 MongoDB 中
# for page in range(116):
#     get_mobilenum_link(prefix,page)






