# 83. Remove Duplicates from Sorted List

# Given a sorted linked list, delete all duplicates such that each element 
# appear only once.

# For example,
# Given 1->1->2, return 1->2.
# Given 1->1->2->3->3, return 1->2->3.

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

        if not head or not head.next:
            return head
        curr,flag, start = head.val, False, head
        backHead = head
        while head:
            if head.val == curr :
                flag = True
            elif head.val != curr and not flag:
                start = head
                flag = False
                curr = head.val
            elif head.val != curr and flag:
                start.next = head
                start = head
                curr = head.val
                flag = False
            head = head.next
        if flag:
            start.next = None
        return backHead
# 关键点在于判断什么时候是需要桥接 需要根据上一步的状态和当前步的状态来决定动作。
# 最后一个不要忘记单独处理，否则循环跳出的时候 还没有处理掉最后一个重复数字