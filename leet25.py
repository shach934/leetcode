25. Reverse Nodes in k-Group

Given a linked list, reverse the nodes of a linked list k at a time and return its modified list.

k is a positive integer and is less than or equal to the length of the linked list. If the number of nodes is not a multiple of k then left-out nodes in the end should remain as it is.

You may not alter the values in the nodes, only nodes itself may be changed.

Only constant memory is allowed.

For example,
Given this linked list: 1->2->3->4->5

For k = 2, you should return: 2->1->4->3->5

For k = 3, you should return: 3->2->1->4->5



class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if head is None or head.next is None or k == 1:
            return head
        dummy = ListNode(0)
        tailAhead = dummy
        tailAhead.next = None
        tail = head
        while tail:
            count = 0
            while tail and count < k:
                count += 1
                if count == k:
                    break
                tail = tail.next
            if count == k:
                headAfter = tail.next
                tail.next = None
                head, tail = self.reversList(head, tail)
                tailAhead.next = head
                tailAhead = tail
                head = headAfter
                tail = head
            else:
                break
        tailAhead.next = head
        return dummy.next
            
        
    def reversList(self, head, tail):
        if head is None or head.next is None:
            return head, tail
        l, m, r = head, head.next, head.next.next
        l.next = None
        while r:
            m.next = l
            l = m
            m = r
            r = r.next
        m.next = l
        return m, head