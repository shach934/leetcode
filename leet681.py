681. Next Closest Time

Given a time represented in the format "HH:MM", form the next closest time by reusing 
the current digits. There is no limit on how many times a digit can be reused.

You may assume the given input string is always valid. For example, "01:34", 
"12:09" are all valid. "1:34", "12:9" are all invalid.

Example 1:

Input: "19:34"
Output: "19:39"
Explanation: The next closest time choosing from digits 1, 9, 3, 4, is 19:39, which occurs 5 minutes later.  
It is not 19:33, because this occurs 23 hours and 59 minutes later.
Example 2:

Input: "23:59"
Output: "22:22"
Explanation: The next closest time choosing from digits 2, 3, 5, 9, is 22:22. It may be assumed that the returned 
time is next day's time since it is smaller than the input time numerically.

class Solution(object):
    def nextClosestTime(self, time):
        """
        :type time: str
        :rtype: str
        """
        avai = {}
        for i in time:
            avai[i] = avai.get(i, 0) + 1
        i, j, hour, minite = 0, 0, int(time[0:2]), int(time[-2:])
        print(hour, minite)
        for i in range(24):
            for j in range(60):
                minite += 1
                hour += minite / 60
                hour %= 24
                minite %= 60
                newtime = ''
                if hour < 10:
                    newtime += '0' + str(hour)
                else:
                    newtime += str(hour)
                if minite<10:
                    newtime += '0' +str(minite)
                else:
                    newtime += str(minite)
                flag = True
                for i in newtime:
                    if i not in avai:
                        flag = False
                if flag:
                    return newtime[:2] + ':' + newtime[-2:]