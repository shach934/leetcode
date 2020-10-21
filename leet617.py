# 617. Merge Two Binary Trees

# Given two binary trees and imagine that when you put one of them to cover the other, some nodes of the two trees are overlapped while the others are not.

# You need to merge them into a new binary tree. The merge rule is that if two nodes overlap, then sum node values up as the new value of the merged node. Otherwise, the NOT null node will be used as the node of new tree.

# Example 1:

# Input: 
	# Tree 1                     Tree 2                  
          # 1                         2                             
         # / \                       / \                            
        # 3   2                     1   3                        
       # /                           \   \                      
      # 5                             4   7                  
# Output: 
# Merged tree:
	     # 3
	    # / \
	   # 4   5
	  # / \   \ 
	 # 5   4   7
	 
# Note: The merging process must start from the root nodes of both trees.

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# first version
class Solution(object):
    def mergeTrees(self, t1, t2):
        """
        :type t1: TreeNode
        :type t2: TreeNode
        :rtype: TreeNode
        """
        if t1 and t2:
            root = TreeNode(t1.val + t2.val)
            root.left = self.mergeTrees(t1.left, t2.left)
            root.right = self.mergeTrees(t1.right, t2.right)
            return root
        elif t1 and not t2:
            root = TreeNode(t1.val)
            root.left = self.mergeTrees(t1.left, None)
            root.right = self.mergeTrees(t1.right, None)
            return root
        elif not t1 and t2:
            root = TreeNode(t2.val)
            root.left = self.mergeTrees(t2.left, None)
            root.right = self.mergeTrees(t2.right, None)
            return root
        else :
            return None

# second version

class Solution(object):
    def mergeTrees(self, t1, t2):
        """
        :type t1: TreeNode
        :type t2: TreeNode
        :rtype: TreeNode
        """
        if t1 or t2:
            root = TreeNode((t1.val if t1 else 0) + (t2.val if t2 else 0))
            root.left = self.mergeTrees(t1 and t1.left, t2 and t2.left )
            root.right = self.mergeTrees(t1 and t1.right, t2 and t2.right)
            return root
        else :
            return None