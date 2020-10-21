# 415. Add Strings

# Given two non-negative integers num1 and num2 represented as string, return the sum of num1 and num2.

# Note:

# The length of both num1 and num2 is < 5100.
# Both num1 and num2 contains only digits 0-9.
# Both num1 and num2 does not contain any leading zero.
# You must not use any built-in BigInteger library or convert the inputs to integer directly.

#先把两个字符串反转，然后用0补齐到相同的长度，相加进位即可。

class Solution(object):
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        num1, num2 = num1[::-1], num2[::-1]
        l1, l2 = len(num1), len(num2)
        if l1 < l2:
            for i in range(l2-l1):
                num1 += '0'
        elif l1>l2:
            for i in range(l1-l2):
                num2 += '0'
        carryOn = 0
        ret =''
        for i in range(len(num1)):
            ret += str((int(num1[i]) + int(num2[i]) + carryOn)%10)
            carryOn = (int(num1[i]) + int(num2[i]) + carryOn)//10
        if carryOn:
            ret += '1'
        return ret[::-1]