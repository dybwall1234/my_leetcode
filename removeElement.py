#!/usr/bin/env python
# -*- coding=utf-8 -*-
#
# Copyright (c) 2014 Baidu.com, Inc. All Rights Reserved
#
"""
This module provide ....

Authors: duanyibo(duanyibo@baidu.com)
Date:    2018/7/24 下午11:08
"""
class Solution(object):
    def removeElement(self, nums, n, elem):
        j = 0
        for i in range(n):
            if nums[i] == elem:
                continue
            nums[j] = nums[i]
            j = j + 1
        return [nums[i] for i in range(j)]

so = Solution()
nums = [1,2,2,3,2,4]
n = 6
elem = 2
print so.removeElement(nums, n, 2)