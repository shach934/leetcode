233. Number of Digit One

Given an integer n, count the total number of digit 1 appearing in all non-negative integers less than or equal to n.

For example:
Given n = 13,
Return 6, because digit 1 occurred in the following numbers: 1, 10, 11, 12, 13.

class Solution(object):
    def countDigitOne(self, n):
        """
        :type n: int
        :rtype: int
        """
        ans, m = 0, 1
        while n >= m:
            if (n//m)%10 == 1:
                ans += n%m + 1 + (n// (m*10))*m
            elif (n//m) % 10 == 0:
                ans += (n//(m*10))*m
            else:
                ans += (n//(m*10)+1) * m
            m *= 10
        return ans