# 147. Insertion Sort List

# Sort a linked list using insertion sort.

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# 还是两个比较特殊的边界需要考虑 
# 开始要加入一个节点，最大的要插入尾部的节点也需要特殊处理

# 整理思路再写

class Solution(object):
    def insertionSortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None:
            return head
        ret = ListNode('inf')
        ret.next = head
        head = head.next
        ret.next.next = None
        while head:
            it = ret
            curr = head
            head = head.next
            curr.next = None
            while it.next:
                if it.next.val > curr.val:
                    curr.next = it.next
                    it.next = curr
                    break
                it = it.next
            if it.next is None:
                it.next = curr
        return ret.next
            