# 23. Merge k Sorted Lists

# Merge k sorted linked lists and return it as one sorted list. 
# Analyze and describe its complexity.

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# 先提前先把所有的空的链表剔除掉 然后再两两merge出来就好了

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        for i in range(len(lists)-1,-1, -1):
            if lists[i] is None:
                lists.pop(i)
        if len(lists) == 0:
            return lists
        while len(lists) > 1:
            newlist = [self.merge2Lists(lists[2*i], lists[2*i+1]) for i in range(len(lists)/2)]
            if len(lists) % 2 != 0:
                newlist.append(lists[-1])
            lists = newlist[:]
        return lists[0]
    
    def merge2Lists(self,listA, listB):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        : merge two sorted lists and return a sorted list Node
        """
        ret = order = ListNode(0)
        while listA and listB:
            if listA.val < listB.val:
                order.next = listA
                listA = listA.next
            else:
                order.next = listB
                listB = listB.next
            order = order.next
        if listA:
            order.next = listA
        else:
            order.next = listB
        return ret.next