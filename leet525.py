525. Contiguous Array

Given a binary array, find the maximum length of a contiguous subarray with equal number of 0 and 1.

Example 1:
Input: [0,1]
Output: 2
Explanation: [0, 1] is the longest contiguous subarray with equal number of 0 and 1.
Example 2:
Input: [0,1,0]
Output: 2
Explanation: [0, 1] (or [1, 0]) is a longest contiguous subarray with equal number of 0 and 1.
Note: The length of the given binary array will not exceed 50,000.


# 第一次的思路，用一个字典统计，然后看看哪个多，从两头往外踢多的元素，但是这种对于pattern不敏感，得不到正确答案
# 看了discussion之后 看到别人怎么做的，累积一个count，遇见1加1，遇到0减一，如果count的值前面出现过，说明上次的值到当前值之间是个对称的
class Solution(object):
    def findMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        record = {}
        count, record[0], maxL = 0, 0, 0
        for i in range(len(nums)):
            if nums[i] == 0:
                count -= 1
            else:
                count += 1
            if count in record:
                maxL = max(maxL, i - record[count] + 1)
            else:
                record[count] = i+1
        return maxL