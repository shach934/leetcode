9. Palindrome Number

Determine whether an integer is a palindrome. Do this without extra space.

click to show spoilers.

Some hints:
Could negative integers be palindromes? (ie, -1)

If you are thinking of converting the integer to string, note the restriction of using extra space.

You could also try reversing an integer. However, if you have solved the problem "Reverse Integer", you know that the reversed integer might overflow. How would you handle such case?

There is a more generic way of solving this problem.

class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        n = 0
        if x < 0: return False
        while x//(10**n):
            n += 1
        for i in range(n//2):
            digiR = x//(10**i) % 10
            digiL = x//(10**(n-i-1)) % 10
            if digiL != digiR:
                return False
        return True