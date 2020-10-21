"""
Given an integer array, your task is to find all the different possible increasing subsequences of the given array, and the length of an increasing subsequence should be at least 2 .

Example:
Input: [4, 6, 7, 7]
Output: [[4, 6], [4, 7], [4, 6, 7], [4, 6, 7, 7], [6, 7], [6, 7, 7], [7,7], [4,7,7]]
Note:
The length of the given array will not exceed 15.
The range of integer in the given array is [-100,100].
The given array may contain duplicates, and two equal integers should also be considered as a special case of increasing sequence.

"""
class Solution:
    def findSubsequences(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        
        def dfs(nums, head, idx, res):
            if idx < len(nums):
                for i in range(idx, len(nums)):
                    if nums[i] >= head[-1]:
                        if (i == idx) or (i > idx and nums[i] != nums [i - 1]):
                            augu = tuple(list(head) + [nums[i]])
                            res.add(augu)
                            dfs(nums, augu, i + 1, res)
        res = set()
        for i in range(len(nums) - 1):
            dfs(nums, [nums[i]], i + 1, res)
        res = [list(a) for a in res]
        return res

nums = [1,4,3,6]
obj = Solution()
res = obj.findSubsequences(nums)
print(res)