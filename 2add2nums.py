#!/usr/bin/env python
# -*- coding=utf-8 -*-
#
# Copyright (c) 2014 Baidu.com, Inc. All Rights Reserved
#
"""
This module provide ....

Authors: duanyibo(duanyibo@baidu.com)
Date:    2018/12/3 下午6:13
"""
from LinkedListCycle import ListNode

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        dummy = ListNode(0)
        current, carry = dummy, 0

        while l1 is not None or l2 is not None:
            val = carry
            if l1 is not None:
                val += l1.val
                l1 = l1.next
            if l2 is not None:
                val += l2.val
                l2 = l2.next
            carry, val = val / 10, val % 10
            current.next = ListNode(val)
            current = current.next
            print current.val
        # 最后一组运算处理
        if carry == 1:
            current.next = ListNode(1)

        return dummy.next

data1 = [5,6]
l1 = [ListNode(i) for i in data1]
for i in range(len(data1) - 1):
    l1[i].next = l1[i + 1]

data2 = [7]
l2 = [ListNode(i) for i in data2]
for i in range(len(data2) - 1):
    l2[i].next = l2[i + 1]

s = Solution()
result = s.addTwoNumbers(l1[0], l2[0])
while result.next:
    print str(result.val) + '-',
    result = result.next
print result.val