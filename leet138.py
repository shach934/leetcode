138. Copy List with Random Pointer

A linked list is given such that each node contains an additional random pointer which could point to any node in the list or null.

Return a deep copy of the list.

# Definition for singly-linked list with a random pointer.
# class RandomListNode(object):
#     def __init__(self, x):
#         self.label = x
#         self.next = None
#         self.random = None

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: RandomListNode
        :rtype: RandomListNode
        """
        if head is None:
            return None
        it = head
        while it:
            newNode = RandomListNode(it.label)
            newNode.next, newNode.random = it.next, it.random
            it.next = newNode
            it = newNode.next
        it = head.next
        while it.next:
            if it.random:
                it.random = it.random.next
            it = it.next.next
        if it.random:
            it.random = it.random.next
        it, newHead, ret = head, head.next, head.next
        while it:
            it.next = newHead.next
            it = it.next
            if it:
                newHead.next = it.next
                newHead = newHead.next
        return ret