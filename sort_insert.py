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


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# https://leetcode-cn.com/problems/insertion-sort-list/
# 147. 对链表进行插入排序
class Solution(object):
    def insertionSortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dummy = ListNode(float('-inf'))
        cur = head
        pre = dummy
        while cur:
            tmp = cur.next
            while pre.next and pre.next.val < cur.val:
                pre = pre.next
            cur.next = pre.next
            pre.next = cur
            cur = tmp
            pre = dummy
        return dummy.next
        