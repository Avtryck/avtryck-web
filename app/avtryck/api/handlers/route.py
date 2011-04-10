#!/usr/bin/env python
# encoding: utf-8
"""
route.py

Created by Joakim Bodin on 2011-04-10.
Copyright (c) 2011 __MyCompanyName__. All rights reserved.
"""

import webapp2 as webapp
from django.utils import simplejson

class RouteListHandler(webapp.RequestHandler):
    def get(self):
        self.response.out.write(simplejson.dumps({
            'yo': 'json',
        }))

class RouteHandler(webapp.RequestHandler):
    def get(self):
        pass
