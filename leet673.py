673. Number of Longest Increasing Subsequence

Given an unsorted array of integers, find the number of longest increasing subsequence.

Example 1:
Input: [1,3,5,4,7]
Output: 2
Explanation: The two longest increasing subsequence are [1, 3, 4, 7] and [1, 3, 5, 7].
Example 2:
Input: [2,2,2,2,2]
Output: 5
Explanation: The length of longest continuous increasing subsequence is 1, and there are 5
subsequences' length is 1, so output 5.
Note: Length of the given array will be not exceed 2000 and the answer is guaranteed to be fit in 32-bit signed int.

class Solution(object):
    def findNumberOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        currL, occur, maxL = [1]*len(nums), [1]*len(nums), 1
        for i in range(1, len(nums)):
            ml,dic = 1 ,{}
            for j in range(0, i):
                if nums[i] > nums[j]:
                    if ml <= currL[j] + 1:
                        ml = currL[j] + 1
                        dic[ml] = dic.get(ml,0) + occur[j]
            currL[i] = ml
            occur[i] = dic.get(ml,1)
            maxL = max(maxL, currL[i])
        count = 0
        for i in range(len(nums)):
            if currL[i] == maxL:
                count += occur[i]
        return count
