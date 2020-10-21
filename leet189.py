# 189. Rotate Array

# Rotate an array of n elements to the right by k steps.

# For example, with n = 7 and k = 3, the array [1,2,3,4,5,6,7] is rotated to [5,6,7,1,2,3,4].

# Note:
# Try to come up as many solutions as you can, there are at least 3 different ways to solve this problem.

# [show hint]

# Hint:
# Could you do it in-place with O(1) extra space?
# Related problem: Reverse Words in a String II

# inplace只用额外一个space的解法，分两种，一个是k整除n的情况，这种分两层嵌套，外层为k，内层为k%n,
# k%n不能整除的时候，一个循环，n次即可, 不能整除的时候，也会出现循环。

class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        if k%len(nums) is 0:
            return
        k %= len(nums)
        num = nums[:]
        for i in range(len(num)):
            if i + k < len(num):
                nums[i+k] = num[i]
            else:
                nums[i+k-len(nums)] = num[i]
                
# 用了最傻耗空间最多的一种方法实现的。没有解决跳格子移动的循环问题。。。。
# 留到第二次刷题的时候再看吧。