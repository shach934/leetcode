"""
55. Jump Game

Given an array of non-negative integers, you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Determine if you are able to reach the last index.

For example:
A = [2,3,1,1,4], return true.

A = [3,2,1,0,4], return false.
"""

class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if len(nums) == 1:
            return True
        maxJ = 0
        for i in range(len(nums)):
            maxJ = max(maxJ - 1, nums[i])
            if maxJ == 0 and nums[i] == 0 and i < len(nums)-1:
                return False
        return True