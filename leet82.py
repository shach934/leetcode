# 82. Remove Duplicates from Sorted List II

# Given a sorted linked list, delete all nodes that have duplicate numbers, 
# leaving only distinct numbers from the original list.

# For example,
# Given 1->2->3->3->4->4->5, return 1->2->5.
# Given 1->1->1->2->3, return 2->3.

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# 一个新的list，每次往里面加一个节点 看看是否这个节点是重复的，如果是 那就剔除他
# 如果不是 那就加入到当前的
# 需要维护两个指针，一个是当前往里加的，一个是前一个节点的，用来踢出节点

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None:
            return None
        rem = rec = ret = ListNode(float('inf'))
        ret.next = head
        head = head.next
        ret = ret.next
        flag = False
        while head:
            if head.val == ret.val:
                flag = True
            else:
                if flag:
                    ret = rec
                    ret.next = head
                    ret = ret.next
                else:
                    ret.next = head
                    ret = ret.next
                    rec = rec.next
                flag = False
            head = head.next
        if flag:
            rec.next = None
        return rem.next
