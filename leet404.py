# 404. Sum of Left Leaves

# Find the sum of all left leaves in a given binary tree.

# Example:

    # 3
   # / \
  # 9  20
    # /  \
   # 15   7

# There are two left leaves in the binary tree, 
# with values 9 and 15 respectively. Return 24.

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        accum = 0
        if (not root) or (not root.left and not root.right):
            return 0
        lb = [root]
        while lb:
            if lb[0].left:
                if not lb[0].left.left and not lb[0].left.right:
                    accum += lb[0].left.val
                else:
                    lb += [lb[0].left]
            lb += filter(None, [lb[0].right])
            lb.pop(0)
        return accum