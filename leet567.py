567. Permutation in String

Given two strings s1 and s2, write a function to return true if s2 contains the permutation of s1. 
In other words, one of the first string's permutations is the substring of the second string.

Example 1:
Input:s1 = "ab" s2 = "eidbaooo"
Output:True
Explanation: s2 contains one permutation of s1 ("ba").
Example 2:
Input:s1= "ab" s2 = "eidboaoo"
Output: False
Note:
The input strings only contain lower case letters.
The length of both given strings is in range [1, 10,000].

class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        if s1 is None:
            return True
        if len(s1) > len(s2):
            return False
        list1 = [0 for i in range(26)]
        list2 = [0 for i in range(26)]
        for i in range(len(s1)):
            list1[ord(s1[i]) - ord('a')] += 1
            list2[ord(s2[i]) - ord('a')] += 1
        if list1 == list2:
            return True   
        for i in range(len(s1), len(s2)):
            list2[ord(s2[i]) - ord('a')] += 1
            list2[ord(s2[i-len(s1)]) - ord('a')] -= 1
            if list1 == list2:
                return True
        return False