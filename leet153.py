153. Find Minimum in Rotated Sorted Array

Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).

Find the minimum element.

You may assume no duplicate exists in the array.

class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:
            return nums[0]
        l, r = 0, len(nums)-1
        if nums[l] < nums[r]:
            return nums[l]
        while l<r:
            mid = (l+r)/2
            if nums[r] < nums[mid]:
                l = mid + 1
            elif nums[r] > nums[mid]:
                r = mid
        return nums[r]