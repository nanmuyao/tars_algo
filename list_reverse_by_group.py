#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        phead = ListNode(0)
        phead.next = head
        stack = []
        tmp_k = k
        cur = phead
        while cur.next:
            cur_node = cur.next
            stack.append(cur_node)
            tmp_k-=1
            if tmp_k == 0:
                tmp_k = k

                # 进行翻转
                first_node_next = None
                while len(stack) > 0:
                    node = stack.pop()
                    if not first_node_next:
                        first_node_next = node.next
                    phead.next = node
                    phead = phead.next
                if first_node_next:
                    first_node_next = None
                    phead.next = first_node_next
