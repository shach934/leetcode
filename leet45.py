45. Jump Game II

Given an array of non-negative integers, you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Your goal is to reach the last index in the minimum number of jumps.

For example:
Given array A = [2,3,1,1,4]

The minimum number of jumps to reach the last index is 2. (Jump 1 step from index 0 to 1, then 3 steps to the last index.)

""" 
这个题目的关键点在于，根本不需要每个点都更新记录其到达的步数，因为从一个点出发，能够到达的点是连在一起的。
所以每步能够走的点一定是连在一起，位于左侧的，需要做的就是每次记录该步能够走的最远的位置。等到这个位置到达了
最右边，就可以返回了。
"""

class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        curr_max, level, last_reach, idx = 0, 0, 0, 0
        while curr_max < len(nums) - 1:
            for i in range(idx, last_reach+1):
                curr_max = max(curr_max, i + A[i])
            level += 1
            idx = last_reach + 1
            last_reach = curr_max
        return level


"""
# BFS 也不够快，需要33s左右。避免了一些重复，但是还不够快。
class Solution(object):
    def jump(self, nums):

        :type nums: List[int]
        :rtype: int

        frontier, seen = [0], {0:0}
        next_level, idx = [], 1
        while frontier:
            for start_point in frontier:
                if start_point == len(nums) - 1:
                    return seen[start_point]
                jump = nums[start_point]
                for i in range(start_point+1, start_point+jump+1):
                    if i not in seen and i < len(nums):
                        next_level.append(i)
                        seen[i] = idx
            idx += 1
            frontier = next_level
"""
                

"""
# first Version, dp, n^2,super slow, 250000 nums take 206s. n方也太慢了，不应该这么慢才对。

class Solution(object):
    def jump(self, nums):
        steps = [i for i in range(n)]
        for idx in range(len(nums)-1):
            jump = nums[idx]
            for i in range(1, jump+1):
                if idx + i < len(nums):
                    steps[idx+i] = min(steps[idx+i], steps[idx] + 1)
                    if steps[-1] < n-1:
                        return steps[-1]
        # return steps[-1]
"""