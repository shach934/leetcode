# 438. Find All Anagrams in a String

# Given a string s and a non-empty string p, find all the start indices of p's anagrams in s.

# Strings consists of lowercase English letters only and the length of both strings s and p will not be larger than 20,100.

# The order of output does not matter.

# Example 1:

# Input:
# s: "cbaebabacd" p: "abc"

# Output:
# [0, 6]

# Explanation:
# The substring with start index = 0 is "cba", which is an anagram of "abc".
# The substring with start index = 6 is "bac", which is an anagram of "abc".

# Example 2:

# Input:
# s: "abab" p: "ab"

# Output:
# [0, 1, 2]

# Explanation:
# The substring with start index = 0 is "ab", which is an anagram of "ab".
# The substring with start index = 1 is "ba", which is an anagram of "ab".
# The substring with start index = 2 is "ab", which is an anagram of "ab".

class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        ret = []
        pdict = Counter(p)
        subS = Counter(s[:(len(p))])
        if(subS == pdict):
            ret.append(0)
        for idx in range(len(p), len(s)):
            if s[idx] in subS:
                subS[s[idx]] += 1
            else:
                subS[s[idx]] = 1
            # print(idx - len(p))
            # print(s[idx - len(p)])
            subS[s[idx - len(p)]] -= 1
            if subS[s[idx - len(p)]] == 0:
                del subS[s[idx - len(p)]]
            if(subS == pdict):
                ret.append(idx - len(p) + 1)
        return ret 


# sliding window algorithm