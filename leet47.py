"""
47. Permutations II

Given a collection of numbers that might contain duplicates, return all possible unique permutations.

For example,
[1,1,2] have the following unique permutations:
[
  [1,1,2],
  [1,2,1],
  [2,1,1]
]

和普通的全排列不同的地方在于，每个数字被交换到前面之前，检查在他之前有没有相同的数字已经被交换到前面去过
如果去过，那就不能再交换了！！
"""

class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ret = []
        self. permutation(nums,0,ret)
        return ret
        
    def permutation(self, nums, begin, ret):
        if begin == len(nums)-1:
            ret.append(nums[:])
        else:
            for i in range(begin, len(nums)):
                flag = True
                for ii in range(begin, i):
                    if nums[ii]==nums[i]:
                        flag = False
                if flag:
                    nums[i], nums[begin] = nums[begin], nums[i]
                    self.permutation(nums, begin+1, ret)
                    nums[i], nums[begin] = nums[begin], nums[i]