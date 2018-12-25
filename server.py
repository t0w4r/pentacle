#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
    
    
    author:  wh1t3P1g <wh1t3P1g@gmail.com>
    description:
    
'''
import tornado.web
from tornado.ioloop import IOLoop
from tornado.httpserver import HTTPServer
from tornado.options import define,options
from motor import motor_tornado
from pymongo.errors import InvalidName
from config.config import defaults
from tornado.log import app_log
from lib.api.handler import *

define('debug', default=True, help='enable debug mode') # 多进程的时候 如果报错，就加if 判断 options.debug是否存在
define('port',default=8000,type=int,help='web port')



def make_app():

    return tornado.web.Application([
            (r"/",IndexHandler),
            (r"/client/auth",ClientAuthHandler)
        ],debug=options.debug)

def make_db():
    client = motor_tornado.MotorClient(defaults['mongodb_backend_settings']['host'])
    db = None
    try:
        db = client[defaults['mongodb_backend_settings']['database']]
    except InvalidName:
        app_log.error("Database InvalidName")
        IOLoop.current().stop()
        exit()
    return db

if __name__ == '__main__':
    options.parse_command_line()
    app = make_app()

    http_server = HTTPServer(app)
    http_server.bind(options.port)
    http_server.start(1)
    app.settings['db'] = make_db()
    try:
        IOLoop.current().start()
    except KeyboardInterrupt:
        IOLoop.current().stop()