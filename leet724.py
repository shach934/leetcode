724. Find Pivot Index

Given an array of integers nums, write a method that returns the "pivot" index of this array.

We define the pivot index as the index where the sum of the numbers to the left of the index 
is equal to the sum of the numbers to the right of the index.

If no such index exists, we should return -1. If there are multiple pivot indexes, 
you should return the left-most pivot index.

Example 1:
Input: 
nums = [1, 7, 3, 6, 5, 6]
Output: 3
Explanation: 
The sum of the numbers to the left of index 3 (nums[3] = 6) is equal to the sum of numbers to the right of index 3.
Also, 3 is the first index where this occurs.
Example 2:
Input: 
nums = [1, 2, 3]
Output: -1
Explanation: 
There is no index that satisfies the conditions in the problem statement.
Note:

The length of nums will be in the range [0, 10000].
Each element nums[i] will be an integer in the range [-1000, 1000].

左扫一遍，右扫一遍
左右累加的相同的时候就是

class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return -1
        Lsum, Rsum = [0], [0]
        for i in range(len(nums)-1):
            Lsum.append(Lsum[-1] + nums[i]) 
        for i in range(len(nums) - 1, 0, -1):
            Rsum.append(Rsum[-1] + nums[i]) 
        Rsum = Rsum[::-1]
        for i in range(len(Lsum)):
            if Lsum[i] == Rsum[i]:
                return i
        return -1