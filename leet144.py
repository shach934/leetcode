# 144. Binary Tree Preorder Traversal

# Given a binary tree, return the preorder traversal of its nodes' values.

# For example:
# Given binary tree {1,#,2,3},
   # 1
    # \
     # 2
    # /
   # 3
# return [1,2,3].

# Note: Recursive solution is trivial, could you do it iteratively?

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
# 递归版本的实现
        ret = []
        self.xianxu(root,ret)
        return ret
    def xianxu(self, root, ret):
        if root:
            ret.append(root.val)
            self.xianxu(root.left, ret)
            self.xianxu(root.right,ret)
            

 # 非递归版本，每次遇到一个节点先把右节点入栈，然后把值保存到返回里面，再去左指数
 
        ret,mystack = [], []
        while root or len(mystack):
            while root:
                ret.append(root.val)
                mystack.append(root.right)
                root = root.left
            root = mystack.pop()
        return ret