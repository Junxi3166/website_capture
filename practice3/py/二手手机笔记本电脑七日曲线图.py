
# coding: utf-8

# In[5]:

import pymongo
from datetime import timedelta, date, datetime
import charts


# In[8]:

client = pymongo.MongoClient('localhost', 27017)
tongcheng = client['58tongcheng']
item_info = tongcheng['item_info']


# In[7]:

for i in item_info.find({'cates': {'$in': ['北京二手手机', '北京二手台式机/配件','北京二手笔记本']}}, {'cates': 1, '_id': 0}).limit(10):
    print(i['cates'][2])


# In[24]:

cate_list = []
for i in item_info.find({'cates': {'$in': ['北京二手手机', '北京二手台式机/配件','北京二手笔记本']}}, {'cates': 1, '_id': 0}):
    # print(i['cates'][2])
    cate_list.append(i['cates'][2])
cate_index = list(set(cate_list))
print(cate_index)


# In[20]:

for i in item_info.find({}, {'_id': 0, 'pub_date': 1}).limit(10):
    print(i)


# In[21]:

a = date(2015 , 5, 10)
print(a)


# In[22]:

d = timedelta(days=1)
print(d)


# In[3]:

def get_all_dates(date1,date2):
    the_date = date(int(date1.split('.')[0]), int(date1.split('.')[1]), int(date1.split('.')[2]))
    end_date = date(int(date2.split('.')[0]), int(date2.split('.')[1]), int(date2.split('.')[2]))
    days = timedelta(days=1)
    
    while the_date <= end_date:
        yield (the_date.strftime('%Y.%m.%d'))
        the_date = the_date + days


# In[13]:

for i in get_all_dates('2015.12.31','2016.01.06'):
    print(i)


# In[31]:

def get_data_within(date1,date2,cate_index):             
    for cate in cate_index:
        # print(cate)
        cate_day_posts = []
        for date in get_all_dates(date1,date2):
            a = list(item_info.find({'pub_date': date, 'cates': cate}))
            # print(a)
            # print(date,cate,len(a))
            each_day_post = len(a)
            cate_day_posts.append(each_day_post)
        data = {
            'name': cate,
            'data': cate_day_posts,
            'type': 'line',
        }
        yield data


# In[30]:

get_data_within('2016.01.05','2016.01.06', cate_index)


# In[33]:

options = {
    'chart'   : {'zoomType':'xy'},
    'title'   : {'text': '七天内发帖量统计'},
    'subtitle': {'text': '可视化统计图表'},
    'xAxis'   : {'categories': [i for i in get_all_dates('2015.12.31','2016.01.06')]},
    'yAxis'   : {'title': {'text': '数量'}}
    }

series = [i for i in get_data_within('2015.12.31','2016.01.06', ['北京二手台式机/配件', '北京二手笔记本', '北京二手手机'])]
         

charts.plot(series, options=options, show='inline')
# options=dict(title=dict(text='Charts are AWESOME!!!'))


# In[ ]:



