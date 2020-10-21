114. Flatten Binary Tree to Linked List

Given a binary tree, flatten it to a linked list in-place.

For example,
Given

         1
        / \
       2   5
      / \   \
     3   4   6
The flattened tree should look like:
   1
    \
     2
      \
       3
        \
         4
          \
           5
            \
             6
             
class Solution(object):
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        if root is None:
            return None
        dummy = TreeNode(0)
        tail = dummy
        stack = []
        while stack or root:
            while root:
                tail.left = None
                tail.right = root
                tail = tail.right
                stack.append(root.right)
                root = root.left
            root = stack.pop()
        root = dummy.right