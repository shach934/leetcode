216. Combination Sum III

Find all possible combinations of k numbers that add up to a number n, given that only numbers from 1 to 9 can be used and each combination should be a unique set of numbers.


Example 1:

Input: k = 3, n = 7

Output:

[[1,2,4]]

Example 2:

Input: k = 3, n = 9

Output:

[[1,2,6], [1,3,5], [2,3,4]]

class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        candidates = [i for i in range(1,10)]
        ret = []
        self.backTrack(k,n, [], 0, 0, ret, candidates)
        return ret
    
    def backTrack(self, k, n, curr,idx, currSum, ret, candidates):
        if len(curr) == k and currSum == n:
            ret.append(curr[:])
        if len(curr) < k :
            for i in range(idx, len(candidates)):
                if candidates[i]:
                    curr.append(candidates[i])
                    currSum += candidates[i]
                    candidates[i] = 0
                    self.backTrack(k, n, curr,i+1, currSum, ret, candidates)
                    candidates[i] = i + 1
                    currSum -= candidates[i]
                    curr.pop()