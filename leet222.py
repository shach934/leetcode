222. Count Complete Tree Nodes

Given a complete binary tree, count the number of nodes.

Definition of a complete binary tree from Wikipedia:
In a complete binary tree every level, except possibly the last, is completely filled, 
and all nodes in the last level are as far left as possible. It can have between 1 and 2h nodes inclusive at the last level h.

简单直接的方法就是直接遍历树，复杂度也就是O(n)， 线性无法通过，超时了


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        mylist = []
        self.inorderHelper(root, mylist)
        return len(mylist)
        
        
    def inorderHelper(self, root, mylist):
        if root:
            self.inorderHelper(root, mylist)
            mylist.append(root.val)
            self.inorderHelper(root, mylist)
            

log（n）的解法，每次拿到一个节点，去其左右子树查看其最左边的深度。
如果两边的深度一致，说明左子树是满树，那就用其深度可以直接计算出来里面的节点数目，然后递归去右子树
如果两遍的深度不一致，说明右子树全部都少了最底下一层，也可以直接计算出来里面的节点数目，然后就递归去左子树

相当于是每次检查一个节点，就扔掉了一半的元素不用再检查了，是log的算法

class Solution(object):
    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        num = [0]
        self.countNode(root, num)
        return num[0]
        
    def countNode(self, root, num):
        if root is None:
            return 0
        leftD = self.depth(root.left)
        rightD = self.depth(root.right)
        if leftD == rightD:
            num[0] += pow(2, leftD)   # 这里面没用2^n -1 这个公式，因为还要把根节点加进去。否则就少算了一个
            self.countNode(root.right, num)
        else:
            num[0] += pow(2, rightD)
            self.countNode(root.left, num)
        
    def depth(self, root):
        count = 0
        while root:
            count += 1
            root = root.left
        return count