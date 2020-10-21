69. Sqrt(x)

Implement int sqrt(int x).

Compute and return the square root of x.

x is guaranteed to be a non-negative integer.


Example 1:

Input: 4
Output: 2
Example 2:

Input: 8
Output: 2
Explanation: The square root of 8 is 2.82842..., and since we want to return an integer, 
the decimal part will be truncated.

class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x == 0:
            return 0
        l, r = 1, x
        while l<r:
            mid = (l+r)/2
            if mid * mid == x:
                return mid
            if mid*mid>x:
                r = mid - 1
            else:
                l = mid+1
        if l*l>x:
            return l - 1
        else:
            return l