# 206. Reverse Linked List

# Reverse a singly linked list.

# click to show more hints.

# Hint:
# A linked list can be reversed either iteratively or recursively. 
# Could you implement both?

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        l, m, r = head, head.next, head.next.next
        l.next = None  # 千万别忘了先把头结点的next置为None，否则第一个节点和第二个节点会形成一个环。
        
        while r:
            m.next = l
            l = m
            m = r
            r = r.next
        m.next = l
        return m
# 递归版本
# 比三指针版本慢很多
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        first, second = head, head.next
        backhead = self.reverseList(second)
        first.next = None
        second.next = first
        return backhead