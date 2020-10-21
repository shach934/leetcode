# 653. Two Sum IV - Input is a BST

# Given a Binary Search Tree and a target number, 
# return true if there exist two elements in the 
# BST such that their sum is equal to the given target.

# Example 1:
# Input: 
    # 5
   # / \
  # 3   6
 # / \   \
# 2   4   7

# Target = 9

# Output: True
# Example 2:
# Input: 
    # 5
   # / \
  # 3   6
 # / \   \
# 2   4   7

# Target = 28

# Output: False

class Solution:
    def findTarget(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: bool
        """

        mydict = {}
        queue = [root]
        while queue:
            mydict[queue[0].val] = 1;
            queue+=filter(None, [queue[0].left, queue[0].right])
            queue.pop(0)
        #print(mydict)
        for keys in mydict:
            if (k - keys != keys) and (k - keys in mydict):
                return True
        return False

class Solution:
    def findTarget(self, root, k):
        if not root: return False
        bfs, s = [root], set()
        for i in bfs:
            if k - i.val in s: return True
            s.add(i.val)
            if i.left: bfs.append(i.left)
            if i.right: bfs.append(i.right)
        return False