#!/usr/bin/env python
# -*- coding: utf-8 -*-



class Stack():
    def __init__(self, size):
        self.size = size
        self.count = 0
        self.stack = list()

    def push(self, item):
        self.count += 1
        self.stack.append(item)

    def pop(self):
        if self.is_empty():
            return Exception('stack is empty')
        else:
            self.count -= 1
            value = self.stack[self.count]
            del self.stack[self.count]
            return value

    def is_empty(self):
        if self.count < 0:
            return True
        else:
            return False

s = Stack(3)
for i in range(3):
    s.push(i)
print(s.stack)

for i in range(3):
    print s.pop()
print(s.stack)
