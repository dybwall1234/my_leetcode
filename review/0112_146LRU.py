#!/usr/bin/env python
# -*- coding=utf-8 -*-
#
# Copyright (c) 2014 Baidu.com, Inc. All Rights Reserved
#
"""
This module provide ....

Authors: duanyibo(duanyibo@baidu.com)
Date:    2019/1/12 下午11:05
"""
import collections
class LRU():
    def __init__(self, cap):
        self.od = collections.OrderedDict()
        self.cap = cap

    def get(self, key):
        if key not in self.od: return -1
        value = self.od[key]
        del self.od[key]
        self.od[key] = value
        return value

    def put(self, key, value):
        if key in self.od:
            del self.od[key]
        else:
            if len(self.od) >= self.cap:
                self.od.popitem(False)
        self.od[key] = value

obj = LRU(3)
obj.put('c',6)
obj.put('d',3)
obj.put('a',1)
obj.put('c',6)
obj.put('e',1)
param_1 = obj.get('c')
print (param_1)
