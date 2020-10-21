80. Remove Duplicates from Sorted Array II

Follow up for "Remove Duplicates":
What if duplicates are allowed at most twice?

For example,
Given sorted array nums = [1,1,1,2,2,3],

Your function should return length = 5, with the first five elements of nums being 1, 1, 2, 2 and 3. 
It doesn't matter what you leave beyond the new length.


class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        dist, count, curr = 1, 1, nums[0]
        for i in range(1,len(nums)):
            if nums[i] != curr:
                nums[dist] = nums[i]
                curr = nums[dist]
                dist += 1
                count = 1
            elif count < 2:
                nums[dist] = nums[i]
                count += 1
                dist += 1                
        return dist