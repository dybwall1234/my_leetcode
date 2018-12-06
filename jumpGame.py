#!/usr/bin/env python
# -*- coding=utf-8 -*-
#
# Copyright (c) 2014 Baidu.com, Inc. All Rights Reserved
#
"""
This module provide ....

Authors: duanyibo(duanyibo@baidu.com)
Date:    2018/11/22 下午5:20
"""

def canJump(nums):
    n = len(nums)
    if n == 0:
        return True
    v = nums[0]
    for i in range(n)[1:]:
        v = v - 1
        if v < 0:
            return False
        if v < nums[i]:
            v = nums[i]
    return True

nums = [2,3,1,1,4]
# nums = [3,2,1,0,4]
print canJump(nums)
