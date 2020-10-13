def merge_two_list(left, right):
    l = []
    left_index = 0
    right_index = 0
    while left_index < len(left) and right_index < len(right):
        if left[left_index] <= right[right_index]:
            l.append(left[left_index])
            left_index += 1
        else:
            l.append(right[right_index])
            right_index += 1
    l.extend(left[left_index:])
    l.extend(right[right_index:])
    return l

# def merge_two_list(data_left, data_right):
#     i = 0
#     j = 0
#     list_result = []
#     while i < len(data_left) and j < len(data_right):
#         if data_left[i] <= data_right[j]:
#             list_result.append(data_left[i])
#             i+=1
#         else:
#             list_result.append(data_right[j])
#             j+=1
#     list_result.extend(data_left[i:])
#     list_result.extend(data_right[j:])
#     return list_result



def merge(l):
    if len(l) <= 1:
        return l
    mid = len(l) // 2
    left = merge(l[:mid])
    right = merge(l[mid:])
    return merge_two_list(left, right)

l = [1, 3, 2, 4, 0]
print(merge(l))
