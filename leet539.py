539. Minimum Time Difference

Given a list of 24-hour clock time points in "Hour:Minutes" format, find the minimum 
minutes difference between any two time points in the list.

Example 1:
Input: ["23:59","00:00"]
Output: 1
Note:
The number of time points in the given list is at least 2 and won't exceed 20000.
The input time is legal and ranges from 00:00 to 23:59.

class Solution(object):
    def findMinDifference(self, timePoints):
        """
        :type timePoints: List[str]
        :rtype: int
        """
        time = []
        for i in timePoints:
            hour, minute = i.split(':')
            time.append(int(hour)*60 + int(minute))
        time.sort()
        nexday = [i+60*24 for i in time]
        time += nexday
        minT = 60*24
        for i in range(len(time)-1):
            minT = min(minT, time[i+1] - time[i])
        return minT