#!/usr/bin/env python
# -*- coding: utf-8 -*-

def reverse(head):
    if not head or not head.next:
        return head
    last_node = reverse(head)
    head.next.next = head
    head.next = None
    return last_node
