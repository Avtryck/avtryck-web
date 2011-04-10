#!/usr/bin/env python
# encoding: utf-8
import webapp2 as webapp
from google.appengine.ext.webapp import util

from app.avtryck.api.handlers.route import RouteListHandler, RouteHandler
from app.avtryck.api.handlers.place import PlaceListHandler, PlaceHandler
from app.avtryck.api.handlers.record import RecordListHandler, RecordHandler

config = {}

def main():
    application = webapp.WSGIApplication(
        [
                webapp.Route('/routes', RouteListHandler),
                webapp.Route('/routes/<routeId>', RouteHandler),
                webapp.Route('/routes/<routeId>/places', PlaceListHandler),
                webapp.Route('/routes/<routeId>/places/<placeId>', PlaceHandler),
                webapp.Route('/routes/<routeId>/places/<placeId>/records', RecordListHandler),
                webapp.Route('/routes/<routeId>/places/<placeId>/records/<recordId>', RecordHandler),
        ],
        config=config,
        debug=True)
    util.run_wsgi_app(application)


if __name__ == '__main__':
    main()