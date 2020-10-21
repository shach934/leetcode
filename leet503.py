# 503. Next Greater Element II

# Given a circular array (the next element of the last element is the 
# first element of the array), print the Next Greater Number for every 
# element. The Next Greater Number of a number x is the first greater 
# number to its traversing-order next in the array, which means you 
# could search circularly to find its next greater number. 
# If it doesn't exist, output -1 for this number.

# Example 1:
# Input: [1,2,1]
# Output: [2,-1,2]
# Explanation: The first 1's next greater number is 2; 
# The number 2 can't find next greater number; 
# The second 1's next greater number needs to search circularly, which is also 2.
# Note: The length of given array won't exceed 10000.

# with stack, 62ms
class Solution(object):
    def nextGreaterElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        nums = nums * 2
        l = nums*2
        ret, stack = [-1]*l, []
        for i in range(l*2):
            while stack and nums[stack[-1]] < nums[i]: 
            # 这一行利用了当前栈里面全是降序的排列这个特性，只检查最后一个，
            # 保证了不会大量的回溯，每次都是输出有效的，运算次数是1 而不是n
                ret[stack[-1]] = nums[i]
                stack.pop()
            stack.append(i)
        return ret[0:l/2]

# first version with O(n^2), time exceed, 972ms, 换成两个数组连接起来，避免用取余操作，直接彪了一倍的时间。
# class Solution(object):
    # def nextGreaterElements(self, nums):
        # """
        # :type nums: List[int]
        # :rtype: List[int]
        # """
        # ret = [-1]*len(nums)
        # for i in range(len(nums)):
            # j = i
            # for dum in range(len(nums)):
                # j = (j + 1)%len(nums)       
                # if nums[j] > nums[i]:
                    # ret[i] = nums[j]
                    # break
        # return ret