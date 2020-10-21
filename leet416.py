416. Partition Equal Subset Sum

Given a non-empty array containing only positive integers, find if the array can be partitioned into two subsets such that the sum of elements in both subsets is equal.

Note:
Each of the array element will not exceed 100.
The array size will not exceed 200.
Example 1:

Input: [1, 5, 11, 5]

Output: true

Explanation: The array can be partitioned as [1, 5, 5] and [11].
Example 2:

Input: [1, 2, 3, 5]

Output: false

Explanation: The array cannot be partitioned into equal sum subsets.

dfs的过不了，dfs简直就是穷举啊，很多时候不能用dfs，只能用dp，很多时候dfs可以转化成dp。避免了重复去做同样的事情。
dfs就是一棵树，很多时候同样的节点往下走，所以这个时候可以用dp

class Solution(object):
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if len(nums)==0:
            return True
        total = sum(nums)
        if (total // 2) + (total//2) != total:
            return False
        taken = [1]*len(nums)
        flag = [False]
        self.dfs(nums, taken, 0, total, flag)
        return flag[0]
        
    def dfs(self, nums, taken, curr, total, flag):
        if curr == total // 2:
            flag[0] = True
            return flag
        if flag[0] is True:
            return True
        for i in range(len(nums)):
            if taken[i]:
                curr += nums[i]
                taken[i] = 0
                flag = self.dfs(nums, taken, curr, total, flag)
                if flag[0] is True:
                    return flag
                taken[i] = 1
                curr -= nums[i]
        return flag
        
dp 方法通过了。

class Solution(object):
    def canPartition(self, nums):
        if len(nums) == 0:
            return True
        total = sum(nums)
        if total & 1:
            return False
        target = total // 2
        dp = set()
        for i in range(len(nums)):
            dp.update([num[i] + n for n in dp]) 
            dp.add(nums[i])
            if target in dp:
                return True
        return target in dp