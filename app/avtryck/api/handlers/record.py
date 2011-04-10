#!/usr/bin/env python
# encoding: utf-8
"""
record.py

Created by Joakim Bodin on 2011-04-10.
Copyright (c) 2011 __MyCompanyName__. All rights reserved.
"""

import webapp2 as webapp

class RecordListHandler(webapp.RequestHandler):
    def get(self, route_id, place_id):
        pass

class RecordHandler(webapp.RequestHandler):
    def get(self, route_id, place_id, record_id):
        pass

    def delete(self, route_id, place_id, record_id):
        pass
