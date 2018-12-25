#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
    
    
    author:  wh1t3P1g <wh1t3P1g@gmail.com>
    description:
    
'''
from __future__ import absolute_import, unicode_literals
from celery import Celery
from config.config import defaults,queue_name
app = Celery(queue_name)

# Optional configuration, see the application user guide.
app.conf.update(defaults)

if __name__ == '__main__':
    app.start()