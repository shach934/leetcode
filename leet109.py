109. Convert Sorted List to Binary Search Tree

Given a singly linked list where elements are sorted in ascending order, convert it to a height balanced BST.

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        mylist = []
        while head:
            mylist.append(head.val)
            head = head.next
        return self.sortedArrayToBST(mylist)
        
    def sortedArrayToBST(self, nums):
        if len(nums) == 0:
            return None
        root = TreeNode(nums[len(nums)/2])
        root.right = self.sortedArrayToBST(nums[len(nums)/2 + 1:])
        root.left = self.sortedArrayToBST(nums[:len(nums)/2])
        return root