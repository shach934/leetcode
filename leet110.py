110. Balanced Binary Tree

Given a binary tree, determine if it is height-balanced.

For this problem, a height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees of every node never differ by more than 1.

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root is None:
            return True
        flag = [True]
        self.balanced(root, flag)
        return flag[0]
    
    def balanced(self, root, flag):
        if root is None:
            return 0
        heightL = self.balanced(root.left, flag)
        heightR = self.balanced(root.right,flag)
        if flag[0]:
            if (heightL - heightR)**2 > 1:
                flag[0] = False
            else:
                return max(heightL, heightR) + 1
        
        