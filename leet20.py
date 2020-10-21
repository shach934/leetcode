# 20. Valid Parentheses

# Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

# The brackets must close in the correct order, "()" and "()[]{}" are all valid but "(]" and "([)]" are not.

# 考虑到中间可能把栈弹空了的情况

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if len(s) == 0:
            return True
        stack = [s[0]]
        s = s[1:]
        for i in range(len(s)):
            if len(stack) == 0:
                stack.append(s[i])
            else:
                if s[i] == ']' and stack[-1] == '[':
                    stack.pop()
                elif s[i] == ')' and stack[-1] == '(':
                    stack.pop()
                elif s[i] == '}' and stack[-1] == '{':
                    stack.pop()
                else:
                    stack.append(s[i])
        return not len(stack)