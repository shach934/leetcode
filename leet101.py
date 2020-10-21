101. Symmetric Tree

Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).

For example, this binary tree [1,2,2,3,4,4,3] is symmetric:

    1
   / \
  2   2
 / \ / \
3  4 4  3
But the following [1,2,2,null,3,null,3] is not:
    1
   / \
  2   2
   \   \
   3    3
Note:
Bonus points if you could solve it both recursively and iteratively.

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root is None:
            return True
        curr, nex = [root], []
        while curr:
            for i in curr:
                if i is not None:
                    nex += [i.left] if i.left else [None]
                    nex += [i.right] if i.right else [None]
            if not self.check(nex):
                return False
            curr = nex[:]
            nex = []
        return True
            
    def check(self, nums):
        if len(nums):
            l, r = 0, len(nums) - 1
            while l<=r:
                if (nums[l] is None and nums[r] is None) or (nums[l] is not None and nums[r] is not None and nums[r].val == nums[l].val):
                    l += 1
                    r -= 1
                else:
                    return False
            return True
        else:
            return True