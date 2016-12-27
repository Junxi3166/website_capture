from django.db import models
from mongoengine import *
from mongoengine import connect
connect('58tongcheng', host='127.0.0.1', port=27017)

# ORM


class ArtiInfo(Document):
    title = StringField()
    cates = ListField(StringField())
    area = ListField(StringField())
    # price = ListField(StringField)
    price = StringField()
    pub_date = StringField()
    url = StringField()
    look = StringField()

    meta = {
        'collection': 'item_info'}

# for i in ArtiInfo.objects:
#     print(i)

print(len(ArtiInfo.objects))
