131. Palindrome Partitioning

Given a string s, partition s such that every substring of the partition is a palindrome.

Return all possible palindrome partitioning of s.

For example, given s = "aab",
Return

[
  ["aa","b"],
  ["a","a","b"]
]

class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        
        def dfs(s, idx, curr, ret):
            if idx == len(s):
                ret.append(curr[:])
            else:
                for i in range(idx, len(s)):
                    if isParlindrome(s, idx, i):
                        curr.append(s[idx:i+1])
                        dfs(s, i+1,curr, ret)
                        curr.pop()
        def isParlindrome(s, i, j):
            if i == j:
                return True
            if i == 0:
                return s[i:j+1] == s[j::-1]
            else:
                return s[i:j+1] == s[j:i-1:-1]
        ret = []
        dfs(s, 0, [], ret)
        return ret