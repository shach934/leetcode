33. Search in Rotated Sorted Array

Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).

You are given a target value to search. If found in the array return its index, otherwise return -1.

You may assume no duplicate exists in the array.


class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        def findCut(nums):
            l, r = 0, len(nums) - 1
            while l <= r:
                mid = (l + r)// 2
                if nums[mid] >= nums[l]:
                    l += 1
                elif nums[mid] < nums[r]:
                    r = mid
            return r
        
        def bSearch(nums, l, r, target):
            while l <= r:
                mid = (l+r)//2
                if nums[mid] < target: 
                    l = mid + 1
                elif nums[mid] > target:
                    r = mid - 1
                else:
                    return mid
            return -1
        
        if len(nums)==0:
            return -1
        if nums[0] <= nums[-1]:
            return bSearch(nums, 0, len(nums)-1, target)
        cut = findCut(nums)
        a = bSearch(nums, 0, cut-1, target)
        if a != -1:
            return a
        return bSearch(nums, cut, len(nums)-1, target)