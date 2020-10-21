class Solution:
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) == 0 or s[0] == '0':
            return 0
        dp = (len(s) + 1)*[0]
        dp[0], dp[1] = 1, 1
        for i in range(1, len(s)):
            if s[i] is '*':
                for j in range(10):
                    s[i] = str(j)