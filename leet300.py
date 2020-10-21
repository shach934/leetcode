"""
300. Longest Increasing Subsequence 

Given an unsorted array of integers, find the length of longest increasing subsequence.

For example,
Given [10, 9, 2, 5, 3, 7, 101, 18],
The longest increasing subsequence is [2, 3, 7, 101], therefore the length is 4. 
Note that there may be more than one LIS combination, it is only necessary for you to return the length.

Your algorithm should run in O(n2) complexity.

Follow up: Could you improve it to O(n log n) time complexity?

O(n^2) 的DP解法，从前往后数，每次从前往后看，用一个数列记录以当前这个数为结尾的上升序列的最大长度

O(nlogn) 解法是要用到二分查找的，这样就不用n而只是logn了
但是完全想不到怎么用到二分查找。。。。
"""
class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        currL, maxL = [1]*len(nums), 1
        for i in range(1, len(nums)):
            ml = 1
            for j in range(0, i):
                if nums[i] > nums[j]:
                    ml = max(ml, currL[j] + 1)
            currL[i] = ml
            #print(currL)
            maxL = max(maxL, currL[i])
        return maxL