# 143. Reorder List

# Given a singly linked list L: L0?L1?…?Ln-1?Ln,
# reorder it to: L0?Ln?L1?Ln-1?L2?Ln-2?…

# You must do this in-place without altering the nodes' values.

# For example,
# Given {1,2,3,4}, reorder it to {1,4,2,3}.

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# use two pointers to partition the list to two lists. 
# invert the second half of the list and insert it to the first list one by one

class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: void Do not return anything, modify head in-place instead.
        """
        backHead = head
        if head is None or head.next is None or head.next.next is None:
            return
        slow, fast = head, head.next.next
        while fast:
            slow = slow.next
            fast = fast.next.next if fast.next and fast.next.next else None
        second = slow.next
        slow.next = None

        second = self.reverseList(second)

        while second:
            curr = second 
            second = second.next
            curr.next = head.next
            head.next = curr
            head = head.next.next
        
    def reverseList(self, head):
        if head is None or head.next is None:
            return head
        l,m,r = head, head.next, head.next.next
        l.next = None
        while r:
            m.next = l
            l = m
            m = r
            r = r.next
        m.next = l
        return m