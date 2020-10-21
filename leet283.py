283. Move Zeroes

Given an array nums, write a function to move all 0's to the end of it 
while maintaining the relative order of the non-zero elements.

For example, given nums = [0, 1, 0, 3, 12], after calling your function, 
nums should be [1, 3, 12, 0, 0].

Note:
You must do this in-place without making a copy of the array.
Minimize the total number of operations.

class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        zeros = [i for i in range(len(nums)) if nums[i] == 0]
        nums[:] = [nums[i] for i in range(len(nums)) if i not in zeros] + [0 for i in range(len(zeros))]
        # 谨防python里面这个list赋值的问题，在这个函数里面怎么改，出去一传参就完蛋，因为仅仅是传引用
        # 想要删除赋值啥的，都要加一个[:]