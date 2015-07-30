#!/usr/bin/env python
# -*- coding: utf-8 -*-
import scrapy
import sys
import re
import json
from scrapy.spiders import Spider
from scrapy.selector import Selector
from ..items import Post_Item

rep_num_for_good = 100
Tieba_admin_url = "http://tieba.baidu.com/"

def list_n(List, n=0):
    if len(List) > n:
        return List[n]
    else:
        return None


class Rat_spider(Spider):
    name = 'rat'
    start_urls = [
        "http://tieba.baidu.com/f?kw=%C3%C0%BE%E7&fr=ala0&loc=rec"
    ]

    def parse(self, response):
        post_items = []
        sel = response.xpath('//li[@class="j_thread_list clearfix"]')
        print len(sel)
        titles = ''
        for li in sel:
            post = Post_Item()
            data_field = json.loads(
                list_n(li.xpath('.//@data-field').extract()))
            post['rep_num'] = data_field['reply_num']
            if post['rep_num'] > rep_num_for_good:
                post['url_link'] = Tieba_admin_url + \
                    'p/' + str(data_field['id'])
                post['author'] = data_field['author_name'].encode('utf-8')
                post['title'] = list_n(
                    li.xpath('.//a[@class="j_th_tit"]/text()').extract())
                post['body'] = list_n(li.xpath(
                    './/div[@class="threadlist_abs threadlist_abs_onlyline"]/text()').extract())
                post['last_time'] = list_n(li.xpath(
                    './/span[@class="threadlist_reply_date j_reply_data"]/text()').extract()).strip()
                post_items.append(post)
        return post_items

