from django.db import models
from mongoengine import *
from mongoengine import connect
# connect('wbsite', host='127.0.0.1', port=27017)
connect('58tongcheng', host='127.0.0.1', port=27017)

# ORM

# class ArtiInfo(Document):
#     des = StringField()
#     title = StringField()
#     scores = StringField()
#     tags = ListField(StringField)
#
#     meta = {
#         'collection': 'arti_info3'}
#
# for i in ArtiInfo.objects:
#     print(i)
# print(len(ItemInfo.objects))


class ItemInfo(Document):
    title = StringField()
    cates = ListField(StringField())
    area = ListField(StringField())
    # price = ListField(StringField)
    # time = StringField()
    price = IntField()
    pub_date = StringField()
    url = StringField()
    look = StringField()
    meta = {'collection': 'item_infoS'}


pipeline = [
    {'$match': {'$and': [{'pub_date':{'$gte': '2015.12.25','$lte': '2015.12.27'}},{'area':{'$all': ['朝阳']}}]}},
    {'$group': {'_id': {'$slice': ['$cates',2,1]},'counts': {'$sum': 1}}},
    {'$limit': 3},
    {'$sort': {'counts' :-1}}
]

# for i in ItemInfo._get_collection().aggregate(pipeline):
#     print(i)
