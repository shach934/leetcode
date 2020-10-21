15. 3Sum

Given an array S of n integers, are there elements a, b, c in S such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

Note: The solution set must not contain duplicate triplets.

For example, given array S = [-1, 0, 1, 2, -1, -4],

A solution set is:
[
  [-1, 0, 1],
  [-1, -1, 2]
]


class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums) < 3:
            return []
        nums.sort()
        clean, count = [nums[0]], 1
        for idx in range(1, len(nums)):
            if nums[idx] == clean[-1]:
                count += 1
            else:
                count = 0
            if count < 3 or (count == 3 and nums[idx] == 0):
                clean.append(nums[idx])
        dicts = {}
        for i in range(len(clean)):
            if clean[i] in dicts:
                dicts[clean[i]].append(i)
            else:
                dicts[clean[i]] = [i]
        ret = set()
        for i in range(len(clean) - 2):
            for j in range(i+1, len(clean) - 1):
                c = -clean[i] - clean[j]
                if c in dicts and dicts[c][-1] > j:
                    ret.add((clean[i], clean[j], c))
        ret2 = []
        for i in ret:
            ret2.append(list(i))
        return ret2