
# coding: utf-8

# In[70]:

import pymongo
from string import punctuation
from datetime import timedelta, date, datetime
import charts


# In[71]:

client = pymongo.MongoClient('localhost', 27017)
tongcheng = client['58tongcheng']
item_info = tongcheng['item_info']


# In[3]:

for i in item_info.find({}, {'area': 1, '_id': 0}).limit(10):
    print(i)


# In[7]:

for i in item_info.find():
    if i['area']:
        area = [i for i in i['area'] if i not in punctuation]
    else:
        area = ['不明']
    item_info.update({'_id':i['_id']},{'$set':{'area':area}})


# In[35]:

for i in item_info.find({'pub_date': {'$in': ['2016.01.12', '2016.01.14']}}, {'area': {'$slice': 1}, '_id': 0, 'url': 0, 'title': 0, 'look': 0, 'cates': 0, 'price': 0}).limit(30):
    print(i)


# In[72]:

options = {
    'chart'   : {'zoomType':'xy'},
    'title'   : {'text': 'Monthly Average Temperature'},
    'subtitle': {'text': 'Source: WorldClimate.com'},
    'xAxis'   : {'categories': ['周一', '周二', '周三', '周四']},
    'yAxis'   : {'title': {'text': '数量'}}
    }

series = [
    {
    'name': 'OS X',
    'data': [11,2,3,4],
    'type': 'line',
    'y':5
}, {
    'name': 'Ubuntu',
    'data': [8,5,6,7],
    'type': 'line',
    'color':'#ff0066'
}, {
    'name': 'Windows',
    'data': [12,6,7,2],
    'type': 'line'
}, {
    'name': 'Others',
    'data': [29,24,68,23],
    'type': 'line'
}
         ]

charts.plot(series, options=options,show='inline')
# options=dict(title=dict(text='Charts are AWESOME!!!'))


# In[36]:

for i in item_info.find({}, {'_id': 0, 'pub_date': 1}).limit(30):
    print(i)


# In[31]:

for i in item_info.find():          # 把 - 替换为 .
    frags = i['pub_date'].split('-') 
    if len(frags) == 1:
        date = frags[0]
    else:
        date = '{}.{}.{}'.format(frags[0], frags[1], frags[2])
    item_info.update_one({'_id': i['_id']}, {'$set': {'pub_date': date}})   # 更新到数据库


# In[32]:

for i in item_info.find({}, {'_id': 0, 'pub_date': 1}).limit(30):
    print(i)


# In[17]:

a = date(2015 , 5, 10)
print(a)


# In[18]:

d = timedelta(days=1)
print(d)


# In[31]:

def get_all_dates(date1,date2):
    the_date = date(int(date1.split('.')[0]), int(date1.split('.')[1]), int(date1.split('.')[2]))
    end_date = date(int(date2.split('.')[0]), int(date2.split('.')[1]), int(date2.split('.')[2]))
    days = timedelta(days=1)
    
    while the_date <= end_date:
        yield (the_date.strftime('%Y.%m.%d'))
        the_date = the_date + days


# In[66]:

for i in get_all_dates('2015.12.24','2016.01.05'):
    print(i)


# In[79]:

def get_data_within(date1,date2,areas):
    for area in areas:
        area_day_posts = []
        for date in get_all_dates(date1,date2):
            a = list(item_info.find({'pub_date': date, 'area': area}))
            # print(a)
            # print('#'*20,date,area,len(a),'#'*20)
            each_day_post = len(a)
            area_day_posts.append(each_day_post)
        data = {
            'name': area,
            'data': area_day_posts,
            'type': 'line',
        }
        yield data


# In[76]:

for i in get_data_within('2015.12.24','2016.01.05',['朝阳','海淀','房山']):
    print(i)


# In[49]:

a = [i for i in item_info.find({}, {'_id': 0, 'pub_date': 1}).limit(30)]
print(len(a))


# In[77]:

options = {
    'chart'   : {'zoomType':'xy'},
    'title'   : {'text': '发帖量统计'},
    'subtitle': {'text': '可视化统计图表'},
    'xAxis'   : {'categories': [i for i in get_all_dates('2015.12.24','2016.01.05')]},
    'yAxis'   : {'title': {'text': '数量'}}
    }

series = [i for i in get_data_within('2015.12.24','2016.01.05',['朝阳','海淀','房山'])]
         

charts.plot(series, options=options, show='inline')
# options=dict(title=dict(text='Charts are AWESOME!!!'))


# In[ ]:



