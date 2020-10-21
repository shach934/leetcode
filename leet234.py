234. Palindrome Linked List

Given a singly linked list, determine if it is a palindrome.

Follow up:
Could you do it in O(n) time and O(1) space?


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if head is None or head.next is None:
            return True
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        head2 = self.reveseList(slow)
        
        while head2:
            if head.val != head2.val:
                return False
            head = head.next
            head2 = head2.next
        return True
        
    def reveseList(self, head):
        if head.next is None:
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