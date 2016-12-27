
# coding: utf-8

# In[2]:

import pymongo
from string import punctuation
import charts


# In[7]:

client = pymongo.MongoClient('localhost', 27017)
tongcheng = client['58tongcheng']
item_info = tongcheng['item_info']


# In[13]:

for i in item_info.find().limit(30):
    print(i['cates'][2])


# In[12]:

cate_list = []
for i in item_info.find():
    cate_list.append(i['cates'][2])
cate_index = list(set(cate_list))
print(cate_index)


# In[14]:

post_times = []
for index in cate_index:
    post_times.append(cate_list.count(index))
print(post_times)


# In[21]:

def data_gen(types):             # pythn生成器
    length = 0
    if length <= len(cate_index):
        for cate,times in zip(cate_index,post_times):
            data = {
                'name': cate,
                'data': [times],
                'type': types,
            }
            yield data
            length += 1


# In[22]:

data_gen('column')


# In[23]:

for i in data_gen('column'):
    print(i)


# In[24]:

series = [data for data in data_gen('column')]
charts.plot(series, show='inline', options=dict(title=dict(text='北京城区二手物品发帖量')))


# In[ ]:



