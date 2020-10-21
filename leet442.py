# 442. Find All Duplicates in an Array

# Given an array of integers, 1 ≤ a[i] ≤ n (n = size of array), 
# some elements appear twice and others appear once.

# Find all the elements that appear twice in this array.

# Could you do it without extra space and in O(n) runtime?

# Example:
# Input:
# [4,3,2,7,8,2,3,1]

# Output:
# [2,3]


class Solution(object):
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ret = []
        for i in nums:
            idx = abs(i) - 1
            if nums[idx]<0:
                ret.append(idx + 1)
            nums[idx] = - abs(nums[idx])
        return ret