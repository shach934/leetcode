# 24. Swap Nodes in Pairs

# Given a linked list, swap every two adjacent nodes and return its head.

# For example,
# Given 1->2->3->4, you should return the list as 2->1->4->3.

# Your algorithm should use only constant space. You may not modify the values in the list, 
# only nodes itself can be changed.

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# 第一个和第二个要手动翻转，然后从后面用三个指针翻转
# 

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None or head.next is None:
            return head
        newH = head.next
        head.next = newH.next
        newH.next = head
        if head.next is None:
            return newH
        l,m,r, = head, head.next, head.next.next
        
        while r:
            l.next = r
            m.next = r.next
            r.next = m
            l = m
            m = m.next
            r = m.next if m else None
        return newH