#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        nums = sorted(nums)
        for i, v in enumerate(nums):
            # 这里要注意游标的重复
            if i > 0 and nums[i] == nums[i-1]:
                continue

            l, r = i + 1, len(nums) - 1
            while l < r: # 这里要有一个遍历
                s = v + nums[l] + nums[r]
                if s > 0:
                    r-=1
                elif s < 0:
                    l+=1
                else:
                    res.append([v, nums[l], nums[r]])
                    while l < r and nums[l] == nums[l + 1]:
                        l+=1
                    while r > l and nums[r] == nums[r-1]:
                        r-=1
                    l+=1
                    r-=1
        return res
