647. Palindromic Substrings

Given a string, your task is to count how many palindromic substrings in this string.

The substrings with different start indexes or end indexes are counted as different substrings even they consist of same characters.

Example 1:
Input: "abc"
Output: 3
Explanation: Three palindromic strings: "a", "b", "c".
Example 2:
Input: "aaa"
Output: 6
Explanation: Six palindromic strings: "a", "a", "a", "aa", "aa", "aaa".
Note:
The input string length won't exceed 1000.

class Solution(object):
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        if not n:
            return 0
        dp = [[False]*n for i in range(n)]
        for i in range(n):
            dp[0][i] = True
        for l in range(2, n+1):
            for start in range(n-l+1):
                if l & 1 and s[start] == s[l+start-1] and dp[l-3][start+1]:
                    dp[l-1][start] = True 
                elif l % 2 == 0 and s[start] == s[l+start-1]:
                    if l == 2:
                        dp[l-1][start] = True
                    elif dp[l-3][start+1]:
                        dp[l-1][start] = True
        count = 0
        for i in range(n):
            for j in range(n):
                if dp[i][j]:
                    count += 1
        return count