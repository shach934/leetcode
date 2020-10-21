140. Word Break II

Given a non-empty string s and a dictionary wordDict containing a list of non-empty words, add spaces in s to construct a sentence where each word is a valid dictionary word. You may assume the dictionary does not contain duplicate words.

Return all such possible sentences.

For example, given
s = "catsanddog",
dict = ["cat", "cats", "and", "sand", "dog"].

A solution is ["cats and dog", "cat sand dog"].

UPDATE (2017/1/4):
The wordDict parameter had been changed to a list of strings (instead of a set of strings). Please reload the code definition to get the latest changes.

class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: List[str]
        """
        def breakable(s, wordDict):
            Dict = {}
            for i in wordDict:
                Dict[i] = Dict.get(i,0)+1
            dp = [False] * (len(s) + 1)
            dp[0] = True
            for i in range(len(s)):
                for j in range(i, -1, -1):
                    if dp[j] and s[j:i+1] in Dict:
                        dp[i+1] = True 
                        break
            return dp[-1]

        def dfs(ret, s, Dict, curr):
            if len(s) == 0:
                ret.append(curr)
            for i in range(len(s)):
                if s[:i+1] in Dict:
                    dfs(ret, s[i+1:], Dict, curr + s[:i+1]+' ')
        
        Dict = {}
        for word in wordDict:
            Dict[word] = Dict.get(word, 0) + 1
        ret = []
        if breakable(s, wordDict):
            dfs(ret, s, Dict, '')
            for i in range(len(ret)):
                ret[i] = ret[i][:-1]
        return ret