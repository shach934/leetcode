# 21. Merge Two Sorted Lists

# Merge two sorted linked lists and return it as a new list. 
# The new list should be made by splicing together the nodes of the first two lists.

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None



class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if l1 is None:
            return l2
        elif l2 is None:
            return l1
        ret = ListNode(0)
        head = ret
        while l1 is not None and l2 is not None:
            if l1.val < l2.val:
                ret.next = l1
                ret = ret.next 
                l1 = l1.next
                
            else:
                ret.next = l2
                ret = ret.next
                l2 = l2.next
        if l1:
            ret.next = l1
        elif l2:
            ret.next = l2
        return head.next