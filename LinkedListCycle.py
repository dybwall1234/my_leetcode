#!/usr/bin/env python
# -*- coding=utf-8 -*-
#
# Copyright (c) 2014 Baidu.com, Inc. All Rights Reserved
#
"""
This module provide ....

Authors: duanyibo(duanyibo@baidu.com)
Date:    2018/11/22 下午7:33
"""


class ListNode:
    # Constructor to initialize
    # the node object
    def __init__(self, data):
        self.val = data
        self.next = None

class LinkedList:
    # Function to initialize head
    def __init__(self):
        self.head = None

    def initList(self, data):
        # 创建头结点
        self.head = ListNode(data[0])
        p = self.head
        # 逐个为 data 内的数据创建结点, 建立链表
        for i in data[1:]:
            node = ListNode(i)
            p.next = node
            p = p.next

    # Function to insert a new
    # node at the beginning
    def push(self, new_data):
        new_node = ListNode(new_data)
        new_node.next = self.head
        self.head = new_node

    def printList(self):
        temp = self.head
        while (temp):
            temp = temp.next

    def detectLoop(self):
        s = set()
        temp = self.head
        while (temp):

            # If we have already has
            # this node in hashmap it
            # means their is a cycle
            # (Because you we encountering
            # the node second time).
            if (temp in s):
                return True

            # If we are seeing the node for
            # the first time, insert it in hash
            s.add(temp)

            temp = temp.next

        return False

if __name__ == '__main__':
    llist = LinkedList()
    data = [20, 4, 15, 10]
    for item in data:
        llist.push(item)

    llist.printList()
    # Create a loop for testing
    llist.head.next.next.next.next = llist.head;

    if (llist.detectLoop()):
        print ("Loop found")
    else:
        print ("No Loop ")
