#!/usr/bin/env python
# encoding: utf-8
"""
place.py

Created by Joakim Bodin on 2011-04-10.
Copyright (c) 2011 __MyCompanyName__. All rights reserved.
"""

import webapp2 as webapp

class PlaceListHandler(webapp.RequestHandler):
    def get(self, route_id):
        pass

class PlaceHandler(webapp.RequestHandler):
    def get(self, route_id, place_id):
        pass

    def delete(self, route_id, place_id):
        pass
