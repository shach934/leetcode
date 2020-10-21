129. Sum Root to Leaf Numbers

Given a binary tree containing digits from 0-9 only, each root-to-leaf path could represent a number.

An example is the root-to-leaf path 1->2->3 which represents the number 123.

Find the total sum of all root-to-leaf numbers.

For example,

    1
   / \
  2   3
The root-to-leaf path 1->2 represents the number 12.
The root-to-leaf path 1->3 represents the number 13.

Return the sum = 12 + 13 = 25.

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# 队列，然后一层一层的往下滚，滚到叶节点的时候输出

class Solution(object):
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0
        queue, ret = [root], 0
        while queue:
            curr = queue.pop()
            if curr.left:
                curr.left.val += curr.val*10
                queue.append(curr.left)
            if curr.right:
                curr.right.val += curr.val*10
                queue.append(curr.right)
            if curr.left is None and curr.right is None:
                ret +=  curr.val
        return ret