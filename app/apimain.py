#!/usr/bin/env python
# encoding: utf-8
import webapp2 as webapp
from google.appengine.ext.webapp import util

from avtryck.api.handlers.route import RouteListHandler, RouteHandler
from avtryck.api.handlers.place import PlaceListHandler, PlaceHandler
from avtryck.api.handlers.record import RecordListHandler, RecordHandler

config = {}

def main():
    application = webapp.WSGIApplication(
        [
                webapp.Route(r'/api/routes', RouteListHandler),
                webapp.Route(r'/api/routes/<route_id:[\d]+>', RouteHandler),
                webapp.Route(r'/api/routes/<route_id:[\d]+>/places', PlaceListHandler),
                webapp.Route(r'/api/routes/<route_id:[\d]+>/places/<place_id:[\d]+>', PlaceHandler),
                webapp.Route(r'/api/routes/<route_id:[\d]+>/places/<place_id:[\d]+>/records', RecordListHandler),
                webapp.Route(r'/api/routes/<route_id:[\d]+>/places/<place_id:[\d]+>/records/<record_id:[\d]+>', RecordHandler),
        ],
        config=config,
        debug=True)
    util.run_wsgi_app(application)


if __name__ == '__main__':
    main()