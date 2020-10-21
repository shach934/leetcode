# 94. Binary Tree Inorder Traversal

# Given a binary tree, return the inorder traversal of its nodes' values.

# For example:
# Given binary tree [1,null,2,3],
   # 1
    # \
     # 2
    # /
   # 3
# return [1,3,2].

# Note: Recursive solution is trivial, could you do it iteratively?

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# 递归版本的 中序遍历
class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        
        ret = []     
        self.middleHelper(root, ret)
        return ret
    
    def middleHelper(self, root, ret):
        if root is not None:
            self.middleHelper(root.left, ret)
            ret.append(root.val)
            self.middleHelper(root.right, ret)
            
# 中序遍历非递归版本，每次拿到一个节点 首先往左走到底，然后路过的节点放到栈里面
# 到达最左的节点之后，弹栈，保存值，然后去右节点
class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        mystack, ret = [],[]
        while root or len(mystack):
            while root:
                mystack.append(root)
                root = root.left
            ret.append(mystack[-1].val)
            root = mystack[-1].right
            mystack.pop()
        return ret