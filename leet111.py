111. Minimum Depth of Binary Tree

Given a binary tree, find its minimum depth.

The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
# 层续遍历，碰到叶节点退出
class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0
        dept = 0
        curr, nex = [root], []
        while len(curr):
            dept += 1
            for i in curr:
                if i.left is None and i.right is None:
                    return dept
                nex += filter(None, [i.left, i.right])
            curr = nex[:]
            nex = []