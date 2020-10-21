611. Valid Triangle Number

Given an array consists of non-negative integers, your task is to count the number of triplets chosen from the array that can make triangles if we take them as side lengths of a triangle.

Example 1:
Input: [2,2,3,4]
Output: 3
Explanation:
Valid combinations are: 
2,3,4 (using the first 2)
2,3,4 (using the second 2)
2,2,3
Note:
The length of the given array won't exceed 1000.
The integers in the given array are in the range of [0, 1000].

class Solution(object):
    def triangleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = 0
        nums.sort()
        def bs(nums, N):
            left, right = 0, len(nums)-1
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] < N:
                    left = mid + 1
                elif nums[mid] > N:
                    right = mid - 1
                else:
                    return mid
            return right
        zeros = 0
        while zeros < len(nums)  and nums[zeros] is 0 :
            zeros += 1
        for a in range(zeros, len(nums)-2):
            for b in range(a+1, len(nums)-1):
                idx = bs(nums, nums[a] + nums[b])
                while nums[idx] == nums[a]+nums[b] and idx > b:
                    idx -= 1
                count += idx - b        
        return count