#!/usr/bin/env python
# -*- coding: utf-8 -*-

from lib.self_link import LinkList, Node

# reverse
l = LinkList()
l.add(1)
l.add(2)
l.add(3)
l.add(4)
l.add(5)
l.print_link_list()


# reverse
def reverse():
    head = l.head
    phead = head 
    while phead and phead.next:
        a = phead.next
        b = phead.next.next
        a.next = b.next
        b.next = a
        phead = a
    return head

reverse()
l.print_link_list()
