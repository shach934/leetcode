409. Longest Palindrome

Given a string which consists of lowercase or uppercase letters, find the length of the longest palindromes that can be built with those letters.

This is case sensitive, for example "Aa" is not considered a palindrome here.

Note:
Assume the length of given string will not exceed 1,010.

Example:

Input:
"abccccdd"

Output:
7

Explanation:
One longest palindrome that can be built is "dccaccd", whose length is 7.

class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        dic = {}
        for ll in s:
            dic[ll] = dic.get(ll, 0)+1
        count, flag = 0, False
        for key in dic.keys():
            count += 2 * (dic[key] // 2)
            if dic[key] & 1:
                flag = True
        if flag:
            count += 1
        return count       