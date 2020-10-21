98. Validate Binary Search Tree

Given a binary tree, determine if it is a valid binary search tree (BST).

Assume a BST is defined as follows:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.
Example 1:
    2
   / \
  1   3
Binary tree [2,1,3], return true.
Example 2:
    1
   / \
  2   3
Binary tree [1,2,3], return false.

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# 并不能根据一层的信息判断是否为有效的BST，必须要保证所有的左子树和右子树
# 递归的去找每个子树的最大值和最小值。保证节点左面的最大值也比节点值小，节点右边的最小值也比节点值大即为有效的BST

# 基本可以用后续遍历的思路去解，先去遍历左子树，然后记录最大值和最小值，然后到右子树去遍历，返回一个最大值和最小值。
# 检查一下是否符合BST的规定，如果符合，那么就返回到上一层去考虑一下当前值

# 最简单的，中序遍历，看看是否有不是升序的情况存在

class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        mystack, inorder = [], []
        while mystack or root:
            while root:
                mystack.append(root)
                root = root.left
            root = mystack.pop()
            inorder.append(root.val)
            root = root.right
        for i in range(len(inorder)-1):
            if inorder[i] >= inorder[i+1]:
                return False
        return True