# 387. First Unique Character in a String

# Given a string, find the first non-repeating character in it and return it's index. If it doesn't exist, return -1.

# Examples:

# s = "leetcode"
# return 0.

# s = "loveleetcode",
# return 2.

class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        dict = {}
        for letter in s:
            if letter in dict:
                dict[letter] += 1
            else :
                dict[letter] = 1
        return list(dict.values()).index(1) if 1 in list(dict.values()) else -1