#!/usr/bin/env python
# -*- coding: utf-8 -*-


class KthLargest(object):
    import heapq
    def __init__(self, k, nums):
        """
        :type k: int
        :type nums: List[int]
        """
        self.k = k
        self.que = nums
        heapq.heapify(self.que)


    def add(self, val):
        """
        :type val: int
        :rtype: int
        """
        heapq.heappush(self.que, val)
        while len(self.que) > self.k:
            heapq.heappop(self.que)
        return self.que[0]


