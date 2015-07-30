# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

from .models import Post
from mongoengine import *

MONGODB = 'tieba_rat'
connect(MONGODB)


def item2doc(item):
    doc = Post()
	for (k, v) in item.items():
		doc[k] = item[k]
	return doc

def list_n(List, n=0):
    if len(List) > n:
        return List[n]
    else:
        return None

class RatPipeline(object):

	def __init__(self):
        self.file = codecs.open('items.json', 'w', encoding='utf-8')

    def process_item(self, item, spider):
        d_item = dict(item)
        doc = item2doc(item)
        find = list_n(Post.objects(url_link=doc['url_link']))
        if find:
        	find.delete()
        find.save()
        line = json.dumps(d_item) + "\n"
        self.file.write(line.decode('unicode_escape'))
        return item


