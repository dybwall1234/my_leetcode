#!/usr/bin/env python
# -*- coding=utf-8 -*-
#
# Copyright (c) 2014 Baidu.com, Inc. All Rights Reserved
#
"""
This module provide ....

Authors: duanyibo(duanyibo@baidu.com)
Date:    2019/1/10 下午4:51
"""

import collections
class LRUCache:
    def __init__(self, capacity):
        self.od = collections.OrderedDict()
        self.cap = capacity

    def get(self, key):
        if key not in self.od: return -1
        # self.od.move_to_end(key) # python3
        value = self.od[key]
        del self.od[key]
        self.od[key] = value
        return self.od[key]

    def put(self, key, value):
        if key in self.od:
            del self.od[key]
            self.od[key] = value
        else:
            while len(self.od) >= self.cap:
                self.od.popitem(False)
            self.od[key] = value

obj = LRUCache(3)

obj.put('c',6)
obj.put('d',3)
obj.put('a',1)
obj.put('c',6)
obj.put('e',1)
param_1 = obj.get('c')
print (param_1)