# 676. Implement Magic Dictionary

# Implement a magic directory with buildDict, and search methods.

# For the method buildDict, you'll be given a list of non-repetitive words to build a dictionary.

# For the method search, you'll be given a word, and judge whether if you modify exactly one character 
# into another character in this word, the modified word is in the dictionary you just built.

# Example 1:
# Input: buildDict(["hello", "leetcode"]), Output: Null
# Input: search("hello"), Output: False
# Input: search("hhllo"), Output: True
# Input: search("hell"), Output: False
# Input: search("leetcoded"), Output: False
# Note:
# You may assume that all the inputs are consist of lowercase letters a-z.
# For contest purpose, the test data is rather small by now. You could think about highly efficient 
# algorithm after the contest.
# Please remember to RESET your class variables declared in class MagicDictionary, as static/class 
# variables are persisted across multiple test cases. Please see here for more details.

#有人是用dict来实现的，但是这里面直接用数组也没啥问题，反而index会更快吧

class MagicDictionary(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.val = []

    def buildDict(self, dict):
        """
        Build a dictionary through a list of words
        :type dict: List[str]
        :rtype: void
        """
        self.val = dict[:]

    def search(self, word):
        """
        Returns if there is any word in the trie that equals to the given word after modifying exactly one character
        :type word: str
        :rtype: bool
        """
        for i in self.val:
            diff = 0
            if len(i) == len(word):
                for l in range(len(i)):
                    if i[l] != word[l]:
                        diff += 1
            if diff == 1:
                return True
        return False

# Your MagicDictionary object will be instantiated and called as such:
# obj = MagicDictionary()
# obj.buildDict(dict)
# param_2 = obj.search(word)

