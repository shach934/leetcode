345. Reverse Vowels of a String

Write a function that takes a string as input and reverse only the vowels of a string.

Example 1:
Given s = "hello", return "holle".

Example 2:
Given s = "leetcode", return "leotcede".

Note:
The vowels does not include the letter "y".

class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        s = [i for i in s]
        left, right = 0, len(s)-1
        while left <= right:
            if s[left] in 'aeiouAEIOU' and s[right] in 'aeiouAEIOU':
                s[left], s[right] = s[right], s[left]
                left += 1
                right -= 1
            elif s[left] in 'aeiouAEIOU':
                right -= 1
            elif s[right] in 'aeiouAEIOU':
                left += 1
            else:
                left += 1
                right -= 1
        return ''.join(s)