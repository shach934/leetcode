231. Power of Two

Given an integer, write a function to determine if it is a power of two.

class Solution:
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n <= 0:
            return False 
        
        while n>0:
            if n == 1:
                return True
            elif n%2:
                return False
            else:
                n /= 2