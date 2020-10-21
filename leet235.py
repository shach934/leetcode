235. Lowest Common Ancestor of a Binary Search Tree

Given a binary search tree (BST), find the lowest common ancestor (LCA) of two given nodes in the BST.

According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two 
nodes v and w as the lowest node in T that has both v and w as descendants (where we allow a node to be a descendant of itself).”

        _______6______
       /              \
    ___2__          ___8__
   /      \        /      \
   0      _4       7       9
         /  \
         3   5
For example, the lowest common ancestor (LCA) of nodes 2 and 8 is 6. Another example is LCA 
of nodes 2 and 4 is 2, since a node can be a descendant of itself according to the LCA definition.



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
        print(path1)
        print(path2)
        l = min(len(path1), len(path2))
        common = path1[0]
        for i in range(l):
            if path1[i] == path2[i]:
                common = path1[i]
            else:
                break
        return common
        
        
    def findPath(self, root, node, route, path):
        if root is not None:
            if root == node:
                path += route + [root.val]
            else:
                if root.val > node.val:
                    self.findPath(root.left, node, route + [root.val], path)
                elif root.val < node.val:
                    self.findPath(root.right, node, route + [root.val], path)
            