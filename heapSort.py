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
import random
import time
from datetime import datetime

def bigSift(data, low, high):
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

def sift(data, low, high):
    i = low      # 父节点
    j = 2 * i + 1   # 左子节点
    tmp = data[i]   # 父节点值
    while j <= high:    # 子节点在节点中
        if j < high and data[j] > data[j + 1]:  # 有右子节点且右节点比父节点值大
            j += 1
        if tmp > data[j]:
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
        print data
    # 挨个出数
    for i in range(n):
        data[0], data[n-i-1] = data[n-i-1], data[0]     # 将最后一个值与父节点交互位置
        sift(data, 0, n-i-2)

def head_top0(data, n):
    # 创建堆
    mid = n // 2
    head_data = data[:n]
    for i in range(mid):
        sift(head_data, mid - i - 1, n - 1)
    # print head_data
    for item in data[n:]:
        if item > head_data[0]:
            head_data[0] = item
            sift(head_data, 0, n-1)
    return head_data

def head_top(data, head_data, n):
    for item in data:
        if item > head_data[0]:
            head_data[0] = item
            sift(head_data, 0, n-1)
    return head_data


def heap_out():
    head_data = []
    for i in range(100):
        li = open('data/%s' % i).readlines()[0].split(',')
        li = [int(_) for _ in li]
        print i, str(datetime.now())
        if i != 0:
            head_top(li, head_data, 10000)
        else:
            head_data = head_top0(li, 10000)
        print str(datetime.now())
    print head_data

def writefile():
    time_start=time.time()
    for i in range(100):
        filew = open('data/%s' % i, 'w')
        li =[str(random.randint(0, 1000000000)) for _ in range(10000000)]
        filew.write(','.join(li))
        filew.close()
    time_end=time.time()
    # li = [50, 16, 30, 10, 60, 90, 2, 80, 70]

    print time_start, time_end

if __name__ == '__main__':
    # writefile()
    print str(datetime.now())
    # li = [random.randint(0, 1000000000) for _ in range(10000000)]
    # print 'generate', str(datetime.now())
    # tofile = open('data/random.txt', 'w')
    # for i in li:
    #     tofile.write(str(i) + '\n')
    # tofile.close()
    # print 'write', str(datetime.now())
    li = open('data/random.txt').readlines()
    print 'read', str(datetime.now())
    li = [int(i.strip()) for i in li]
    print 'trans', str(datetime.now())
    time_start=time.time()
    head_out = head_top0(li, 10000000)
    # print head_out
    time_end=time.time()
    print('totally cost',time_end-time_start)