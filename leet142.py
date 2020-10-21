# 142. Linked List Cycle II

# Given a linked list, return the node where the cycle begins. If there is no cycle, return null.

# Note: Do not modify the linked list.

# Follow up:
# Can you solve it without using extra space?


# 如何判断环的入口点：碰撞点p到连接点的距离 = 头指针到连接点的距离，因此，分别从碰撞点、头指针开始走，相遇的那个点就是连接点。

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        
        if not head or not head.next or not head.next.next: 
            return None
        slow, fast = head, head.next.next
        while fast:
            if slow == fast:
                break
            else:
                slow = slow.next
                fast = fast.next.next if fast.next and fast.next.next else None
        if slow == fast:
            slow = slow.next.next # 就是这一步，因为fast和slow他俩不是同时从头结点出发的，所以碰撞点其实也改变了，要把碰撞点也改掉
            while slow != head:
                slow = slow.next
                head = head.next
            return head
        else:
            return None