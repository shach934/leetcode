239. Sliding Window Maximum

Given an array nums, there is a sliding window of size k which is moving from 
the very left of the array to the very right. You can only see the k numbers in the window. 
Each time the sliding window moves right by one position.

For example,
Given nums = [1,3,-1,-3,5,3,6,7], and k = 3.

Window position                Max
---------------               -----
[1  3  -1] -3  5  3  6  7       3
 1 [3  -1  -3] 5  3  6  7       3
 1  3 [-1  -3  5] 3  6  7       5
 1  3  -1 [-3  5  3] 6  7       5
 1  3  -1  -3 [5  3  6] 7       6
 1  3  -1  -3  5 [3  6  7]      7
Therefore, return the max sliding window as [3,3,5,5,6,7].

Note: 
You may assume k is always valid, ie: 1 ≤ k ≤ input array's size for non-empty array.

Follow up:
Could you solve it in linear time?

不能用heap，因为不能保证每次都把出窗的那个元素有效的踢出去。
用了一个队列，其实跟队列也没啥太大关系
主要的因素是：
每次进队的时候，把比他小的都可以踢出去了，因为他是最新进队的，保证了后面覆盖的窗口范围内都不能取到前面的小数了！！
然后每次检查最大数是不是需要出队了，需要出队了就踢出去。然后每次输出之前，检查是不是当前元素早就该出队了

class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        deq, ret = collections.deque(), []
        for i in range(len(nums)):
            while deq and nums[i] > nums[deq[-1]]:
                deq.pop()
            deq += i,
            if deq[0] == i - k:
                deq.popleft()
            if i >= k-1:
                ret += nums[deq[0]],
        return ret