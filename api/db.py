#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
    
    
    author:  wh1t3P1g <wh1t3P1g@gmail.com>
    description:
    
'''
import motor.motor_tornado


class MongoDBClient(object):

    def __init__(self, config, database):
        client = motor.motor_tornado.MotorClient(config)
        self.db = client[database]

    async def insert_one(self, document):
        result = await self.db.insert_one(document)
        print('result %s' % repr(result.inserted_id))