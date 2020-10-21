# 86. Partition List

# Given a linked list and a value x, partition it such that all nodes 
# less than x come before nodes greater than or equal to x.

# You should preserve the original relative order of the nodes 
# in each of the two partitions.

# For example,
# Given 1->4->3->2->5->2 and x = 3,
# return 1->2->2->4->3->5.

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        if head is None or head.next is None:
            return head
        less = lessBack = ListNode(0)
        it = head
# 处理掉起始的比x小的节点 直到找到大的，或者直接到尽头，如果到了尽头直接返回
        while it is not None and it.val < x:
            less.next = it
            less = less.next
            it = it.next
        head = it
        if it is None:
            return lessBack.next
        print(it.val)
# 运行到这里，说明当前head不为空且比x大。从下一个开始挑选
        while it.next:
# 判断下一个节点是否小，如果小 一直踢出去，直到结尾或者比当前x大，往后挪一个
# 否则不要往后挪！！！
            if it.next.val < x:
                less.next = it.next
                less = less.next
                it.next = it.next.next
            else:
                it = it.next
        less.next = head
        return lessBack.next
        