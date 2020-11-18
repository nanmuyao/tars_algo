# https://www.runoob.com/python3/python-insertion-sort.html
def sort_insert(arr):
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

arr = [2, 1, 7, 9, 5, 8]
print('sort before', arr)
arr = sort_insert(arr)
print('sort after', arr)

