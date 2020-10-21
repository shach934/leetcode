# 1 two sum
# Given an array of integers, return indices of the two numbers such that they add up to a specific target.

# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# Given nums = [2, 7, 11, 15], target = 9,

# Because nums[0] + nums[1] = 2 + 7 = 9,
# return [0, 1].

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



# def twoSum2(self, numbers, target):
    # dic = {}
    # for i, num in enumerate(numbers):
        # if target-num in dic:
            # return [dic[target-num]+1, i+1]
        # dic[num] = i