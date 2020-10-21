# 19. Remove Nth Node From End of List

# Given a linked list, remove the nth node from the end of list and return its head.

# For example,

   # Given linked list: 1->2->3->4->5, and n = 2.

   # After removing the second node from the end, the linked list becomes 1->2->3->5.
# Note:
# Given n will always be valid.
# Try to do this in one pass.

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# 关键点还是特殊情况，比如最后一个节点，头结点，只有一个节点的时候

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        if head.next is None:
            return None
        if n == 1:
            it = head
            while it.next.next:
                it = it.next
            it.next = None
            return head
        first, second = head, head
        for i in range(n):
            first = first.next
        if first is None:
            return head.next
        while first.next:
            first = first.next
            second = second.next
        print(first.val)
        print(second.val)
        second.next = second.next.next
        return head
