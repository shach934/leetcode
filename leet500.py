# 500. Keyboard Row

# Given a List of words, return the words that can be typed using letters 
# of alphabet on only one row's of American keyboard like the image below.

# Example 1:
# Input: ["Hello", "Alaska", "Dad", "Peace"]
# Output: ["Alaska", "Dad"]
# Note:
# You may use one character in the keyboard more than once.
# You may assume the input string will only contain letters of alphabet.

class Solution(object):
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        row1 = set('qwertyuiop')
        row2 = set('asdfghjklASDFGHJKL')
        row3 = set('zxcvbnmZXCVBNM')
        out = []
        for i in a:
            w = set(i.lower())
            if w.issubset(row1) or w.issubset(row2) or w.issubset(row3):
                out.append(i)
        return out

# set elements are unique, and it can use & to find the intersect set. issubset. isupperset 