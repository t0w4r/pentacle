#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
    
    
    author:  wh1t3P1g <wh1t3P1g@gmail.com>
    description:
    
'''
import string,random,time

def random_name():
    tm = time.localtime()
    dict_str = list(string.ascii_lowercase)
    return "".join(random.sample(dict_str, 5))+"_"+str(tm.tm_year)+str(tm.tm_mon)+str(tm.tm_mday)+str(tm.tm_hour)+str(tm.tm_min)