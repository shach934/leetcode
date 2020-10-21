# 92. Reverse Linked List II

# Reverse a linked list from position m to n. Do it in-place and in one-pass.

# For example:
# Given 1->2->3->4->5->NULL, m = 2 and n = 4,

# return 1->4->3->2->5->NULL.

# Note:
# Given m, n satisfy the following condition:
# 1 ≤ m ≤ n ≤ length of list.

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# 主要是特殊情况需要考虑，比如起始点是1，结尾点是链表结尾

class Solution(object):
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        if head is None or head.next is None or n == mm :
            return head
        if mm == 1:
            return self.invertListN(head, n)
        else:
            count,it = 2, head
            while count < mm:
                it = it.next
                count += 1
            half = self.invertListN(it.next, n-mm+1)
            it.next = half
        return head

    def invertListN(self, head, n):
        count = 1
        l, m, r = head, head.next, head.next.next
        l.next = None
        while count < n and r:
            m.next = l
            l = m
            m = r
            r = r.next
            count += 1
        if count == n:
            head.next = m
            return l
        elif r is None and count<n:
            m.next = l
            return m