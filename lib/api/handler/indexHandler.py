#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
    
    
    author:  wh1t3P1g <wh1t3P1g@gmail.com>
    description:
    
'''
from lib.api.baseHandler import BaseHandler

class IndexHandler(BaseHandler):

    def get(self):
        self.write({"info":"Success"})