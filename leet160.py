# 160. Intersection of Two Linked Lists

# Write a program to find the node at which the intersection of two singly 
# linked lists begins.


# For example, the following two linked lists:

# A:          a1 → a2
                   # ↘
                     # c1 → c2 → c3
                   # ↗            
# B:     b1 → b2 → b3
# begin to intersect at node c1.


# Notes:

# If the two linked lists have no intersection at all, return null.
# The linked lists must retain their original structure after the function returns.
# You may assume there are no cycles anywhere in the entire linked structure.
# Your code should preferably run in O(n) time and use only O(1) memory.\


# 先把一个链表给弄成环，然后从来从另外一个进去，判断是否有环，如果有环说明两者相交
# 如果没环的话，说明两个链表没有相交

# 注意的情况 只有一个节点的链表，需要单独考虑

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        if not headA or not headB:
            return None
        elif not headA.next:
            backB = headB
            while backB:
                if backB == headA:
                    return headA
                backB = backB.next
            return None
        elif not headB.next:
            backA = headA
            while backA:
                if backA == headB:
                    return headB
                backA = backA.next
            return None
        
        backA = headA
        while headA.next:
            headA = headA.next
        headA.next = backA
        slow=fast = headB
        intersect = False
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                intersect = True
                break
        if intersect:
            backB = headB
            while backB:
                if backB == slow:
                    headA.next = None
                    return slow
                else:
                    backB = backB.next
                    slow = slow.next
        else:
            headA.next = None
            return None