#!/usr/bin/env python
# -*- coding=utf-8 -*-
#
# Copyright (c) 2014 Baidu.com, Inc. All Rights Reserved
#
"""
This module provide ....

Authors: duanyibo(duanyibo@baidu.com)
Date:    2018/12/4 下午3:37
"""


class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        nums = sorted(nums1 + nums2)
        t_len = len(nums)
        if t_len == 1:
            return nums[0]

        if t_len % 2:
            return nums[t_len / 2]
        else:
            return (nums[t_len / 2] + nums[t_len / 2 - 1]) / 2.0