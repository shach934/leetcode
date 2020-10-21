257. Binary Tree Paths

Given a binary tree, return all root-to-leaf paths.

For example, given the following binary tree:

   1
 /   \
2     3
 \
  5
All root-to-leaf paths are:

["1->2->5", "1->3"]

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# 智商不够。。。怎么都折腾不明白这个list的问题了
# 用discussion里面看到的别人的答案仿着写一个吧 唉。。。。。

class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        
        ret = []
        ret = self.helper(root, ret)
        print(ret)
        
    def helper(self, root, ret):
        if root.left is None and root.right is None:
            return [[root.val]]
        if root.left and root.right is None:
            ret = [i.append(root.val) for i in self.helper(root.left, ret)]
        elif root.right and root.left is None:
            ret = [i.append(root.val) for i in self.helper(root.right, ret)]
        else:
            ret = [ret + [root.val] + self.helper(root.left, ret), ret + [root.val] + self.helper(root.right, ret)]
        return ret

# 照着discuss里面看到的别人的解决方案写的
# 这个效率比较高，因为只是往下滚，没有回来的路程，到底就结束了，不像我的想法还得回来把路过的累积起来
class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        
        ret = []
        if root is None:
            return []
        self.helper(root, '', ret)
        return ret
        
    def helper(self, root, ls, ret):
        if root.left is None and root.right is None:
            ret.append(ls + str(root.val))
            print(ret)
        if root.left:
            self.helper(root.left, ls + str(root.val) + '->' , ret)
        if root.right:
            self.helper(root.right, ls + str(root.val)+ '->' , ret)