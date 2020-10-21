227. Basic Calculator II

Implement a basic calculator to evaluate a simple expression string.

The expression string contains only non-negative integers, +, -, *, / operators and empty spaces . The integer division should truncate toward zero.

You may assume that the given expression is always valid.

Some examples:
"3+2*2" = 7
" 3/2 " = 1
" 3+5 / 2 " = 5
Note: Do not use the eval built-in library function.


class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        s = s.replace(' ', '') + '+'
        posi, lastOp = True, '+'
        curr, num, ans = 0, '', 0
        idx = 0
        while idx < len(s):
            if s[idx].isdigit():
                while idx < len(s) and s[idx].isdigit():
                    num += s[idx]
                    idx += 1
                idx -= 1
                num = int(num)
            elif s[idx] == '*' or s[idx] == '/':
                if lastOp is '+' or lastOp is '-':
                    curr = num
                else:
                    if lastOp == '*':
                        curr *= num
                    else:
                        curr //= num
                num = ''
                lastOp = s[idx]
            elif s[idx] == '+' or s[idx] == '-':
                if lastOp == '+' or lastOp == '-':
                    if posi:
                        ans += num
                    else:
                        ans -= num
                    num = ''
                else:
                    if lastOp is '*':
                        curr *= num
                    else:
                        curr //= num

                    if posi:
                        ans += curr
                    else:
                        ans -= curr
                    num = '' 
                lastOp = s[idx]
                if s[idx] == '-':
                    posi = False
                else:
                    posi = True
            idx += 1
        return ans