#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
    
    
    author:  wh1t3P1g <wh1t3P1g@gmail.com>
    description:
    
'''
from tornado.web import RequestHandler,Application
from tornado.ioloop import IOLoop
from tornado.httpserver import HTTPServer
from tornado.options import define,options
from pentacle import add,test
define('port',default=8000,type=int)

class IndexHandler(RequestHandler):
   def get(self):
       r = test.delay(2)

       self.write(r.id)


class ArticleHandler(RequestHandler):
   def initialize(self,title):
       print('-->initialize()')
       self.title = title

   def get(self):
       self.write('你正在查看文章：%s'% self.title)

if __name__ == '__main__':
   options.parse_command_line()

   app = Application([(r'/',IndexHandler),(r'/article',ArticleHandler,{'title':'你>希望自己成为什么样的人，最终就会成为那样的人。'})],debug=True)
   http_server = HTTPServer(app)
   http_server.bind(options.port)
   http_server.start(1)

   IOLoop.current().start()