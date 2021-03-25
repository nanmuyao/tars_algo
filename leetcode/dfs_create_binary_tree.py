#!/usr/bin/env python
# -*- coding: utf-8 -*-

#尝试生成一颗二叉树
class Tree:
    def __init__(self):
	self.left = None
	self.right = None
	self.val = None

val = 0
def dfs_create_tree(root, left, right, level=2):
    if left > level and right > level:
	return
    if left < level:
        print('left===', left)
	root.left = Tree()
	root.val = val
	root = root.left
	dfs_create_tree(root, left + 1, right, level)
    if right < level:
        print('right===============', right)
	root.right = Tree()
	root = root.right
	dfs_create_tree(root, left, right + 1, level)

t = Tree
dfs_create_tree(t, 0, 0, level=3)

def dfs_traval(root):
    if not root:
        return
    dfs_traval(root.left)
    print('val====', root.val)
    dfs_traval(root.right)
