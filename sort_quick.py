arr = [2, 1, 7, 9, 5, 8]
print('sort before', arr)


def quick_sort(arr):
    if len(arr) < 2:
        return arr
    pivot = arr.pop()
    lesser = []
    greater = []
    for i in arr:
        (lesser if i < pivot else greater).append(i)
    return quick_sort(lesser) + [pivot] + quick_sort(greater)

print(quick_sort(arr))
