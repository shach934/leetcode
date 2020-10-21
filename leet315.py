315. Count of Smaller Numbers After Self

You are given an integer array nums and you have to return a new counts array. The counts array has the property where counts[i] is the number of smaller elements to the right of nums[i].

Example:

Given nums = [5, 2, 6, 1]

To the right of 5 there are 2 smaller elements (2 and 1).
To the right of 2 there is only 1 smaller element (1).
To the right of 6 there is 1 smaller element (1).
To the right of 1 there is 0 smaller element.
Return the array [2, 1, 1, 0].


class TreeNode(object):
    def __init__(self, n, nDup):
        self.val = n
        self.Nleft = 0
        self.dup = nDup
        self.left = None
        self.right = None

class Solution(object):
    def countSmaller(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        count = [0]*len(nums)
        if len(nums)<2:
            return count
        root = TreeNode(nums[-1], 1)
        for i in range(len(nums)-2, -1, -1):
            count[i] = self.insert(root, nums[i])
        return count
    
    def insert(self, root, num):
        it, count = root, 0
        while True:
            if num < it.val:
                if it.left:
                    it.Nleft += 1
                    it = it.left
                else:
                    it.left = TreeNode(num, 1)
                    it.Nleft += 1
                    break
            elif num > it.val:
                count += it.dup + it.Nleft
                if it.right:
                    it = it.right
                else:
                    it.right = TreeNode(num,1)
                    break
            else:
                it.dup += 1
                count += it.Nleft
                break
        return count