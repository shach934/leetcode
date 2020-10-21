14. Longest Common Prefix

Write a function to find the longest common prefix string amongst an array of strings.

class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs) == 0:
            return ''
        prefix = ''
        shortest, idx = 2**32, 0
        for i in range(len(strs)):
            if len(strs[i]) < shortest:
                shortest = len(strs[i])
                idx = i
        
        for i in range(shortest):
            candidate, flag = strs[idx][i], True
            for s in strs:
                if s[i] != candidate:
                    flag = False
                    break
            if flag:
                prefix += candidate
            else:
                break
        return prefix