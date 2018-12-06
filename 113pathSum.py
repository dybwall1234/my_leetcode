#!/usr/bin/env python
# -*- coding=utf-8 -*-
#
# Copyright (c) 2014 Baidu.com, Inc. All Rights Reserved
#
"""
This module provide ....

Authors: duanyibo(duanyibo@baidu.com)
Date:    2018/12/2 下午7:54
"""
from BinaryTree import node
class Solution():
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        self.res = []
        self.total = sum

        def caculate(root, sum, templist):
            if not root:
                return
            if not root.left and not root.right:
                if root.val + sum == self.total:
                    self.res.append(templist + [root.val])
            if root.left:
                caculate(root.left, sum + root.val, templist + [root.val])
            if root.right:
                caculate(root.right, sum + root.val, templist + [root.val])
        caculate(root, 0, [])
        return self.res



data_list = [5,4,8,11,None,13,4,7,2,None,None,None,None,None,5,1]
root = node()
listTree = root.listcreattree(root, data_list, 0)

s = Solution()
print s.pathSum(listTree, 22)

