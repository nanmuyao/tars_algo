#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        win = []
        res = []
        # 双端队列
        for i, v in enumerate(nums):
            # 最左侧的元素根据坐标可以判断是否有效
            if i >= k and win[0] <= i - k:
                win.pop(0)
            # 最右侧元素根据value判断，如果窗口中的元素小于要加入的元素，那么弹出
            while win and nums[win[-1]] < v:
                win.pop()

            win.append(i)
            if i >= k - 1:
                res.append(nums[win[0]])
        return res
