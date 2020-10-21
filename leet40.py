40. Combination Sum II

Given a collection of candidate numbers (C) and a target number (T), find all unique combinations in C where the candidate numbers sums to T.

Each number in C may only be used once in the combination.

Note:
All numbers (including target) will be positive integers.
The solution set must not contain duplicate combinations.
For example, given candidate set [10, 1, 2, 7, 6, 1, 5] and target 8, 
A solution set is: 
[
  [1, 7],
  [1, 2, 5],
  [2, 6],
  [1, 1, 6]
]

class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        ret = []
        candidates.sort()
        self.backTrack(candidates, target, [], 0, 0, ret)
        return ret
    
    def backTrack(self, candidates, target, curr, currSum, idx, ret):
        if currSum == target:
            ret.append(curr[:])
        if currSum < target:
            for i in range(idx,len(candidates)):
                if i > idx and candidates[i] == candidates[i-1]:
                    continue
                curr.append(candidates[i])
                self.backTrack(candidates, target, curr, currSum + candidates[i], i+1, ret)
                curr.pop()