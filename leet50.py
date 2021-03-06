"""50. Pow(x, n)
Implement pow(x, n).


Example 1:

Input: 2.00000, 10
Output: 1024.00000
Example 2:

Input: 2.10000, 3
Output: 9.26100
"""

class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if n == 0:
            return 1.0
        if n < 0 :
            return 1/self.pow(x, -n)
        else:
            return self.pow(x, n)
    def pow(self, x, n):
        if n == 1:
            return x
        a = self.pow(x, n/2)
        if n%2:
            return a * a * x
        else:
            return a * a