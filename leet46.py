# 46. Permutations

# Given a collection of distinct numbers, return all possible permutations.

# For example,
# [1,2,3] have the following permutations:
# [
  # [1,2,3],
  # [1,3,2],
  # [2,1,3],
  # [2,3,1],
  # [3,1,2],
  # [3,2,1]
# ]

class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ret = []
        self.permutation(ret, nums, curr)
        return ret
        
    def permutation( ret, nums, curr):
        if len(nums) == 0:
            print(curr)
            ret.append(curr[:])
        for i in range(len(nums)):
            curr.append(nums[i])
            nums.pop(i)
            permutation(ret, nums, curr)
            nums.insert(i, curr[-1])
            curr.pop()
            
# 用每个字母于后面字母去交换生成全排列，ms是标准做法

    def permutation2(self, ret, nums, begin):
        if begin == len(nums) -1:
            ret.append(nums[:])   # 大坑啊，，，不能每次都是存一个副本，到时候nums都换回去了，里面保存的就都换回去了！！！
        for i in range(begin,len(nums)):
            nums[begin], nums[i] = nums[i], nums[begin]
            self.permutation2(ret, nums, begin + 1)
            nums[begin], nums[i] = nums[i], nums[begin]