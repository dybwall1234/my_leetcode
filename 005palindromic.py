#!/usr/bin/env python
# -*- coding=utf-8 -*-
#
# Copyright (c) 2014 Baidu.com, Inc. All Rights Reserved
#
"""
This module provide ....

Authors: duanyibo(duanyibo@baidu.com)
Date:    2018/12/4 下午3:43
"""
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        longest, mid = "", (len(s) - 1) / 2
        i, j = mid, mid
        while i >= 0 and j < len(s):
            args = [(s, i, i), (s, i, i + 1), (s, j, j), (s, j, j + 1)]
            for arg in args:
                # 从中间往两边找
                tmp = self.longestPalindromeByAxis(*arg)
                if len(tmp) > len(longest):
                    longest = tmp
            if len(longest) >= i * 2:
                if len(longest) == 1:
                    return s[0]
                return longest
            i, j = i - 1, j + 1
        return longest

    def longestPalindromeByAxis(self, s, left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left, right = left - 1, right + 1
        return s[left + 1: right]

string = 'asdfdggr'
s = Solution()
print s.longestPalindrome(string)