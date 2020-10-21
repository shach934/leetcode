209. Minimum Size Subarray Sum

Given an array of n positive integers and a positive integer s, find the minimal length of a contiguous subarray of which the sum ≥ s. If there isn't one, return 0 instead.

For example, given the array [2,3,1,2,4,3] and s = 7,
the subarray [4,3] has the minimal length under the problem constraint.

click to show more practice.

More practice:
If you have figured out the O(n) solution, try coding another solution of which the time complexity is O(n log n).

class Solution(object):
    def minSubArrayLen(self, s,nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        minL, length, summ, left, idx = len(nums) + 1, 0, 0, 0, 0
        while idx < len(nums):
            while summ < s:
                summ += nums[idx]
                idx += 1
                length += 1
                if idx >= len(nums):  break
            while summ >= s:
                minL = min(minL, length)
                summ -= nums[left]
                left += 1
                length -= 1
        return 0 if minL == len(nums) +1 else minL