
# coding: utf-8

# In[5]:

import pymongo
from datetime import timedelta, date
import charts


# In[6]:

client = pymongo.MongoClient('localhost', 27017)
ganji = client['ganji']
item_info = ganji['item_info_new']


# In[7]:

for i in item_info.find().limit(5):
    print(i)


# In[8]:

for i in item_info.find().limit(5):
    print(i['area'])


# In[9]:

area_list = []
for i in item_info.find():
    # print(i['area'].split('-')[0])
    if i['area'].split('-')[0] == '北京':
        # print(i['area'])
        area_list.append(i['area'])
area_index = list(set(area_list))
print(area_index)


# In[10]:

pipeline = [
    {'$match': {'area': '北京-朝阳'}},  
    # {'$match': {'$and': [{'cates': '北京二手家居百货'}, {'area': '北京-朝阳'}]}}, 
    {'$group': {'_id': '$cates', 'counts': {'$sum': 1}}},              # 数据重新进行分组 ，统计类目出现的次数
    {'$sort': {'counts': -1}},               # 1 是正序，-1 是倒序
]


# In[11]:

line = 0
for i in item_info.aggregate(pipeline):
    line += 1
    print(i)
    if line == 3:
        break


# In[12]:

'''
def data_gen(area):
    line = 0
    pipeline = [
        {'$match': {'area': area}},  
        {'$group': {'_id': '$cates', 'counts': {'$sum': 1}}},              
        {'$sort': {'counts': -1}},               
    ]
    for i in item_info.aggregate(pipeline):
        line += 1
        yield [i['_id'],i['counts']]
        if line == 3:
            break
'''


# In[35]:

def data_gen(area,limit):
    pipeline = [
        {'$match': {'area': area}},  
        {'$group': {'_id': '$cates', 'counts': {'$sum': 1}}},
        {'$sort': {'counts': -1}},
        {'$limit': limit},                    # 前几行
    ]

    for i in item_info.aggregate(pipeline):
        data = {
            'name': i['_id'],
            'data': [i['counts']],
            'type': 'column'
        }
        yield data


# In[42]:

for i in data_gen('北京-朝阳', 5):
    print(i)


# In[41]:

area = '北京-朝阳'
limit = 5
series = [i for i in data_gen(area, limit)]

options = {
    'chart'   : {'zoomType':'xy'},
    'title'   : {'text': '发帖最多的 TOP5 类目'},
    'subtitle': {'text': area},
     'yAxis'   : {'title': {'text': '数量'}}
    }

charts.plot(series,options=options,show='inline')


# In[ ]:



