154. Find Minimum in Rotated Sorted Array II

Follow up for "Find Minimum in Rotated Sorted Array":
What if duplicates are allowed?

Would this affect the run-time complexity? How and why?

Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).

Find the minimum element.

The array may contain duplicates.


class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def helper(nums, l, r):
            if l == r:
                return nums[l]
            mid = (l + r)//2
            if nums[l] < nums[r]:
                return nums[l]
            elif nums[l] >= nums[r] :
                if nums[mid] < nums[r]:
                    return helper(nums, l, mid)
                elif nums[mid] > nums[l]:
                    return helper(nums, mid+1, r)
                else:
                    return min(helper(nums, l, mid), helper(nums, mid+1, r))
        return helper(nums, 0, len(nums)-1)