#!/usr/bin/env python
# -*- coding=utf-8 -*-
#
# Copyright (c) 2014 Baidu.com, Inc. All Rights Reserved
#
"""
This module provide ....

Authors: duanyibo(duanyibo@baidu.com)
Date:    2019/1/10 下午3:41
"""
# 日期排序
# 回顾题目 柱子框起来的最大水量
# 思路 左柱 右柱

def maxWater(height):
    ans = left = 0
    right = len(height) - 1
    leftWall = rightWall = float("-inf")
    while left < right:
        if leftWall <= rightWall:
            ans += max(0, leftWall - height[left])
            leftWall = max(height[left], leftWall)
            left += 1
        else:
            ans += max(0, rightWall - height[right])
            leftWall = max(height[right], rightWall)
            right -= 1
    return ans

arr = [0,1,0,2,1,0,1,3,2,1,2,1]
print maxWater(arr)