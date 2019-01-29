#!/usr/bin/env python
# -*- coding=utf-8 -*-
#
# Copyright (c) 2014 Baidu.com, Inc. All Rights Reserved
#
"""
This module provide ....

Authors: duanyibo(duanyibo@baidu.com)
Date:    2019/1/29 下午4:27
"""
import heapq

import LinkedListCycle
from LinkedListCycle import ListNode

def mergeKList(lists):
    heap = []
    p = dummy = ListNode(-1)
    for node in lists:
        if not node:
            continue
        heapq.heappush(heap, (node.val, node))

    while heap:
        val, node = heapq.heappop(heap)
        p.next = node
        p = p.next
        if node.next:
            node = node.next
            heapq.heappush(heap, (node.val, node))
    return dummy.next

data = [[2,4,5],[1,3,4],[1,6]]
listLink = []
for list in data:
    linkList = LinkedListCycle.initList(list)
    listLink.append(linkList)


re = mergeKList(listLink)
print re.val
temp = re.next
while (temp):
    print temp.val
    temp = temp.next