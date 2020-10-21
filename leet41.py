41. First Missing Positive

Given an unsorted integer array, find the first missing positive integer.

For example,
Given [1,2,0] return 3,
and [3,4,-1,1] return 2.

Your algorithm should run in O(n) time and uses constant space.

这类问题，需要在原地，不能用任何的space，那么能用的就只能是原来的数组内容了。
只能通过修改数组内容来达到目的。根据题意，需要找的是1到n中哪个不在数组里面。
其实是类似于bucket sort。使用1 到 n作为index，然后去找哪个数开始不在数组里面。

class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        for i in range(len(nums)):
            while nums[i] > 0 and nums[i] < n and nums[nums[i] - 1] != nums[i]:
                a, b = nums[i], nums[nums[i] - 1]
                nums[nums[i] - 1], nums[i] = a, b
        for i in range(len(nums)):
            if nums[i] != i + 1:
                return i + 1
        return n + 1