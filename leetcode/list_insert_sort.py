
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
        