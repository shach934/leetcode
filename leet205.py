205. Isomorphic Strings

Given two strings s and t, determine if they are isomorphic.

Two strings are isomorphic if the characters in s can be replaced to get t.

All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character but a character may map to itself.

For example,
Given "egg", "add", return true.

Given "foo", "bar", return false.

Given "paper", "title", return true.

Note:
You may assume both s and t have the same length.

class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        dicts = {}
        for idx, letter in enumerate(s):
            if letter not in dicts:
                dicts[letter] = t[idx]
            elif dicts[letter] != t[idx]:
                return False
        dicts = {}
        for idx, letter in enumerate(t):
            if letter not in dicts:
                dicts[letter] = s[idx]
            elif dicts[letter] != s[idx]:
                return False
        return True