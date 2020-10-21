357. Count Numbers with Unique Digits

Given a non-negative integer n, count all numbers with unique digits, x, where 0 ≤ x < 10n.

Example:
Given n = 2, return 91. (The answer should be the total numbers in the range of 0 ≤ x < 100, excluding [11,22,33,44,55,66,77,88,99])

backtracking的解法，能给出答案，但是就是太慢了，看了一眼答案，才发现这是个排列组合的问题，不需要自己去搞。。。。

class Solution(object):
    def countNumbersWithUniqueDigits(self, nn):
        """
        :type n: int
        :rtype: int
        """
        if nn == 0:
            return 1
        if nn == 1:
            return 10
        nums, count = [], [10]
        for n in range(2,nn+1):
            for i in range(1,10):
                nums = [i]
                self.backtrack(nums, n, count)

        return count[0]
        
    def backtrack(self, nums, n, count):
        if len(nums) == n:
            count[0] += 1
        else:
            for i in range(10):
                flag = True
                for j in nums:
                    if j==i:
                        flag = False
                if flag:
                    nums.append(i)
                    self.backtrack(nums, n, count)
                    nums.pop()

                    
！！！写的真好，计算n的时候 自动把前面n-1位的结果累加在里面了，就是往后面又加了一位更少选择的
class Solution(object):
    def countNumbersWithUniqueDigits(self, nn):
        """
        :type n: int
        :rtype: int
        """
        if nn == 0:
            return 1
        if nn == 1:
            return 10
        prod, accum = 9, 10
        for i in range(2,nn+1):
            prod *= 10-i+1
            accum += prod
        return accum