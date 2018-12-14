#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
    
    
    author:  wh1t3P1g <wh1t3P1g@gmail.com>
    description:
    
'''
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
]