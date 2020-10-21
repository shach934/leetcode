"""
53. Maximum Subarray

Find the contiguous subarray within an array (containing at least one number) which has the largest sum.

For example, given the array [-2,1,-3,4,-1,2,1,-5,4],
the contiguous subarray [4,-1,2,1] has the largest sum = 6.

click to show more practice.

More practice:
If you have figured out the O(n) solution, try coding another solution using the 
divide and conquer approach, which is more subtle.

线性解法，用陈越在数据结构课程上的方法，算法导论上的线性法没看明白。。。。。
"""

class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_sum, this_sum =float('-inf'), 0
        for i in nums:
            this_sum += i
            if this_sum > max_sum:
                max_sum = this_sum
            if this_sum < 0:
                this_sum = 0
        return max_sum
"""        
分治法，关键在于左右两边最大的那个，
固定了中间，必然要跨越两边，所以就只有一头需要遍历了。变成了线性的
"""
class Solution2(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return self.maxSub(nums, 0, len(nums)-1)
        
    def maxSub(self, nums, left, right):
        if left == right:
            return nums[left]
        mid = (left + right) // 2
        max_left = self.maxSub(nums,left, mid)
        max_right = self.maxSub(nums, mid+1, right)
        max_xos = self.Xos(nums, left, right)
        
        if max_left >= max_right and max_left >= max_xos:
            return max_left
        elif max_right >= max_left and max_right >= max_xos:
            return max_right
        else:
            return max_xos
        
    def Xos(self, nums, left, right):
        mid = (left + right) // 2
        max_left, max_right = float('-inf'), float('-inf')
        sum_left, sum_right = 0, 0
        for i in range(mid, left - 1, -1):
            sum_left += nums[i]
            max_left = max(max_left, sum_left)
        for j in range(mid+1, right+1):
            sum_right += nums[j]
            max_right = max(max_right, sum_right)
        return max_left + max_right 
