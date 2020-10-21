# 136. Single Number

# Given an array of integers, every element appears 
# twice except for one. Find that single one.

# Note:
# Your algorithm should have a linear runtime complexity. 
# Could you implement it without using extra memory?

class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        mydict = {}
        for i in nums:
            if i in mydict:
                mydict.pop(i)
            else:
                mydict[i] = 1
        return mydict.keys()[0]