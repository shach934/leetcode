103. Binary Tree Zigzag Level Order Traversal

Given a binary tree, return the zigzag level order traversal of its nodes' values. 
(ie, from left to right, then right to left for the next level and alternate between).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its zigzag level order traversal as:
[
  [3],
  [20,9],
  [15,7]
]

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root is None:
            return []
        curr, nex, path, direct = [root], [], [], -1
        while curr:
            path.append([i.val for i in curr])
            for i in range(len(curr)-1, -1, -1):
                if direct == -1:
                    nex += filter(None, [curr[i].right, curr[i].left])
                else:
                    nex += filter(None, [curr[i].left, curr[i].right])
            curr = nex[:]
            nex = []
            direct = -direct
        return path
                    