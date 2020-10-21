# 203. Remove Linked List Elements

# Remove all elements from a linked list of integers that have value val.

# Example
# Given: 1 --> 2 --> 6 --> 3 --> 4 --> 5 --> 6, val = 6
# Return: 1 --> 2 --> 3 --> 4 --> 5

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# 关键点，如果起始就是要删掉的

class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        if head is None:
            return None
        while head and head.val == val:
            head = head.next
        if head is None:
            return None
        
        it = head
        while it.next:
            if it.next.val == val:
                it.next = it.next.next
            else:
                it = it.next
        return head