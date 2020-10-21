164. Maximum Gap

仿bucket sort，把每个数字都放到各个范围桶里面去，桶多来一个，一定会有桶间隔的。这个时候用各个桶的间隔取最大值。

Given an unsorted array, find the maximum difference between the successive elements in its sorted form.

Try to solve it in linear time/space.

Return 0 if the array contains less than 2 elements.

You may assume all elements in the array are non-negative integers and fit in the 32-bit signed integer range.

class Solution(object):
    def maximumGap(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) < 2:
            return 0
        n = len(nums)
        big, small = float('-inf'), float('inf')
        for num in nums:
            big = max(big, num)
            small = min(small, num)
        if big == small:
            return 0
        maxs, mins = [float('-inf') for i in range(n+1)], [float('inf') for i in range(n+1)]
        filled = [False for i in range(n+1)]
        steps = (big - small) * 1.0  / n
        for num in nums:
            idx = int((num - small) / steps)
            if filled[idx]:
                maxs[idx] = max(maxs[idx], num)
                mins[idx] = min(mins[idx], num)
            else:
                filled[idx] = True
                maxs[idx] = num
                mins[idx] = num
        lastMax, ret = maxs[0], maxs[0] - mins[0]
        for i in range(1, n+1):
            if filled[i]:
                ret = max(ret, mins[i] - lastMax)
                lastMax = maxs[i]
        return ret