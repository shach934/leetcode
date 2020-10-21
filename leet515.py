# 515. Find Largest Value in Each Tree Row

# You need to find the largest value in each row of a binary tree.

# Example:
# Input: 

          # 1
         # / \
        # 3   2
       # / \   \  
      # 5   3   9 

# Output: [1, 3, 9]

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def largestValues(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        ret = []
        qnow, qnext, mylist = [root],[], []
        if not root:
            return ret
        while qnow:
            for i in qnow:
                mylist.append(i.val)
                qnext += filter(None, [i.left, i.right])
            ret.append(max(mylist))
            qnow = qnext[:]
            del mylist[:]
            del qnext[:]
        return ret
# 其实可以不用两个list，更新now和next的，用一行的循环，可以直接更新now
# 然后max可以直接用一个一行循环解决问题