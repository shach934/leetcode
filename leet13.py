# 13. Roman to Integer

# Given a roman numeral, convert it to an integer.

# Input is guaranteed to be within the range from 1 to 3999.

class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        roman = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100,'D':500,'M':1000}
        sum = 0
        for r in range(len(s) - 1):
            if roman[s[r]] >= roman[s[r+1]]:
                sum += roman[s[r]]
            else:
                sum -= roman[s[r]]
        sum += roman[s[-1]]
        return sum