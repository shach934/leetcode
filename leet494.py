494. Target Sum

You are given a list of non-negative integers, a1, a2, ..., an, and a target, S. Now you have 2 symbols + and -. For each integer, you should choose one from + and - as its new symbol.

Find out how many ways to assign symbols to make sum of integers equal to target S.

Example 1:
Input: nums is [1, 1, 1, 1, 1], S is 3. 
Output: 5
Explanation: 

-1+1+1+1+1 = 3
+1-1+1+1+1 = 3
+1+1-1+1+1 = 3
+1+1+1-1+1 = 3
+1+1+1+1-1 = 3

There are 5 ways to assign symbols to make the sum of nums be target 3.
Note:
The length of the given array is positive and will not exceed 20.
The sum of elements in the given array will not exceed 1000.
Your output answer is guaranteed to be fitted in a 32-bit integer.

# 不能用dfs，会超时，要用dp
即使是0，也有正负区分，算两个
能够使用dp，是因为没有后效性

class Solution(object):
    def findTargetSumWays(self, nums, S):
        """
        :type nums: List[int]
        :type S: int
        :rtype: int
        """
        dic = {nums[0]:1, -nums[0]:1} if nums[0] else {0:2}
        for i in range(1,len(nums)):
            newD = {}
            for val in dic.keys():
                newD[val+nums[i]] = dic.get(val, 0) + newD.get(val+nums[i],0)
                newD[val-nums[i]] = dic.get(val, 0) + newD.get(val-nums[i],0)
            dic = newD
        return dic.get(S,0)