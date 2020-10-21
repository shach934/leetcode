90. Subsets II

Given a collection of integers that might contain duplicates, nums, return all possible subsets (the power set).

Note: The solution set must not contain duplicate subsets.

For example,
If nums = [1,2,2], a solution is:

[
  [2],
  [1],
  [1,2,2],
  [2,2],
  [1,2],
  []
]

class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ret = []
        nums.sort()
        self.backTrack(nums, 0, [], ret)
        return ret
    
    def backTrack(self, nums, idx, curr, ret):
        ret.append(curr[:])
        for i in range(idx, len(nums)):
            if i > idx and nums[i-1] == nums[i]:
                continue
            curr.append(nums[i])
            self.backTrack(nums, i+1, curr, ret)
            curr.pop()