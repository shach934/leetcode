162. Find Peak Element

A peak element is an element that is greater than its neighbors.

Given an input array where num[i] ≠ num[i+1], find a peak element and return its index.

The array may contain multiple peaks, in that case return the index to any one of the peaks is fine.

You may imagine that num[-1] = num[n] = -∞.

For example, in array [1, 2, 3, 1], 3 is a peak element and your function should return the index number 2.

class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l, r = 0, len(nums) - 1
        x = self.Bsearch(nums, l, r)
        return x
    def Bsearch(self, nums, l, r):
        mid = (l+r)/2
        if mid-1>=l and nums[mid] < nums[mid-1]:
            x = self.Bsearch(nums, l, mid-1)
        elif mid+1<=r and nums[mid] < nums[mid + 1]:
            x = self.Bsearch(nums, mid + 1, r)
        else:
            return mid
        return x