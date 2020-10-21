# 513. Find Bottom Left Tree Value

# Given a binary tree, find the leftmost value in the last row of the tree.

# Example 1:
# Input:

    # 2
   # / \
  # 1   3

# Output:
# 1
# Example 2: 
# Input:

        # 1
       # / \
      # 2   3
     # /   / \
    # 4   5   6
       # /
      # 7

# Output:
# 7

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findBottomLeftValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        qnow, qnext,left = [root],[],root.val
        while qnow:
            for i in qnow:
                if i.left:
                    qnext.append(i.left)
                if i.right:
                    qnext.append(i.right)
            if qnext:
                left = qnext[0].val
            qnow = qnext[:] # 因为后面要删除qnext，所以这儿必须不能直接用等于号复制，相当于是指针复制。
            del qnext[:]
        return left


# second version

class Solution(object):
    def findBottomLeftValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        qnow, qnext,left = [root],[],root.val
        while qnow:
            for i in qnow:
                qnext += fiter(None, i.left,i.right)
            if qnext:
                left = qnext[0].val
            qnow = qnext[:] # 因为后面要删除qnext，所以这儿必须不能直接用等于号复制，相当于是指针复制。
            del qnext[:]
        return left