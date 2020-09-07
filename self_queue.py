#!/usr/bin/env python
# -*- coding: utf-8 -*-



class Queue():
    def __init__(self, size):
        self.size = size
        self.end = 0
        self.queue = list()


    def push(self, item):
    	self.end += 1
        self.queue.append(item)


    def pop(self):
        if self.is_empty():
            return Exception('stack is empty')
        else:
            self.end -= 1
            value = self.queue[0]
            del self.queue[0]
            return value


    def is_empty(self):
        if 0 == self.end:
	    return True
        else:
	    return False

q = Queue(3)
for i in range(3):
    q.push(i)
print q.queue

for i in range(3):
    print q.pop()
