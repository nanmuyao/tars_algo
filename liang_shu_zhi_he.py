#!/usr/bin/env python
# -*- coding: utf-8 -*-


# nums = [2, 7, 11, 15] target=9
# nums[0] + nums[1] = 2 + 7 = 9 所以放回[0, 1]
#给定 nums = [2, 7, 11, 15], target = 9
#
#因为 nums[0] + nums[1] = 2 + 7 = 9
#所以返回 [0, 1]

'''
class Solution(object):
    def twoSum_v1(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        target_index = []
        d = dict()
        for i, value in enumerate(nums):
            d.update({value: i})
        for value, index in d.items():
            need_value = target - value
            need_value_index = d.get(need_value)
            if need_value_index and index < need_value_index:
                target_index.append(index)
                target_index.append(need_value_index)
        target_index = list(set(target_index))
        return target_index


s = Solution()

nums = [2, 7, 11, 15]
print(s.twoSum(nums, 9))

nums = [3, 3]
print(s.twoSum(nums, 6))
'''
# 得审题，每个target只有一种答案
class Solution(object):
    def twoSum(self, nums, target):
        hashmap={}
        for ind,num in enumerate(nums):
            hashmap[num] = ind
        print hashmap
        for i,num in enumerate(nums):
            j = hashmap.get(target - num)
            if j is not None and i!=j:
                return [i,j]

s = Solution()

# nums = [2, 7, 11, 15]
# print(s.twoSum(nums, 9))

nums = [3, 3, 3]
print(s.twoSum(nums, 6))
