from bs4 import BeautifulSoup
import requests
import time
import pymongo
import random



client = pymongo.MongoClient('localhost', 27017)
ganji = client['ganji']
url_list = ganji['url_list_new']
item_info = ganji['item_info_new']

headers  = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36',
    'Connection':'keep-alive'
}

# http://cn-proxy.com/
proxy_list = [
    'http://111.13.7.42:81',
    'http://183.95.152.159:3128',
    'http://211.153.17.151:80',
    ]
proxy_ip = random.choice(proxy_list) # 随机获取代理ip
proxies = {'http': proxy_ip}



# spider 1
def get_links_from(channel, pages, who_sells='o'):
    # http://bj.ganji.com/ershoubijibendiannao/o3/
    # o for personal a for merchant
    time.sleep(2)
    list_view = '{}{}{}/'.format(channel, str(who_sells), str(pages))
    # wb_data = requests.get(list_view,headers=headers,proxies=proxies)
    wb_data = requests.get(list_view)
    soup = BeautifulSoup(wb_data.text, 'lxml')
    if soup.find('ul', 'pageLink'):
        for link in soup.select('.zzinfo td.t a'):
            item_link = link.get('href')
            url_list.insert_one({'url': item_link})
            print(item_link)
            # return urls
    else:
        # It's the last page !
        pass

# get_links_from('http://bj.ganji.com/jiaju/', 5)


# spider 2
def get_item_info_from(url, data=None):
    time.sleep(1)
    wb_data = requests.get(url, headers=headers)
    soup = BeautifulSoup(wb_data.text, 'lxml')
    if soup.find('span', 'soldout_btn'):
        pass
        # print('商品已下架')
    else:
        soup = BeautifulSoup(wb_data.text, 'lxml')
        cates = soup.select('span.crb_i > a')
        if len(cates) == 3:     # 分类判断
            cate = cates[2].text
            # print(cate)
        else:
            cate = cates[1].text
            # print(cate)
        data = {
            'title': soup.select('h1.info_titile')[0].text,
            'price': soup.select('span.price_now i')[0].text,
            # 'pub_date': soup.select('.pr-5')[0].text.strip().split(' ')[0],
            # 'area': list(map(lambda x:x.text,soup.select('ul.det-infor > li:nth-of-type(3) > a'))),
            # 'cates': list(soup.select('ul.det-infor > li:nth-of-type(1) > span')[0].stripped_strings),
            'area': soup.select('.palce_li > span i')[0].text,
            'cates': cate,
            'url': url.split('?')[0]
        }
        print(data)
        item_info.insert_one(data)


# get_item_info_from('http://zhuanzhuan.ganji.com/detail/801290327291625479z.shtml?from=pc&source=ganji&cate=%E5%8C%97%E4%BA%AC%E8%B5%B6%E9%9B%86%7C%E5%8C%97%E4%BA%AC%E4%BA%8C%E6%89%8B%7C%E5%8C%97%E4%BA%AC%E5%AE%B6%E7%94%A8%E7%94%B5%E5%99%A8%7C%E5%8C%97%E4%BA%AC%E4%BA%8C%E6%89%8B%E7%94%B5%E8%A7%86&cateurl=bj|wu|jiadian|dianshi')
# get_item_info_from('http://zhuanzhuan.ganji.com/detail/797384445754605569z.shtml?from=pc&source=ganji&cate=%E5%8C%97%E4%BA%AC%E8%B5%B6%E9%9B%86%7C%E5%8C%97%E4%BA%AC%E4%BA%8C%E6%89%8B%7C%E5%8C%97%E4%BA%AC%E4%BA%8C%E6%89%8B%E7%AC%94%E8%AE%B0%E6%9C%AC&cateurl=bj|wu|ershoubijibendiannao')