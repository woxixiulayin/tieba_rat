#!/usr/bin/env python
# -*- coding: utf-8 -*-

import bottle
from bottle import Bottle, template
from bottle import jinja2_view as view


app = Bottle()
bottle.TEMPLATE_PATH.append('./templates')


@app.route('/index')
def index():
	return template('index')

app.run(host='localhost', port=8080, debug=True)
