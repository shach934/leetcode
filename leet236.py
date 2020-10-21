236. Lowest Common Ancestor of a Binary Tree

Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.

According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between 
two nodes v and w as the lowest node in T that has both v and w as descendants (where we 
allow a node to be a descendant of itself).”

        _______3______
       /              \
    ___5__          ___1__
   /      \        /      \
   6      _2       0       8
         /  \
         7   4
For example, the lowest common ancestor (LCA) of nodes 5 and 1 is 3. Another example is LCA of 
nodes 5 and 4 is 5, since a node can be a descendant of itself according to the LCA definition.

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        path1, path2 = [], []
        self.findPath(root, p, [], path1)
        self.findPath(root, q, [], path2)
        common = path1[0]
        l = min(len(path1), len(path2))
        for i in range(l):
            if path1[i] == path2[i]:
                common = path1[i]
            else:
                break
        return common.val
    def findPath(self, root, node, route, path):
        if root == node:
            path += route + [root]
        else:
            if root.left:
                self.findPath(root.left, node, route + [root], path)
            if root.right:
                self.findPath(root.right, node, route + [root], path)