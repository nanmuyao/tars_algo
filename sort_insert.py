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

##########################################差距在这里
"""
A pure Python implementation of the insertion sort algorithm
This algorithm sorts a collection by comparing adjacent elements.
When it finds that order is not respected, it moves the element compared
backward until the order is correct.  It then goes back directly to the
element's initial position resuming forward comparison.
For doctests run following command:
python3 -m doctest -v insertion_sort.py
For manual testing run:
python3 insertion_sort.py
"""


def insertion_sort(collection: list) -> list:
    """A pure Python implementation of the insertion sort algorithm
    :param collection: some mutable ordered collection with heterogeneous
    comparable items inside
    :return: the same collection ordered by ascending
    Examples:
    >>> insertion_sort([0, 5, 3, 2, 2])
    [0, 2, 2, 3, 5]
    >>> insertion_sort([]) == sorted([])
    True
    >>> insertion_sort([-2, -5, -45]) == sorted([-2, -5, -45])
    True
    >>> insertion_sort(['d', 'a', 'b', 'e', 'c']) == sorted(['d', 'a', 'b', 'e', 'c'])
    True
    >>> import random
    >>> collection = random.sample(range(-50, 50), 100)
    >>> insertion_sort(collection) == sorted(collection)
    True
    >>> import string
    >>> collection = random.choices(string.ascii_letters + string.digits, k=100)
    >>> insertion_sort(collection) == sorted(collection)
    True
    """

    for insert_index, insert_value in enumerate(collection[1:]):
        temp_index = insert_index
        while insert_index >= 0 and insert_value < collection[insert_index]:
            collection[insert_index + 1] = collection[insert_index]
            insert_index -= 1
        if insert_index != temp_index:
            collection[insert_index + 1] = insert_value
    return collection


if __name__ == "__main__":
    from doctest import testmod

    testmod()

    user_input = input("Enter numbers separated by a comma:\n").strip()
    unsorted = [int(item) for item in user_input.split(",")]
    print(f"{insertion_sort(unsorted) = }")
