# 167. Two Sum II - Input array is sorted

# Given an array of integers that is already sorted in ascending order, find two numbers such that they add up to a specific target number.

# The function twoSum should return indices of the two numbers such that they add up to the target, where index1 must be less than index2. Please note that your returned answers (both index1 and index2) are not zero-based.

# You may assume that each input would have exactly one solution and you may not use the same element twice.

# Input: numbers={2, 7, 11, 15}, target=9
# Output: index1=1, index2=2

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        dictor = {}
        ind = 0
        for i in nums:
            dictor[i] = ind
            ind += 1
        for n in range(len(nums)):
            if target - nums[n] in dictor:
                if dictor[nums[n]] != dictor[target - nums[n]]:
                    return dictor[nums[n]], dictor[target - nums[n]]
                else:
                    record = nums[n]
        lists = []
        for n in range(len(nums)):
            if(nums[n] == record):  
                lists.append(n)
        return lists

# this problem can be solved by other methods instead of hash table, two pointers, binary search
# implement later