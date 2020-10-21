106. Construct Binary Tree from Inorder and Postorder Traversal

Given inorder and postorder traversal of a tree, construct the binary tree.

Note:
You may assume that duplicates do not exist in the tree.

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        if len(inorder) == 0:
            return None
        root = TreeNode(postorder[-1])
        cut = 0
        for i in range(len(inorder)):
            if inorder[i] == postorder[-1]:
                cut = i
                break
        root.left = self.buildTree(inorder[:cut], postorder[:cut])
        root.right = self.buildTree(inorder[cut+1:], postorder[cut:-1])
        return root