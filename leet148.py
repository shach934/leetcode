# 148. Sort List

# Sort a linked list in O(n log n) time using constant space complexity.

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None or head.next is None:
            return head
        lists = []
        while head:
            curr = head
            head = head.next
            curr.next = None
            lists.append(curr)

        while len(lists) > 1:
            if len(lists) % 2:
                lists[-1] += [self.merge2List(lists[2*i], lists[2*i+1]) for i in range(len(lists)/2)]
            else:
                lists = [self.merge2List(lists[2*i], lists[2*i+1]) for i in range(len(lists)/2)]
            print([lists[i].val for i in range(len(lists))])
        return lists[0]
            
            
    def merge2List(self, listA, listB):
        ret = it = ListNode(0)
        while listA and listB:
            if listA.val < listB.val:
                it.next = listA
                it = it.next
                listA = listA.next
            else:
                it.next = listB
                it = it.next
                listB = listB.next
        if listA:
            it.next = listA
        elif listB:
            it.next = listB
        return ret.next