#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
    
    
    author:  wh1t3P1g <wh1t3P1g@gmail.com>
    description:
    
'''
import uuid
import time
from lib.core.common import random_name


class Task(object):
    __slots__ = (
        'taskid',
        'name',
        'mode',
        'targets',
        'description',
        'state',
        'create_time',
        'finish_time',
        'child_task',
        'parent_task',
        'modules',
        'finished_modules',
        'results',
        'proxy',
    )

    def __init__(self, data):
        self.taskid = str(uuid.uuid1()) # task标示
        self.name = data['name'] if data.__contains__('name') else random_name() # 任务名
        self.mode = data['mode'] if data.__contains__('mode') else 0 # 任务模式 0=> 域名模式 1=> fofa模式
        self.targets = data['targets'] if data.__contains__('targets') else [] # 任务目标 可以是单个ip 单个url 或者ip，url列表
        self.description = data['description'] if data.__contains__('description') else '' # 任务描述
        self.state = data['state'] if data.__contains__('state') else '' # 任务状态 waiting running finished
        self.create_time = time.asctime() # 任务创建时间
        self.finish_time = None # 任务结束时间 所有的module都运行完毕
        self.child_task = data['child_task'] if data.__contains__('child_task') else '' # 子任务 由父任务衍生出来 一般为一连续的module调用
        self.parent_task = data['parent_task'] if data.__contains__('parent_task') else '' # 该任务的父任务，当子任务完成后，告诉
        self.modules = data['modules'] if data.__contains__('modules') else [] # 该任务下的待检测模块(每个模块的uuid) 当一个模块任务结束时，从这个列表中移除，并添加到已完成列表
        self.finished_modules = [] # 以完成的检测模块
        self.results = dict() # 当module结束时，填充  初始化为dict
        self.proxy = data['state'] if data.__contains__('state') else '' # 该任务是否调用代理池 true or false


    def is_finished(self):
        return False if self.modules else True

    def to_dict(self):
        return {
            'taskid': self.taskid,
            'name': self.name,
            'mode': self.mode,
            'targets': self.targets,
            'description': self.description,
            'state': self.state,
            'create_time': self.create_time,
            'finish_time': self.finish_time,
            'child_task': self.child_task,
            'parent_task': self.parent_task,
            'modules': self.modules,
            'finished_modules': self.finished_modules,
            'results': self.results,
            'proxy': self.proxy,
        }


class Module(object):
    '''
    模块实例
    '''
    __slots__ = (
        'moduleid',
        'name',
        'filepath',
        'author',
        'description',
        'config',
        'schedule',
        'schedule_time',
    )
    def __init__(self, data):
        self.moduleid = str(uuid.uuid1()) # module uuid
        self.name = data['name'] if data.__contains__('name') else random_name() # module名
        self.filepath = data['filepath'] if data.__contains__('filepath') else '' # module的路径
        self.description = data['description'] if data.__contains__('description') else '' # 描述
        self.author = data['author'] if data.__contains__('author') else '' # 作者
        self.config = data['config'] if data.__contains__('config') else {} # module的配置
        self.schedule = data['schedule'] if data.__contains__('schedule') else False # 是否为循环模块任务
        self.schedule_time = data['schedule_time'] if data.__contains__('schedule_time') else 0 # 循环时间间隔

    def to_dict(self):
        return {
            'moduleid': self.moduleid,
            'name': self.name,
            'filepath': self.filepath,
            'description': self.description,
            'author': self.author,
            'config': self.config,
            'schedule': self.schedule,
            'schedule_time': self.schedule_time,
        }

    def finished(self):
        pass

if __name__ == '__main__':
    module = Module({'filepath':'sdf'})
    task = Task({'state':'sdf'})
    print(task.to_dict())
    print(module.to_dict())