#!/usr/bin/env python
# -*- coding=utf-8 -*-
#
# Copyright (c) 2014 Baidu.com, Inc. All Rights Reserved
#
"""
This module provide ....

Authors: duanyibo(duanyibo@baidu.com)
Date:    2018/12/26 下午8:23
"""
# 理解题目
# 选择方法
# 实现
# 考虑其他方法
class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        ans = left = 0
        right = len(height) - 1
        leftWall = rightWall = float("-inf")
        while left <= right:
            if leftWall <= rightWall:
                ans += max(0, leftWall - height[left])
                leftWall = max(leftWall, height[left])
                left += 1
            else:
                ans += max(0, rightWall - height[right])
                rightWall = max(rightWall, height[right])
                right -= 1
        return ans
s = Solution()
arr = [0,1,0,2,1,0,1,3,2,1,2,1]
print s.trap(arr)