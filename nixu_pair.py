#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 1,2,3,4,5 
# 5,4,3,2,1
# 0 + 1 + 2 + 3 + 4 = 10

# 时间复杂度O(n2)
def reverse_pair(list_value):
    print(list_value)
    reverse_pair_count = 0
    while len(list_value):
        last_value = list_value.pop()
        for i in list_value:
            if last_value < i:
                reverse_pair_count += 1
    print(reverse_pair_count)


#l = [6, 2, 8, 1, 9, 0]
#    0  1  0  3  0  5
#reverse_pair(l)
#l = [1, 2, 3, 4, 5]
#    0  1  0  3  0  5
#reverse_pair(l)
#l = [5, 4, 3, 2, 1]
#    0  1  0  3  0  5
#reverse_pair(l)

def merge_two_list(left_nums, right_nums):
    arr = []
    while i < len(left_nums) and j < len(right_nums):
        if left_nums[i] <= right_nums[j]:
            arr.append(left_nums[i])
            i+=1
        else:
            arr.append(right_nums[j])
            j+=1

    arr.extend(left_nums[i:]) 
    arr.extend(right_nums[j:]) 
    return arr

def merge(nums):
    length = len(nums)
    if length <= 1:
        return nums

    mid = length // 2
    left_nums = merge(nums[:mid])
    right_nums = merge(nums[mid:])

    return merge_two_list(left_nums, right_nums)

l = [6, 3, 9, 1, 8, 0, 7]

print(merge(l))
