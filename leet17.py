17. Letter Combinations of a Phone Number

Given a digit string, return all possible letter combinations that the number could represent.

A mapping of digit to letters (just like on the telephone buttons) is given below.

dic = {'0':' ', '1':'*', '2':'abc','3':'def','4':'ghi','5':'jkl','6':'mno','7':'pqrs','8':'tuv','9':'wxyz'}

Input:Digit string "23"
Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
Note:
Although the above answer is in lexicographical order, your answer could be in any order you want.

class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if len(digits) == 0:
            return []
        dic = {'0':' ', '1':'*', '2':'abc','3':'def','4':'ghi','5':'jkl','6':'mno','7':'pqrs','8':'tuv','9':'wxyz'}
        ret = []
        self.backTrack(digits, dic, ret, '')
        return ret
    
    def backTrack(self, digits, dic, ret, curr):
        if len(curr) == len(digits):
            ret.append(curr[:])
        else:
            nex = len(curr)
            option = dic[digits[nex]]
            for i in option:
                self.backTrack(digits, dic, ret, curr + i)