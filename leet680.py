680. Valid Palindrome II

Given a non-empty string s, you may delete at most one character. Judge whether you can make it a palindrome.

Example 1:
Input: "aba"
Output: True
Example 2:
Input: "abca"
Output: True
Explanation: You could delete the character 'c'.
Note:
The string will only contain lowercase characters a-z. The maximum length of the string is 50000.

class Solution(object):
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if len(s) <= 2:
            return True
        idxL, idxR = 0, len(s)-1
        while idxL <= idxR:
            if s[idxL] != s[idxR]:
                return self.check(s, idxL+1, idxR) or self.check(s, idxL, idxR-1)
            else:
                idxL += 1
                idxR -= 1
        return True
    def check(self, s, idxL, idxR):
        while idxL <= idxR:
            if s[idxL] != s[idxR]:
                return False
            else:
                idxL += 1
                idxR -= 1
        return True