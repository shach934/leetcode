538. Convert BST to Greater Tree

Given a Binary Search Tree (BST), convert it to a Greater Tree such that every key of the original 
BST is changed to the original key plus sum of all keys greater than the original key in BST.

Example:

Input: The root of a Binary Search Tree like this:
              5
            /   \
           2   13

Output: The root of a Greater Tree like this:
             18
            /   \
          20   13
          
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def convertBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        mystack, accum, back = [], 0, root
        while root or len(mystack):
            while root:
                mystack.append(root)
                root = root.right
            mystack[-1].val += accum
            accum = mystack[-1].val
            root = mystack[-1].left
            mystack.pop()
        return back