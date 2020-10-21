102. Binary Tree Level Order Traversal

Given a binary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its level order traversal as:
[
  [3],
  [9,20],
  [15,7]
]

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root is None:
            return []
        retList, currList,  = [],[root]
        while currList:
            vals, nextList = [], []
            for i in currList:
                if i.left:
                    nextList.append(i.left)
                if i.right:
                    nextList.append(i.right)
                vals.append(i.val)
            currList = nextList[:]
            del nextList
            retList.append(vals)
        return retList