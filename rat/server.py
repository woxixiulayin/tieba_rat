#!/usr/bin/env python
# -*- coding: utf-8 -*-

import bottle
from bottle import Bottle, template
from bottle import jinja2_view as view
from rat import DB

app = Bottle()
bottle.TEMPLATE_PATH.append('./templates')
db = DB()

@app.route('/index')
@view('index')
def index():
    return dict(posts=db.findall())

app.run(host='localhost', port=8080, debug=True)
