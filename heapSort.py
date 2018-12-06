#!/usr/bin/env python
# -*- coding=utf-8 -*-
#
# Copyright (c) 2014 Baidu.com, Inc. All Rights Reserved
#
"""
This module provide ....

Authors: duanyibo(duanyibo@baidu.com)
Date:    2018/12/6 上午10:23
"""
import math,random
import heapq

class heapSort():   #网上找的打印树的一个函数，很好用，谁用谁知道
    def print_tree(self, array): #打印堆排序使用
        '''
        深度 前空格 元素间空格
        1     7       0
        2     3       7
        3     1       3
        4     0       1
        '''
        # first=[0]
        # first.extend(array)
        # array=first
        index = 1
        depth = int(math.ceil(math.log(len(array), 2))) # 因为补0了，不然应该是math.ceil(math.log2(len(array)+1))
        sep = '  '
        for i in range(depth):
            offset = 2 ** i
            print(sep * (2 ** (depth - i - 1) - 1)),
            line = array[index:index + offset]
            for j, x in enumerate(line):
                print("{:>{}}".format(x, len(sep))),
                interval = 0 if i == 0 else 2 ** (depth - i) - 1
                if j < len(line) - 1:
                    print(sep * interval),
            index += offset
            print ''
