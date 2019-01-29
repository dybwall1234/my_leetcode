#!/usr/bin/env python
# -*- coding=utf-8 -*-
#
# Copyright (c) 2014 Baidu.com, Inc. All Rights Reserved
#
"""
This module provide ....

Authors: duanyibo(duanyibo@baidu.com)
Date:    2019/1/22 下午3:33
"""
from Queue import PriorityQueue
import heapq

from LinkedListCycle import ListNode, LinkedList
import LinkedListCycle

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        # 使用小根堆
        heap = []
        p = dummy = ListNode(-1)
        for i in xrange(0, len(lists)):
            node = lists[i]
            if not node:
                continue
            heapq.heappush(heap, (node.val, node))

        while heap:
            value, node = heapq.heappop(heap)
            p.next = node
            p = p.next
            if node.next:
                node = node.next
                heapq.heappush(heap, (node.val, node))
        return dummy.next

    def divideNconquer(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        amount = len(lists)
        interval = 1
        while interval < amount:
            for i in range(0, amount - interval, interval * 2):
                lists[i] = self.merge2Lists(lists[i], lists[i + interval])
            interval *= 2
        return lists[0] if amount > 0 else lists

    def merge2Lists(self, l1, l2):
        head = point = ListNode(0)
        while l1 and l2:
            if l1.val <= l2.val:
                point.next = l1
                l1 = l1.next
            else:
                point.next = l2
                l2 = l1
                l1 = point.next.next
            point = point.next
        if not l1:
            point.next = l2
        else:
            point.next = l1
        return head.next

data = [[2,4,5],[1,3,4],[1,6]]
listLink = []
for list in data:
    linkList = LinkedListCycle.initList(list)
    listLink.append(linkList)


s = Solution()
re = s.mergeKLists(listLink)
print re.val
temp = re.next
while (temp):
    print temp.val
    temp = temp.next