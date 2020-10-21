78. Subsets

Given a set of distinct integers, nums, return all possible subsets (the power set).

Note: The solution set must not contain duplicate subsets.

For example,
If nums = [1,2,3], a solution is:

[
  [3],
  [1],
  [2],
  [1,2,3],
  [1,3],
  [2,3],
  [1,2],
  []
]

backTracking method, record all the possible set during the backtracking

class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ret = [[]]
        self.backTrack(nums, 0, [], ret)
        return ret
    
    def backTrack(self, nums, idx, curr, ret):
        for i in range(idx, len(nums)):
            curr.append(nums[i])
            ret.append(curr[:])
            self.backTrack(nums, i+1, curr, ret)
            curr.pop()
            
class Solution(object):
    def subsets(self, nums):
        ret = []
        count = 2**len(nums)
        for i in range(count):
            
        
        