# 141. Linked List Cycle

# Given a linked list, determine if it has a cycle in it.

# Follow up:
# Can you solve it without using extra space?

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# 快慢两个指针，一个一次移动一步，一个一次移动两步。如果两者能相遇，说明是环，否则则没有环
# 没环的情况下，快的首先到达链表结尾，主要判断快的指针只能移动一步的情况也要跳出

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head or not head.next or not head.next.next: 
            return False
        slow, fast = head, head.next.next
        while fast:
            if slow == fast:
                break
            else:
                slow = slow.next
                fast = fast.next.next if fast.next and fast.next.next else None
        if slow == fast:
            return True
        else:
            return False