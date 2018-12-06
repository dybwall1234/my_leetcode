#!/usr/bin/env python
# -*- coding=utf-8 -*-
#
# Copyright (c) 2014 Baidu.com, Inc. All Rights Reserved
#
"""
This module provide ....

Authors: duanyibo(duanyibo@baidu.com)
Date:    2018/11/22 下午5:20
"""

class node():
    def __init__(self, k=None, l=None, r=None):
        self.val = k
        self.left = l
        self.right = r

    def listcreattree(self, root, llist, i):  ###用列表递归创建二叉树，
        if i < len(llist):
            if llist[i] is None:
                return None  ###这里的return很重要
            else:
                root = node(k=llist[i])
                root.left = self.listcreattree(root.left, llist, 2 * i + 1)
                root.right = self.listcreattree(root.right, llist, 2 * i + 2)
                return root  ###这里的return很重要
        return root


class BiTree(object):

    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root is None:
            return True
        return self.help(root.left, root.right)

    def help(self, left, right):
        if not left and not right:
            return True

        if not left:
            return False
        if not right:
            return False
        if left.val != right.val:
            return False

        # print left.val, right.val
        return self.help(left.left, right.right) and self.help(right.left, left.right)

# data_list = [1,2,2, None,3, None,3]
data_list = [1,2,2,3,4,4,3]
root = node()
root = root.listcreattree(root, data_list, 0)
btree = BiTree()

print(btree.isSymmetric(root))