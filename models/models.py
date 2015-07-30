from mongoengine import *

MONGODB = 'tieba_rat'
connect(MONGODB)


class Post(Document):
    url_link = StringField(max_length=300, required=True)
    rep_num = IntField(required=True)
    title = StringField(max_length=100, required=True)
    first_time = DateTimeField(max_length=20, required=True)
    last_time = DateTimeField(max_length=20, required=True)
    author = StringField(max_length=30, required=True)
    body = StringField(required=True)
