#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
    
    
    author:  wh1t3P1g <wh1t3P1g@gmail.com>
    description:
    
'''
from tornado.web import RequestHandler

class BaseHandler(RequestHandler):

    async def prepare(self):
        await self.auth()

    async def auth(self):
        # 这里验证 config 里面 验证token
        token = self.get_cookie('pentacle_token')
        doc = await self.settings['db'].clientAuth.find_one({'token':token})
        if not doc or not doc.get('token'):
            self.send_error(404)

    def send_error(self, status_code=500, **kwargs):
        self.set_status(status_code)
        self.finish({"info": status_code})

