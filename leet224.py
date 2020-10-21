224. Basic Calculator

Implement a basic calculator to evaluate a simple expression string.

The expression string may contain open ( and closing parentheses ), the plus + or minus sign -, non-negative integers and empty spaces .

You may assume that the given expression is always valid.

Some examples:
"1 + 1" = 2
" 2-1 + 2 " = 3
"(1+(4+5+2)-3)+(6+8)" = 23
Note: Do not use the eval built-in library function.

class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        def helper(s, start, end):
            curr = 0
            idx, posi = start, True
            while idx <= end:
                if s[idx] == '(':
                    subSum, finish = helper(s, idx+1, end)
                    if posi:
                        curr += subSum
                    else:
                        curr -= subSum
                    idx = finish
                elif s[idx] == ')':
                    return curr, idx+1
                elif s[idx].isdigit():
                    num = ''
                    while idx < len(s) and  s[idx].isdigit():
                        num += s[idx]
                        idx += 1
                    num = int(num)
                    if posi:
                        curr += num
                    else:
                        curr -= num
                elif s[idx] == '+':
                    posi = True
                    idx += 1
                else:
                    posi = False
                    idx += 1
            return curr, end
        
        s = s.replace(' ','')
        curr, end = helper(s, 0, len(s)-1)
        return curr