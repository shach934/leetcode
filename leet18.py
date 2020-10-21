"""
18. 4Sum

Given an array S of n integers, are there elements a, b, c, and d in S such that a + b + c + d = target? Find all unique quadruplets in the array which gives the sum of target.

Note: The solution set must not contain duplicate quadruplets.

For example, given array S = [1, 0, -1, 0, -2, 2], and target = 0.

A solution set is:
[
  [-1,  0, 0, 1],
  [-2, -1, 1, 2],
  [-2,  0, 0, 2]
]
"""

class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        if len(nums) < 4:
            return []
        nums.sort()
        clean, count = [nums[0]], 1
        for i in range(1, len(nums)):
            if nums[i] == clean[-1]:
                count += 1
            else:
                count = 0
            if count < 5:
                clean.append(nums[i])
        nums = clean[:]
        ret = set()
        for mid1 in range(1, len(nums) - 2):
            for mid2 in range(mid1+1, len(nums)-1):
                l, r = 0, len(nums)-1
                while l < mid1 and r > mid2:
                    c = nums[l] + nums[mid1] + nums[mid2] + nums[r]
                    if c == target:
                        ret.add((nums[l], nums[mid1], nums[mid2], nums[r]))
                        l += 1
                    elif c > target:
                        r -= 1
                    elif c < target:
                        l += 1
        ans = []
        for i in ret:
            ans.append(list(i))
        return ans