671. Second Minimum Node In a Binary Tree

Given a non-empty special binary tree consisting of nodes with the non-negative value, where each node 
in this tree has exactly two or zero sub-node. If the node has two sub-nodes, then this node's value is 
the smaller value among its two sub-nodes.

Given such a binary tree, you need to output the second minimum value 
in the set made of all the nodes' value in the whole tree.

If no such second minimum value exists, output -1 instead.

Example 1:
Input: 
    2
   / \
  2   5
     / \
    5   7

Output: 5
Explanation: The smallest value is 2, the second smallest value is 5.
Example 2:
Input: 
    2
   / \
  2   2

Output: -1
Explanation: The smallest value is 2, but there isn't any second smallest value.


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findSecondMinimumValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        ret,base = [-1], root.val
        self.helper(root, ret, base)
        return ret[0]
    
    def helper(self, root, ret, base):
        if root.left:
            a = max(root.left.val, root.right.val)
            if a > base:
                if ret[0] == -1:
                    ret[0] = a
                elif a < ret[0]:
                    ret[0] = a 
            self.helper(root.left, ret, base)
            self.helper(root.right, ret, base)         