
# coding: utf-8

# In[3]:

import pymongo
from datetime import timedelta, date, datetime
import charts


# In[4]:

client = pymongo.MongoClient('localhost', 27017)
tongcheng = client['58tongcheng']
item_info = tongcheng['item_infoS']


# In[18]:

# 导入带 time 的json 数据，查看如下
for i in item_info.find().limit(5):
    print(i)


# In[150]:

pipeline = [
    {'$match':{'$and':[{'pub_date': '2016.01.11'}, {'time': 0}]}},
    {'$group':{'_id': {'$slice':['$area', 1]}, 'counts':{'$sum': 1}}},
    {'$sort':{'counts': 1}}
]


# In[151]:

for i in item_info.aggregate(pipeline):
    print(i)


# In[152]:

def data_gen(date,time):
    pipeline = [
        {'$match':{'$and':[{'pub_date': date}, {'time': time}]}},
        {'$group':{'_id': {'$slice':['$area', 1]}, 'counts':{'$sum': 1}}},
        {'$sort':{'counts': 1}}
    ]
    for i in item_info.aggregate(pipeline):
        yield [i['_id'][0],i['counts']]


# In[153]:

for i in data_gen('2016.01.11',0):
    print(i)


# In[154]:

# 绘制七天内未交易成功的商品中，各城区交易量的饼图


# In[155]:

options = {
    'chart'   : {'zoomType':'xy'},
    'title'   : {'text': '发帖量统计'},
    'subtitle': {'text': '2016.01.11二手物品在随后7天内，未交易成功的城区分布占比'},
    }


series =  [{
    'type': 'pie',
    'name': 'pie charts',
    'data':[i for i in data_gen('2016.01.11',0)]

        }]
charts.plot(series,options=options,show='inline')


# In[ ]:



