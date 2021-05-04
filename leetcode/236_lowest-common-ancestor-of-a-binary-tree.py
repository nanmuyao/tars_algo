#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


# 这几天好像突然搞懂了递归的套路，
# 比如说二叉树的这种题经常可以用递归的思想来解决。
# 我不管你是怎么遍历的，我只需要明确我的递归函数的作用是什么，
# 千万不要跳到递归函数中去用你的人脑压栈。 
# 比如说找最近公共祖先这道题，算法的框架是这样的，
# 我就让递归函数TreeNode lowestCommonAncestor(TreeNode root, TreeNode p, TreeNode q)
# 的作用是从当前根节点向下搜索 p、q是否存在于当前节点的左右子树中，找到就返回相应的节点。

# 思路很好
# https://leetcode-cn.com/problems/lowest-common-ancestor-of-a-binary-tree/solution/236-er-cha-shu-de-zui-jin-gong-gong-zu-x-tl5b/
class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if root in (None, p, q):
            return root
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        return root if left and right else left if left else right
