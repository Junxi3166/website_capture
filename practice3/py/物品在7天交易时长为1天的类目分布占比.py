
# coding: utf-8

# In[1]:

import pymongo
from datetime import timedelta, date, datetime
import charts


# In[2]:

client = pymongo.MongoClient('localhost', 27017)
tongcheng = client['58tongcheng']
item_info = tongcheng['item_info']


# In[27]:

for i in item_info.find().limit(5):
    print(i)


# In[29]:

pipeline = [
    {'$match': {'$and': [{'pub_date': '2015.12.24'}, {'area': '朝阳'}]}},   # 匹配多个
    {'$group': {'_id': '$price', 'counts': {'$sum': 1}}},              # 数据重新进行分组
    {'$sort': {'counts': 1}},          # 排序，1 是正序，-1 是倒序
    {'$limit': 5}                  # 出现频率最高的 5 个价格
]


# In[30]:

for i in item_info.aggregate(pipeline):
    print(i)


# In[ ]:

pipeline2 = [
    {'$match':{'$and':[{'pub_date':'2015.12.25'},{'time':3}]}},
    {'$group':{'_id':{'$slice':['$cates',2,1]},'counts':{'$sum':1}}},
    {'$sort':{'counts':-1}}
]


# In[ ]:
'''
def data_gen(date,time):
    pipeline = [
    {'$match':{'$and':[{'pub_date':date},{'time':time}]}},
    {'$group':{'_id':{'$slice':['$cates',2,1]},'counts':{'$sum':1}}},
    {'$sort':{'counts':-1}}
]
    for i in item_info.aggregate(pipeline):
        yield [i['_id'][0],i['counts']]


# In[ ]:

for i in data_gen('2016.01.10',1):
    print(i)


# In[ ]:

options = {
    'chart'   : {'zoomType':'xy'},
    'title'   : {'text': '发帖量统计'},
    'subtitle': {'text': '2016.01.10二手物品在随后7天内，交易时长为1天的类目分布占比'},
    }


series =  [{
    'type': 'pie',
    'name': 'pie charts',
    'data':[i for i in data_gen('2016.01.10',1)]

        }]
charts.plot(series,options=options,show='inline')
'''

# In[32]:

# 因为没有 time 这个数据，所以使用模拟数据


# In[36]:

options = {
    'chart'   : {'zoomType':'xy'},
    'title'   : {'text': '发帖量统计'},
    'subtitle': {'text': '2016.01.10二手物品在随后7天内，交易时长为1天的类目分布占比'},
    }


series =  [{
    'type': 'pie',
    'name': 'pie charts',
    'data':[
            ['北京二手家电', 8836],
            ['北京二手文体/户外/乐器', 5337],
            ['北京二手数码产品', 4405],
            ['北京二手服装/鞋帽/箱包', 4074],
            ['北京二手母婴/儿童用品', 3124],
            ['北京二手台式机/配件', 2863],
            ['北京二手图书/音像/软件', 2777],
            ['北京二手办公用品/设备', 2496],
            ['北京二手家具', 1903],
            ['北京二手美容/保健', 1838],
            ['北京二手手机', 1603],
            ['北京二手笔记本', 1174],
            ['北京二手设备', 1004],
            ['北京其他二手物品', 761],
            ['北京二手平板电脑', 724] 
            ]
        }]
        
charts.plot(series,options=options,show='inline')


# In[ ]:




# In[ ]:



