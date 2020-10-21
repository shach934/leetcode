# 2. Add Two Numbers
# You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

# You may assume the two numbers do not contain any leading zero, except the number 0 itself.

# Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
# Output: 7 -> 0 -> 8

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
        head, carryOn = ListNode(0), 0
        tail = head
        if l1 and l2:
            while l1 or l2:
                tail.next = ListNode(sum([l1.val if l1 else 0, l2.val if l2 else 0, carryOn])%10)
                tail = tail.next
                carryOn = sum([l1.val if l1 else 0, l2.val if l2 else 0, carryOn])//10
                l1, l2 = l1.next if l1 else None, l2.next if l2 else None
            if carryOn:
                tail.next = ListNode(carryOn)
            return head.next
        elif l1 and not l2:
            return l1
        elif l2 and not l1:
            return l2
        else:
            return None