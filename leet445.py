# 445. Add Two Numbers II

# You are given two non-empty linked lists representing two non-negative integers. 
# The most significant digit comes first and each of their nodes contain a single digit. 
# Add the two numbers and return it as a linked list.

# You may assume the two numbers do not contain any leading zero, except the number 0 itself.

# Follow up:
# What if you cannot modify the input lists? In other words, reversing the lists is not allowed.

# Example:

# Input: (7 -> 2 -> 4 -> 3) + (5 -> 6 -> 4)
# Output: 7 -> 8 -> 0 -> 7

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if l1 is None:
            return l2
        elif l2 is None:
            return l1
        ret, carryOn = ListNode(0), 0
        back = ret
        l1 = self.invertList(l1)
        l2 = self.invertList(l2)
        while l1 is not None or l2 is not None:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
            ret.next = ListNode((v1 + v2 + carryOn) % 10)
            carryOn = (v1 + v2 + carryOn) // 10
            ret = ret.next
        if carryOn:
            ret.next = ListNode(carryOn % 10)
        return self.invertList(back.next)
    
    
    def invertList(self, head):
        if head is None or head.next is None:
            return head
        l, m, r = head, head.next, head.next.next
        l.next = None
        while r:
            m.next = l
            l = m
            m = r
            r = r.next
        m.next = l
        return m