# Invert a binary tree.

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if root:
            root.left, root.right= self.invertTree(root.left), self.invertTree(root.right)
            temp = root.left
            root.left = root.right
            root.right = temp
            return root
        else:
            return root

# def invertTree(self, root):
    # if root:
        # root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)
        # return root