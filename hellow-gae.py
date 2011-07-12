#!/usr/bin/env python
# -*- coding: utf-8 -*-

from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app

class InterfaceServiceHandler(webapp.RequestHandler):
    def get(self):
        self.response.out.write("Hellow Google AppEngine")


app = webapp.WSGIApplication([('/', InterfaceServiceHandler)])


def main():
    run_wsgi_app(app)


if __name__ == "__main__":
    main()
