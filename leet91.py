91. Decode Ways

A message containing letters from A-Z is being encoded to numbers using the following mapping:

'A' -> 1
'B' -> 2
...
'Z' -> 26
Given an encoded message containing digits, determine the total number of ways to decode it.

For example,
Given encoded message "12", it could be decoded as "AB" (1 2) or "L" (12).

The number of ways decoding "12" is 2.

dp 法， 截止到每个数字的decode 的方法是固定的，无后效性。并且当前的数字是否是一位的还是两位的，只取决于前面一位
然后只能取决于前两个状态

class Solution:
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) == 0 or s[0] == '0':
            return 0
        dp = [0]*(len(s) + 1)
        dp[0], dp[1] = 1, 1
        for i in range(1, len(s)):
            if s[i] is '0' and s[i] > '2':
                return 0
            if (s[i-1] == '2' and s[i] < '7') or s[i-1] =='1':
                dp[i+1] += dp[i-1]
            if s[i] > '0':
                dp[i+1] += dp[i]
        return dp[-1] 