# 268. Missing Number

# Given an array containing n distinct numbers taken from 0, 1, 2, ..., n, 
# find the one that is missing from the array.

# For example,
# Given nums = [0, 1, 3] return 2.

# Note:
# Your algorithm should run in linear runtime complexity. 
# Could you implement it using only constant extra space complexity?

#等差数列！直接算出总数和，然后减去当前数列的和。

n = len(nums)
return n*(n+1)/2 - sum(nums)

class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        mydict = {}
        for i in range(len(nums) + 1):
            mydict.setdefault(i, 0)
        for i in nums:
            del mydict[i]
        return mydict.keys()[0]