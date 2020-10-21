22. Generate Parentheses

Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

For example, given n = 3, a solution set is:

[
  "((()))",
  "(()())",
  "(())()",
  "()(())",
  "()()()"
]

class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        solu = []
        self.backtrack(solu, '', n, 0, n)
        return solu
        
        
    def backtrack(self, solu, curr, Nleft, Nright, n):
        if len(curr) == 2*n:
            solu.append(curr)
        if Nleft > 0 and  Nright <= 0:
            option = '('
        elif Nright>0 and Nleft <=0:
            option = ')'
        elif Nright >0 and Nleft > 0:
            option = '()'
        else:
            option = []
        for i in range(len(option)):
            if option[i] == '(':
                Nleft -= 1
                Nright += 1
            else:
                Nright -= 1
            curr += option[i]
            self.backtrack(solu, curr, Nleft, Nright, n)
            curr = curr[:-1]
            if option[i] == '(':
                Nleft += 1
                Nright -= 1
            else:
                Nright += 1