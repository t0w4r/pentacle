#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
    
    
    author:  wh1t3P1g <wh1t3P1g@gmail.com>
    description:
    
'''

queue_name = 'test'

app_token = "848bdbfe-0836-11e9-8ad6-00e04c680497"

defaults = {
    'broker_url': 'amqp://user:password@localhost',
    'task_serializer': 'json',
    'result_serializer': 'json',
    'result_expires': 60 * 60 * 24,
    'accept_content': ['json'],
    'timezone':'Europe/Oslo',
    'enable_utc': True,
    'result_backend': 'mongodb',
    'mongodb_backend_settings':
            {
                # 'host':'mongodb://root:password@192.168.99.16:27017',
                'host':'mongodb://root:password@localhost:27017',
                "database": "pentacle",
                "taskmeta_collection":'celery'
            }
}




