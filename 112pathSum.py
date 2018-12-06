#!/usr/bin/env python
# -*- coding=utf-8 -*-
#
# Copyright (c) 2014 Baidu.com, Inc. All Rights Reserved
#
"""
This module provide ....

Authors: duanyibo(duanyibo@baidu.com)
Date:    2018/12/2 下午4:57
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

class Solution():
    def hasPathSum(self, root,  sum):
        if root == None:
            return False
        if root.left == None and root.right == None:
            return sum - root.val == 0
            # 递归遍历左右子树
        if root.left != None or root.right != None:
            return self.hasPathSum(root.left, sum - root.val) or self.hasPathSum(root.right, sum - root.val)

data_list = [5,4,8,11,None,13,4,7,2,None,None,None,None,None,5,1]
root = node()
listTree = root.listcreattree(root, data_list, 0)

s = Solution()
print s.hasPathSum(listTree, 22)