# leetcode 
# 520. Detect Capital
# Given a word, you need to judge whether the usage of capitals in it is right or not.

# We define the usage of capitals in a word to be right when one of the following cases holds:

# All letters in this word are capitals, like "USA".  
# All letters in this word are not capitals, like "leetcode".
# Only the first letter in this word is capital if it has more than one letter, like "Google".
# Otherwise, we define that this word doesn't use capitals in a right way.

class Solution(object):
    def detectCapitalUse(self, word):
        """
        :type word: str
        :rtype: bool
        """
        str = input("input a word: ")
        if str.isupper() or str.islower() or (str[0].isupper() and str[1:].islower()):
            return true
        return false

# solution in 1 line: 
# return word.isupper() or word.islower() or word.istitle()