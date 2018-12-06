#!/usr/bin/env python
# -*- coding=utf-8 -*-
#
# Copyright (c) 2014 Baidu.com, Inc. All Rights Reserved
#
"""
This module provide ....

Authors: duanyibo(duanyibo@baidu.com)
Date:    2018/12/4 下午5:12
"""


class Solution(object):
    def fourSumCount(self, A, B, C, D):
        """
        :type A: List[int]
        :type B: List[int]
        :type C: List[int]
        :type D: List[int]
        :rtype: int
        """
        ans = 0
        abDict = {}
        for i in range(len(A)):
            for j in range(len(B)):
                if A[i] + B[j] not in abDict:
                    abDict[A[i] + B[j]] = 1
                else:
                    abDict[A[i] + B[j]] += 1

        for i in range(len(C)):
            for j in range(len(D)):
                if -C[i] - D[j] in abDict:
                    ans += abDict[-C[i] - D[j]]
        return ans