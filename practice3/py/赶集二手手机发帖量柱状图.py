
# coding: utf-8

# In[25]:

import pymongo
from string import punctuation
import charts


# In[26]:

client = pymongo.MongoClient('localhost',27017)
ceshi = client['ceshi']
item_info = ceshi['item_info_shouji_Y']


# In[27]:

for i in item_info.find().limit(30):
    print(i['area'])


# In[28]:

area_list = []
for i in item_info.find():
    a = str(i['area']).replace('None','不明').split('-')
    item_info.update({'_id': i['_id']}, {'$set': {'area': a}})


# In[29]:

for i in item_info.find().limit(30):
    print(i['area'])


# In[30]:

series = [
    {
    'name': 'OS X',
    'data': [11],
    'type': 'column'
}, {
    'name': 'Ubuntu',
    'data': [8],
    'type': 'column',
    'color':'#ff0066'
}, {
    'name': 'Windows',
    'data': [12],
    'type': 'column'
}, {
    'name': 'Others',
    'data': [29],
    'type': 'column'
}
         ]

series2 = [{'name': 'John','data': [5],'type': 'column'},{'name': 'John','data': [5],'type': 'column'}]


charts.plot(series, show='inline', options=dict(title=dict(text='Charts are AWESOME!!!')))


# In[31]:

area_list = []
for i in item_info.find():
    area_list.append(i['area'][0])
area_index = list(set(area_list))
print(area_index)


# In[32]:

post_times = []
for index in area_index:
    post_times.append(area_list.count(index))
print(post_times)


# In[33]:

def data_gen(types):             # python生成器
    length = 0
    if length <= len(area_index):
        for area,times in zip(area_index,post_times):
            data = {
                'name': area,
                'data': [times],
                'type': types,
            }
            yield data
            length += 1


# In[34]:

data_gen('column')


# In[35]:

for i in data_gen('column'):
    print(i)


# In[36]:

series = [data for data in data_gen('column')]
charts.plot(series, show='inline', options=dict(title=dict(text='七日内北京城区二手手机发帖量')))


# In[ ]:



