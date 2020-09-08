#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Node():
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value


class BTree():
    def __init__(self):
        self.root = None

    def insert(self, value, root=None):
        if not self.root:
            self.root = Node(value)
            return 

        root = root or self.root
        if root:
            if value > root.value:
                if root.right:
                    self.insert(value, root.right)
                else:
                    root.right = Node(value)
            else:
                if root.left:
                    self.insert(value, root.left)
                else:
                    root.left = Node(value)

    def pre_order_r(self, root):
        """递归先序遍历"""
        if not root:
            return
        print(root.value)
        self.pre_order_r(root.left)
        self.pre_order_r(root.right)

   # 先序打印二叉树（非递归）
    def pre_order(self, node):
        stack = [node]
        while len(stack) > 0:
            print(node.value)
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
            node = stack.pop() 

btree = BTree()  
l = [8, 3, 9, 1, 13, 4]
for i in l:
    btree.insert(i)

btree.pre_order_r(btree.root)
print('===')
print(btree.root.left.left.value)
print('===')
print(btree.root.right.right.value)
print('===')
btree.pre_order(btree.root)

import networkx as nx
import matplotlib.pyplot as plt

def create_graph(G, node, pos={}, x=0, y=0, layer=1):
    pos[node.value] = (x, y)
    if node.left:
        G.add_edge(node.value, node.left.value)
        l_x, l_y = x - 1 / 2 ** layer, y - 1
        l_layer = layer + 1
        create_graph(G, node.left, x=l_x, y=l_y, pos=pos, layer=l_layer)
    if node.right:
        G.add_edge(node.value, node.right.value)
        r_x, r_y = x + 1 / 2 ** layer, y - 1
        r_layer = layer + 1
        create_graph(G, node.right, x=r_x, y=r_y, pos=pos, layer=r_layer)
    return (G, pos)

def draw(node):   # 以某个节点为根画图
    graph = nx.DiGraph()
    graph, pos = create_graph(graph, node)
    fig, ax = plt.subplots(figsize=(20, 20))  # 比例可以根据树的深度适当调节
    nx.draw_networkx(graph, pos, ax=ax, node_size=500)
    plt.show()

#draw(btree.root)
