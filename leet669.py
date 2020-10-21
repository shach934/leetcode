669. Trim a Binary Search Tree

Given a binary search tree and the lowest and highest boundaries as L and R, trim the tree so that all its elements lies in [L, R] (R >= L). 
You might need to change the root of the tree, so the result should return the new root of the trimmed binary search tree.

Example 1:
Input: 
    1
   / \
  0   2

  L = 1
  R = 2

Output: 
    1
      \
       2
Example 2:
Input: 
    3
   / \
  0   4
   \
    2
   /
  1

  L = 1
  R = 3

Output: 
      3
     / 
   2   
  /
 1
 
 # Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def trimBST(self, root, L, R):
        """
        :type root: TreeNode
        :type L: int
        :type R: int
        :rtype: TreeNode
        """
        dummy = TreeNode(0)     
        dummy.left = self.trim(root, L, R)
        return dummy.left
        
# 每次删除一个，结果能够生成一个二叉树，但是和expeect的不一样，所以判错，
# 因为标准的，或者说更聪明的做法是：每次看到一个值过大或者过小的时候，
# 可以抛弃掉一棵子树，不用每次一个个删除，而是应该一棵树一棵树的删除

    def trim(self, root, L, R)
        if root.val < L or root.val > R:
            while root.val < L or root.val > R:
                if root.left is None and root.right is None:
                    return None
                if root.left is None:
                    root = root.right
                if root.right is None:
                    root =  root.left
                if curr.right.left:
                    curr =  root.right
                    while curr.left.left:
                        curr = curr.left
                    temp = curr
                    curr = curr.left
                    temp.left = curr.right
                    curr.left = root.left
                    curr.right = root.right
                    root =  curr
                else:
                    root.right.left = root.left
                    root =  root.right
            return root
        root.left = self.trim(root.left, L, R)
        root.right = self.trim(root.right, L, R)
        
# 不会出现剔除一个，然后提上来一个还是不行的这种情况，因为是有序的，是通过剔除树来实现的，而不是通过一个一个节点的删除实现的！！！！

    def trim2(self, root, L, R)
        if L > root.val:
            return self.trim2 (root.right, L, R)
        if R < root.val:
            return self.trim2(root.left, L, R)
        root.left = self.trim2(root.left, L, R)
        root.right = self.trim2(root.right, L, R)
        return root
            
            