#!/usr/bin/env python
# -*- coding=utf-8 -*-
#
# Copyright (c) 2014 Baidu.com, Inc. All Rights Reserved
#
"""
This module provide ....

Authors: duanyibo(duanyibo@baidu.com)
Date:    2018/7/23 上午11:17
"""
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        dt = {}
        lth = len(nums)
        for i in range(lth):
            compete = target - nums[i]
            if dt.has_key(compete):
                return [dt[compete], i]
            else:
                dt[nums[i]] = i


t = Solution()
nums = [0,4,3,0]
target = 0
print t.twoSum(nums, target)