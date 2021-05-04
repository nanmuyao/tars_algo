#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        res = self.inorder(root)
        # 测试用例里有一个[1,1]
        sorted_res = sorted(set(res))
        return sorted_res == res

    def inorder(self, root):
        if not root:
            # 这里要注意，返回的是空数组
            return []
        return self.inorder(root.left) + [root.val] + self.inorder(root.right)
