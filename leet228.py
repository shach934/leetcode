# 228. Summary Ranges

# Given a sorted integer array without duplicates, 
# return the summary of its ranges.

# Example 1:
# Input: [0,1,2,4,5,7]
# Output: ["0->2","4->5","7"]
# Example 2:
# Input: [0,2,3,4,6,8,9]
# Output: ["0","2->4","6","8->9"]

# 一共有三种状态，位于序列中，位于序列外，序列外分为结束序列或者一个元素就是一个序列。
class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """

        ret, start, end, flag = [], 0, 0, False
        if not nums :
            return nums
        
        for i in range(len(nums) - 1):
            if nums[i+1] - nums[i] == 1 and not flag:
                flag = True
                start = i
            elif nums[i+1] - nums[i] != 1 and flag:
                flag = False
                ret += [str(nums[start]) + "->" + str(nums[i])]
                start, end = i, i
            elif nums[i+1] - nums[i] != 1 and not flag:
                ret += [str(nums[i])]
                start, end = i, i
        if flag: 
            ret += [str(nums[start]) + "->" + str(nums[-1])]
        else:
            ret += [str(nums[-1])] 
        return ret