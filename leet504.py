504. Base 7

Given an integer, return its base 7 string representation.

Example 1:
Input: 100
Output: "202"
Example 2:
Input: -7
Output: "-10"
Note: The input will be in range of [-1e7, 1e7].

class Solution(object):
    def convertToBase7(self, num):
        """
        :type num: int
        :rtype: str
        """
        flag = False
        if num<0:
            flag = True
            num = -num
        if num == 0:
            return str(0)
        ret,carryOn = '',0
        while num > 0:
            ret += str(num % 7)
            if num == 7:
                ret += '1'
                num = 0
            else:
                num = num // 7
        if flag:
            ret += '-'
        return ret[::-1]