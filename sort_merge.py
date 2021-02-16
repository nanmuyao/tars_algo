#!/usr/bin/env python
# -*- coding: utf-8 -*-

l = [1, 3, 2, 4, 0]

# def merge_two_list(left, right):
#     list_merged = []
#     i = 0
#     j = 0
#     while i < len(left) and j < len(right):
#         if left[i] < right[j]:
#             list_merged.append(left[i])
#             i+=1
#         else:
#             list_merged.append(right[j])
#             j+=1
#     list_merged.extend(left[i:])
#     list_merged.extend(right[j:])
#     return list_merged
    
# def merge(arr):
#     if len(arr) <= 1:
#         return arr
#     mid = len(arr)//2
#     left = merge(arr[:mid])
#     right = merge(arr[mid:])
#     return merge_two_list(left, right)
    # 

# print(merge(l))

# time n
def sort(left, right):
    i, j = 0, 0
    arr = []
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            arr.append(left[i])
            i+=1
        else:
            arr.append(right[j])
            j+=1
    arr.extend(left[i:])
    arr.extend(right[j:])
    return arr

def merge(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge(arr[:mid])
    right = merge(arr[mid:])
    arr = sort(left, right)
    return arr

print(merge(l))
