56. Merge Intervals

Given a collection of intervals, merge all overlapping intervals.

For example,
Given [1,3],[2,6],[8,10],[15,18],
return [1,6],[8,10],[15,18].

# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution:
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        if len(intervals) == 0:
            return []
        a = sorted(intervals, key= lambda x:x.start)
        b, temp, i = [], a[0], 1
        while i < len(a):
            if temp.end >= a[i].start:
                temp.end = max(temp.end, a[i].end)
            else:
                b.append(temp)
                temp = a[i]
            i+=1
        b.append(temp)
        return b