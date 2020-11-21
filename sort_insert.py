arr = [2, 1, 7, 9, 5, 8]
print('sort before', arr)

# https://www.runoob.com/python3/python-insertion-sort.html
def sort_insert1(arr):
    length = len(arr)
    for i in range(1, length):
        cursor_value = arr[i]
        j = i - 1
        # 可以参考下动图，排序是真的秒
        while j >= 0 and cursor_value < arr[j]:
            arr[j + 1] = arr[j]
            j-=1
        arr[j + 1] = cursor_value
    return arr


arr = sort_insert1(arr)
print('1 sort after', arr)


# times 2 写法简洁了一些，但是空间复杂度变大了，每一次交换数组
def sort_insert2(arr):
    length = len(arr)
    for i in range(1, length):
        cursor = i
        while i >= 1:
            i-=1
            if arr[cursor] < arr[i]:
                arr[cursor], arr[i] = arr[i], arr[cursor]
                cursor = i
    return arr

arr = sort_insert2(arr)
print('2 sort after', arr)