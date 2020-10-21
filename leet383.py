383. Ransom Note

Given an arbitrary ransom note string and another string containing letters from all the magazines, 
write a function that will return true if the ransom note can be constructed from the magazines ; 
otherwise, it will return false.

Each letter in the magazine string can only be used once in your ransom note.

Note:
You may assume that both strings contain only lowercase letters.

canConstruct("a", "b") -> false
canConstruct("aa", "ab") -> false
canConstruct("aa", "aab") -> true

class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        ransom, maga = {}, {}
        for i in magazine:
            maga[i] = maga.get(i, 0) + 1
        for i in ransomNote:
            ransom[i] = ransom.get(i, 0) + 1

        for i in ransom.keys():
            if i not in maga or ransom[i] > maga[i]:
                return False
        return True