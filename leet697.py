697. Degree of an Array

Given a non-empty array of non-negative integers nums, the degree of this array is defined as the maximum frequency of any one of its elements.

Your task is to find the smallest possible length of a (contiguous) subarray of nums, that has the same degree as nums.

Example 1:
Input: [1, 2, 2, 3, 1]
Output: 2
Explanation: 
The input array has a degree of 2 because both elements 1 and 2 appear twice.
Of the subarrays that have the same degree:
[1, 2, 2, 3, 1], [1, 2, 2, 3], [2, 2, 3, 1], [1, 2, 2], [2, 2, 3], [2, 2]
The shortest length is 2. So return 2.
Example 2:
Input: [1,2,2,3,1,4,2]
Output: 6
Note:

nums.length will be between 1 and 50,000.
nums[i] will be an integer between 0 and 49,999.

class Solution:
    def findShortestSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:
            return 1
        count = {}
        
        for i in range(len(nums)):
            if nums[i] in count:
                count[nums[i]].append(i)
            else:
                count[nums[i]] = [i]
        a = sorted(count.items(), key = lambda x: len(x[1]), reverse = True)
        print(a)
        maxL, minL = len(a[0][1]), a[0][1][-1] - a[0][1][0] + 1
        print(minL)
        for i in a:
            if len(i[1]) == maxL:
                minL = min(minL, i[1][-1] - i[1][0] + 1)
            else:
                break
        return minL