#!/usr/bin/env python
# -*- coding=utf-8 -*-
#
# Copyright (c) 2014 Baidu.com, Inc. All Rights Reserved
#
"""
This module provide ....

Authors: duanyibo(duanyibo@baidu.com)
Date:    2018/12/3 下午7:55
"""
import collections

class Solution(object):
    def _lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        d = collections.defaultdict(int)
        l = ans = 0
        for i, c in enumerate(s):
            while l > 0 and d[c] > 0:
                d[s[i - l]] -= 1
                l -= 1
            d[c] += 1
            l += 1
            ans = max(ans, l)
        return ans

    def lengthOfLongestSubstring(self, s):
        d = {}
        # 无重复字符的起点
        start = 0
        ans = 0
        for i, c in enumerate(s):
            print start, c
            if c in d:
                start = max(start, d[c] + 1)
            d[c] = i
            ans = max(ans, i - start + 1)
        return ans

s = Solution()
string = "abcabcbb"
print s.lengthOfLongestSubstring(string)