# 61. Rotate List

# Given a list, rotate the list to the right by k places, where k is non-negative.

# For example:
# Given 1->2->3->4->5->NULL and k = 2,
# return 4->5->1->2->3->NULL.

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if not head or not head.next or not k:
            return head
        
        listL, headBackUp = 1, head
        while head.next:
            head = head.next
            listL += 1
        k %= listL
        head.next = headBackUp

        for i in range(listL - k):
            head = head.next
            headBackUp = headBackUp.next
        head.next = None
        return headBackUp