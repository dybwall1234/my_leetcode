#!/usr/bin/env python
# -*- coding=utf-8 -*-
#
# Copyright (c) 2014 Baidu.com, Inc. All Rights Reserved
#
"""
This module provide ....

Authors: duanyibo(duanyibo@baidu.com)
Date:    2018/12/1 下午10:40
"""
class Solution(object):
    def updateMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        h, w = len(matrix), len(matrix[0])
        # 初始化结果矩阵为0
        ans = [[0] * w for x in range(h)]
        # 处理非0坐标
        queue = [(x, y) for x in range(h) for y in range(w) if matrix[x][y]]
        step = 0
        # BFS
        while queue:
            step += 1
            nqueue, mqueue = [], []
            for x, y in queue:
                zero = 0
                # 四个方向判断是否有0
                for dx, dy in zip((1, 0, -1, 0), (0, 1, 0, -1)):
                    nx, ny = x + dx, y + dy
                    # condition
                    if 0 <= nx < h and 0 <= ny < w and matrix[nx][ny] == 0:
                        zero += 1
                if zero:
                    ans[x][y] = step
                    mqueue.append((x, y))
                else: # 当前处理不完的,留个下次处理, 步数保留
                    nqueue.append((x, y))
            # print step, ans, queue, nqueue, mqueue
            for x, y in mqueue: # 由于步数保留, 结果矩阵是另一个, 原始矩阵里被处理过的重新赋值为0, 以便上面的condition一致简捷
                matrix[x][y] = 0
            queue = nqueue
        return ans

matrix = [ [0, 0, 0], [0, 1 ,0], [1, 1, 1]]
s = Solution()
print s.updateMatrix(matrix)

# 靠谱解释 http://www.voidcn.com/article/p-tqvugamj-bpc.html