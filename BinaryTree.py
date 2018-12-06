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

    def findNode(self, root, val):
        if root == None:
            return None

        if root.val == val:
            # print root.val
            print val, 'null' if root.left == None else root.left.val, 'null' if root.right == None else root.right.val
        else:
            self.findNode(root.left, val) or self.findNode(root.right, val)

    def tree2Json(self, root):
        d = {}
        if root != None:
            d['val'] = root.val
        if root.left != None:
            d['left'] = self.tree2Json(root.left)
        if root.right != None:
            d['right'] = self.tree2Json(root.right)
        return d

class BiTree(object):
    def __init__(self, data_list):
        #初始化即将传入的列表的迭代器
        self.it = iter(data_list)

    def createBiTree(self, bt=None):
        try:
            #步进获取下一个元素
            next_data = next(self.it)
            #如果当前列表元素为'#', 则认为其为 None
            if next_data is None:
                bt = None
            else:
                bt = node(next_data)
                bt.left = self.createBiTree(bt.left)
                bt.right = self.createBiTree(bt.right)
        except Exception as e:
            print(e)

        return bt

    #先序遍历函数
    def preOrderTrave(self, bt):
        if bt is not None:
            print bt.val,
            self.preOrderTrave(bt.left)
            self.preOrderTrave(bt.right)

    #中序遍历函数
    def inOrderTrave(self, bt):
        if bt is not None:
            self.inOrderTrave(bt.left)
            print(bt.val) ,
            self.inOrderTrave(bt.right)

    #后序遍历函数
    def postOrderTrave(self, bt):
        if bt is not None:
            self.postOrderTrave(bt.left)
            self.postOrderTrave(bt.right)
            print(bt.val),

    #综合打印
    def printTrave(self, bt):
        print("先序遍历: ")
        self.preOrderTrave(bt)
        print('\n')
        print("中序遍历: ")
        self.inOrderTrave(bt)
        print('\n')
        print("后序遍历: ")
        self.postOrderTrave(bt)
        print('\n')


if __name__ == '__main__':
    # data_list = [5, 4, 8, 11, None, 13, 4, 7, 2, None, None, None, None, 1, None]
    data_list = [5,4,8,11,None,13,4,7,2,None,None,None,None,None,5,1]
    from heapSort import heapSort
    heap1 = heapSort()
    heap1.print_tree(data_list)
    # root = node()
    # root = root.listcreattree(root, data_list, 0)
    # btree = BiTree(data_list)
    # root = btree.createBiTree()
    # btree.printTrave(root)
    # root.findNode(root, 4)