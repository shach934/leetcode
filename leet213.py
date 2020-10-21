213. House Robber II

Note: This is an extension of House Robber.

After robbing those houses on that street, the thief has found himself a new place for his thievery so that he will not get too much attention. This time, all houses at this place are arranged in a circle. That means the first house is the neighbor of the last one. Meanwhile, the security system for these houses remain the same as for those in the previous street.

Given a list of non-negative integers representing the amount of money of each house, determine the maximum amount of money you can rob tonight without alerting the police.

class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        # do not  rob the first 
        lastRob, lastNotRob = 0, 0
        for i in range(1,len(nums)-1):
            lastRob, lastNotRob = lastNotRob + nums[i], max(lastNotRob, lastRob)
        firstNotRob = max(lastNotRob + nums[-1], lastRob)
        # rob the first 
        lastRob, lastNotRob = nums[0], nums[0]
        for i in range(2,len(nums)-1):
            lastRob, lastNotRob = lastNotRob + nums[i], max(lastNotRob, lastRob)
        firstRob = max(lastRob, lastNotRob)
        return max(firstNotRob, firstRob)