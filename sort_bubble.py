
def sort_bubble(arr):
    length = len(arr)
    for i in range(length):
        for j in range(length - i - 1):
            if arr[j] < arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

arr = [2, 1, 7, 9, 5, 8]
print('sort before', arr)
arr = sort_bubble(arr)
print('sort after', arr)

