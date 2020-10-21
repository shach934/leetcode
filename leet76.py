76. Minimum Window Substring

Given a string S and a string T, find the minimum window in S which will contain all the characters in T in complexity O(n).

For example,
S = "ADOBECODEBANC"
T = "ABC"
Minimum window is "BANC".

Note:
If there is no such window in S that covers all characters in T, return the empty string "".

If there are multiple such windows, you are guaranteed that there will always be only one unique minimum window in S.

这道题简直TM了，在算法一目了然的情况下，搞了快一天了，编码能力太差了，几十行，根本没有任何复杂的算法！！！

class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        def contain(dictA, dictB):
            for item in dictB:
                if item not in dictA or dictA[item] < dictB[item]:
                    return False
            return True

        dict_s, dict_t = {}, {}
        start, end = 0, 0
        ans = ''

        for letter in t:
            dict_t[letter] = dict_t.get(letter, 0) + 1
    
        while end <= len(s) - 1:
            while end <= len(s) - 1 and not contain(dict_s, dict_t):
                dict_s[s[end]] = dict_s.get(s[end], 0) + 1
                end += 1
            if contain(dict_s, dict_t):
                while start <= len(s) - 1 and contain(dict_s, dict_t):
                    if not ans or end - start < len(ans):
                        ans = s[start:end]
                    dict_s[s[start]] -= 1
                    start += 1
        return ans