#coding=utf-8

# leetcode 796

# if string A is a rotate of string B
# if so, there is a index where is string A is cut and rotated.
# so we can find this index, the string is at most 100. so n^2 algo is acceptable.

class Solution(object):
    def rotateString(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: bool
        """
        if len(A) != len(B):
            return False
        for i in range(len(A)):
            if A[i:] + A[:i] == B:
                return True
        return False