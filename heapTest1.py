#!/usr/bin/env python
# -*- coding=utf-8 -*-
#
# Copyright (c) 2014 Baidu.com, Inc. All Rights Reserved
#
"""
This module provide ....

Authors: duanyibo(duanyibo@baidu.com)
Date:    2018/12/6 下午1:54
"""
def sift(data, low, high):
    i = low      # 父节点
    j = 2 * i + 1   # 左子节点
    tmp = data[i]   # 父节点值
    while j <= high:    # 子节点在节点中
        if j < high and data[j] < data[j + 1]:  # 有右子节点且右节点比父节点值大
            j += 1
        if tmp < data[j]:
            data[i] = data[j]   # 将父节点替换成新的子节点的值
            i = j   # 变成新的父节点
            j = 2 * i + 1   # 新的子节点
        else:
            break
    data[i] = tmp   # 将替换的父节点值赋给最终的父节点


def heap_sort(data):
    n = len(data)
    # 创建堆
    mid = n//2
    for i in range(mid):
        sift(data, mid - i - 1, n-1)
    # 挨个出数
    for i in range(n):
        data[0], data[n-i-1] = data[n-i-1], data[0]     # 将最后一个值与父节点交互位置
        sift(data, 0, n-i-2)


li = [50, 16, 30, 10, 60, 90, 2, 80, 70]
heap_sort(li)
print(li)