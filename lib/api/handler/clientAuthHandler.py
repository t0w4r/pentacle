#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
    
    
    author:  wh1t3P1g <wh1t3P1g@gmail.com>
    description:
    
'''
import tornado.web
from config.config import app_token
import uuid
class ClientAuthHandler(tornado.web.RequestHandler):
    '''
    new a client key
    '''
    async def post(self):
        token = self.get_body_argument('token')
        if token == app_token:
            # new a client token, then insert into mongodb
            db = self.settings['db']
            ret_token = str(uuid.uuid1())
            db.clientAuth.insert_one({'token': ret_token})
            self.write({"token": ret_token})
            # the client should store the token, and use it for next time
        else:
            self.send_error()

    def send_error(self, status_code=500, **kwargs):
        self.set_status(status_code)
        self.finish({"info": status_code})