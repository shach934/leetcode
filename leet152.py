152. Maximum Product Subarray

Find the contiguous subarray within an array (containing at least one number) which has the largest product.

For example, given the array [2,3,-2,4],
the contiguous subarray [2,3] has the largest product = 6.

class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return self.maxProd(nums, 0, len(nums)-1)
    
    def maxProd(self, nums,left, right):
        if left == right:
            return nums[left]
        mid = (left + right) // 2
        max_left = self.maxProd(nums, left, mid)
        max_right = self.maxProd(nums, mid + 1, right)
        max_xos = self.max_xos(nums, left, right)
        
        if max_left >= max_right and max_left >= max_xos:
            return max_left
        elif max_right >= max_left and max_right >= max_xos:
            return max_right
        else:
            return max_xos
        
    def max_xos(self, nums, left, right):
        max_left,min_left, max_right, min_right = float('-inf'), float('inf'), float('-inf'), float('inf')
        prod_left, prod_right = 1, 1
        mid = (left + right) // 2
        for i in range(mid, left-1,-1):
            prod_left *= nums[i]
            min_left = min(min_left, prod_left)
            max_left = max(max_left, prod_left)
        for j in range(mid+1, right+1):
            prod_right *= nums[j]
            min_right = min(min_right, prod_right)
            max_right = max(max_right, prod_right)
        return max([min_left*min_right, min_left*max_right, min_right*max_left, max_left * max_right])