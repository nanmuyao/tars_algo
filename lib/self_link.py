#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Node():
    def __init__(self, value):
        self.pre = None
        self.next = None
        self.value = value


class LinkList():
    def __init__(self):
        self.head = None
        self.tail = None

    def add(self, v):
        node = Node(v)
        if not self.head:
            self.head = node

        if not self.tail:
            self.tail = node
        else:
            node.pre = self.tail
            self.tail.next = node
            self.tail = node

    def get_node(self, v):
        cur = self.head
        while cur.next:
            if cur.value == v:
                return v
            else:
                cur = cur.next
        return None

    def delete(self, v):
        cur = self.head
        while True:
            if cur.value == v:
                if cur.pre:
                    cur.pre.next = cur.next
                else:
                    self.head = cur.next

                if cur.next:
                    cur.next.pre = cur.pre
                else:
                    self.tail = cur.pre

                return True 
            else:
                cur = cur.next
        return False

    def print_link_list(self):
        cur = self.head
        while True:
            if cur:
                print(cur.value)
                cur = cur.next
            else:
                break
        print('==============')


#l = LinkList()
#l.add(1)
#l.add(3)
#l.add(4)
#l.print_link_list()
#l.delete(1)
#l.print_link_list()
#l.delete(4)
#l.print_link_list()
#l.delete(3)
#l.print_link_list()
