# 43. Multiply Strings

# Given two non-negative integers num1 and num2 represented as strings, return the product of num1 and num2.

# Note:

# The length of both num1 and num2 is < 110.
# Both num1 and num2 contains only digits 0-9.
# Both num1 and num2 does not contain any leading zero.
# You must not use any built-in BigInteger library or convert the inputs to integer directly.

class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        if num1 == '0' or num2 == '0':
            return '0'
        num1, num2 = num1[::-1], num2[::-1]
        if len(num1) > len(num2):
            longer, shorter = num1, num2
        else:
            longer, shorter = num2, num1
        ret = ['0' for i in range(len(longer))]
        
        for i in range(len(shorter)):
            prod= []
            carryOn = 0
            for j in range(len(longer)):
                prod += str((int(shorter[i]) * int(longer[j]) + carryOn)%10)
                carryOn = (int(shorter[i]) * int(longer[j]) + carryOn)//10
            if carryOn:
                prod += str(carryOn)
            l1, l2 = len(prod), len(ret[i:-1])
            if l1 < l2:
                for m in range(l2-l1):
                    prod += '0'
            elif l1>l2:
                for n in range(l1-l2 - 1):
                    ret += '0'
            
            addOn = 0
            for k in range(len(prod)):
                addOn_temp = (int(prod[k]) + int(ret[k+i]) + addOn)//10
                ret[k + i] = str((int(prod[k]) + int(ret[k+i]) + addOn)%10)
                addOn = addOn_temp
            if addOn:
                ret += str(addOn)
        return ''.join(ret[::-1])