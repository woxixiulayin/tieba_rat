#!/usr/bin/env python
from model import *
import urllib
import urllib2
import json
from BeautifulSoup import BeautifulSoup
from lxml import etree

import sys
reload(sys)
sys.setdefaultencoding( "utf-8" )

tieba_preurl = "http://tieba.baidu.com/"


def li2post(li):
    li_obj = json.loads(li.get('data-field'))
    post = Post()
    post.id = li_obj['id']
    post.author = li_obj['author_name']
    post.rep_num = int(li_obj['reply_num'])
    post.last_time = li.xpath(
        './/span[@class="threadlist_reply_date j_reply_data"]')[0].text.strip()
    link_a = li.xpath('.//a[@class="j_th_tit"]')[0]
    post.title = link_a.get('title')
    post.url_link = tieba_preurl + link_a.get('href')
    post.body = li.xpath('.//div[@class="threadlist_abs threadlist_abs_onlyline"]')[0].text
    post.tags = 'tieba'
    return post


class My_url():

    def __init__(self, url):
        self.resp = urllib2.urlopen(url)
        self.content = self.resp.read().decode('utf-8')
        self.tree = etree.HTML(self.content)
        # print self.tree.xpath('//li[@class="j_thread_list clearfix"]')
        if not self.content:
            self.content = 'no response'

    def prettify(self):
        self.content = BeautifulSoup(self.content).prettify()
        return self.content

    def save(self, filename='my.html'):
        self.prettify()
        with open('my.html', 'wb') as f:
            f.write(self.content)


class Tieba_url(My_url):

    def get_all_li(self):
        self.all_li = self.tree.xpath('//li[@class="j_thread_list clearfix"]')
        return self.all_li

    def get_li_need(self, rep_num_least=100):
        self.get_all_li()
        self.posts = []
        for li in self.all_li:
            post = li2post(li)
            if post.rep_num >= rep_num_least:
                self.posts.append(post)
        return self.posts

    def save_posts(self):
        session = DBsession()
        for post in self.posts:
            session.add(post)
        session.commit()
        session.close()


class DB():

    def findall(self):
        session = DBsession()
    	posts = session.query(Post).all()
    	session.close()
    	return posts

# url = "http://tieba.baidu.com/f?kw=%C3%C0%BE%E7"
# l = Tieba_url(url)
# l.get_li_need()
# l.save_posts()

