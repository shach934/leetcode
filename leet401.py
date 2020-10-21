401. Binary Watch

A binary watch has 4 LEDs on the top which represent the hours (0-11), and the 6 LEDs on the bottom represent the minutes (0-59).

Each LED represents a zero or one, with the least significant bit on the right.


For example, the above binary watch reads "3:25".

Given a non-negative integer n which represents the number of LEDs that are currently on, return all possible times the watch could represent.

Example:

Input: n = 1
Return: ["1:00", "2:00", "4:00", "8:00", "0:01", "0:02", "0:04", "0:08", "0:16", "0:32"]
Note:
The order of output does not matter.
The hour must not contain a leading zero, for example "01:00" is not valid, it should be "1:00".
The minute must be consist of two digits and may contain a leading zero, for example "10:2" is not valid, it should be "10:02".


class Solution(object):
    def readBinaryWatch(self, num):
        """
        :type num: int
        :rtype: List[str]
        """
        if num == 0 :
            return ["0:00"]
        elif num >= 9:
            return []
        
        bumb = [0]*10
        H_weight, M_weight = [1,2,4,8,1,2,4,8,16,32]
        ret = []
        self.dfs(num, bumb, weights, ret)
        return ret
        
        
    def dfs(num, bumb, weights, ret):
        if num == 0 and self.time(bumb, weights):
            ret += self.time(bumb, weights),
        for i in rang(len(bumb)):
            if bumb[i] is 0:
                bumb[i] = 1
                if self.time(bumb, weights):
                    self.dfs(num - 1, bumb, weights, ret)
                bumb[i] = 0
                
    def time(self, bumb, weights):
        hour, minute = 0, 0
            for i in range(4):
                hour += bumb[i] * weights[i]
            for i in range(4, 10):
                minute += bumb[i] * weights[i]
            if hour <= 11 and minute <= 59:
                if minute < 10:
                    return str(hour) + ':0' + str(minute)
                else:
                    return str(hour) + ':' + str(minute)
            else:
                return False
            