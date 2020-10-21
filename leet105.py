105. Construct Binary Tree from Preorder and Inorder Traversal

Given preorder and inorder traversal of a tree, construct the binary tree.

Note:
You may assume that duplicates do not exist in the tree.


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        if len(preorder) == 0:
            return None
        root = TreeNode(preorder[0])
        idx = inorder.index(preorder[0])
        root.right = self.buildTree(preorder[idx+1:], inorder[idx+1:])
        root.left = self.buildTree(preorder[1:idx+1],inorder[:idx])
        return root


# 尽可能的避免拷贝list的话，每次就传开始和结束的index进去，会快一些。但是不知道怎么搞的。下面的这个就是不好使。。。。

class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        return helper(self, preoder, 0, len(preoder), inorder, 0, len(inorder))
        
    def helper(self, preoder, startP, endP, inorder, startI, endI):
        if endP = startP or endI == startI :
            return None
        root = TreeNode(preoder[startP])
        idx = inorder.index(preoder[startP])
        root.right = self.helper(preoder, idx+1, endP, inorder, idx+1, endI)
        root.left = self.helper(preoder, startP+1, idx, inorder, startI, idx-1)
        return root