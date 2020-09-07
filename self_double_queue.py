#!/usr/bin/env python
# -*- coding: utf-8 -*-



class Queue():
    def __init__(self):
        self.size = 0
        self.queue = list()

    def push_rear(self, item):
        self.size+=1
        self.queue.append(item)

    def push_front(self, item):
        self.size+=1
        self.queue.insert(0, item)

    def pop_front(self):
        if self.is_empty():
            raise Exception('stack is empty')
        else:
            value = self.queue[0]
            print('front', value)
            del self.queue[0]
            self.size -= 1
            return value

    def pop_rear(self):
        if self.is_empty():
            raise Exception('stack is empty')
        else:
            value = self.queue[-1]
            print('rear', value)
            del self.queue[-1]
            self.size -= 1
            return value

    def is_empty(self):
        print(self.size)
        if 0 == len(self.queue):
            return True
        else:
            return False

q = Queue()

def test():
    word = 'abc'
    for char in word:
        q.push_front(char)  

    while True:
        try:
            char_front = q.pop_front()
            char_rear = q.pop_rear()
            if char_rear != char_front:
                print('no hui wen')
                break
        except Exception as queue_is_empty:
            print('is hui wen')
            break

test()

