#!/usr/bin/env python
# -*- coding: utf-8 -*-

def merge_two_list(data_left, data_right):
    i = 0
    j = 0
    list_result = []
    while i < len(data_left) and j < len(data_right):
        if data_left[i] <= data_right[j]:
            list_result.append(data_left[i])
            i+=1
        else:
            list_result.append(data_right[j])
            j+=1
    list_result.extend(data_left[i:])
    list_result.extend(data_right[j:])
    return list_result


def merge(data_list):
    length = len(data_list)
    if length <= 1:
	return data_list

    m = length // 2

    data_left = merge(data_list[:m])
    data_right = merge(data_list[m:])

    return merge_two_list(data_left, data_right)

l = [1, 3, 2, 4, 0]
print merge(l)
