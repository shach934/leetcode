"""
39. Combination Sum

Given a set of candidate numbers (C) (without duplicates) and a target number (T), find all unique combinations in C where the candidate numbers sums to T.

The same repeated number may be chosen from C unlimited number of times.

Note:
All numbers (including target) will be positive integers.
The solution set must not contain duplicate combinations.
For example, given candidate set [2, 3, 6, 7] and target 7, 
A solution set is: 
[
  [7],
  [2, 2, 3]
]
"""

class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        ret = []
        self.backTrack(candidates, target, [], 0,0, ret)
        return ret
    
    def backTrack(self, candidates, target, curr, currSum, idx, ret):
        if currSum == target:
            ret.append(curr[:])
        if currSum < target:
            for i in range(idx,len(candidates)):
                curr.append(candidates[i])
                self.backTrack(candidates, target, curr, currSum + candidates[i], i, ret)
                curr.pop()