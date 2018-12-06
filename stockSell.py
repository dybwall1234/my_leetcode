#!/usr/bin/env python
# -*- coding=utf-8 -*-
#
# Copyright (c) 2014 Baidu.com, Inc. All Rights Reserved
#
"""
This module provide ....

Authors: duanyibo(duanyibo@baidu.com)
Date:    2018/11/20 下午7:19
"""

def maxProfit1(prices):
    lth = len(prices)
    if lth < 1:
        return 0
    minP = prices[0]
    profit = prices[1] - prices[0]
    for i in range(lth)[2:]:
        minP = min(minP, prices[i - 1])
        profit = max(profit, prices[i] - minP)
    if profit < 0:
        return 0
    return profit