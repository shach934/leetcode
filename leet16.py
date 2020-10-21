"""
16. 3Sum Closest

Given an array S of n integers, find three integers in S such that the sum is closest to a given number, target. Return the sum of the three integers. You may assume that each input would have exactly one solution.

    For example, given array S = {-1 2 1 -4}, and target = 1.

    The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
"""

class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if len(nums) < 4:
            return sum(nums)
        nums.sort()
        
        clean, count =[nums[0]], 1 
        for i in range(1, len(nums)):
            if nums[i] == clean[-1]:
                count += 1
            else:
                count = 0
            if count < 4:
                clean.append(nums[i])
        nums = clean[:]
        
        ans = sum(nums[:3])
        for mid in range(1, len(nums)-1):
            l, r = 0, len(nums) - 1
            while l < mid and r > mid:
                candi = nums[mid] + nums[l] + nums[r]
                if abs(candi - target) < abs(ans - target):
                    ans = candi
                if candi > target : 
                    r -= 1
                elif candi < target: 
                    l += 1
                else:
                    return target
        return ans