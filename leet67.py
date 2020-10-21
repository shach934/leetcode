# 67. Add Binary

# Given two binary strings, return their sum (also a binary string).

# For example,
# a = "11"
# b = "1"
# Return "100".

class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        a, b = a[::-1], b[::-1]
        if len(a) < len(b):
            sht, lon = a, b
        else:
            sht, lon = b, a
        for i in range(len(lon) - len(sht)):
            sht += '0'
        ret, carryOn = '', 0
        
        for i in range(len(lon)):
            if int(lon[i]) + int(sht[i]) + carryOn>1:
                ret += str((int(lon[i]) + int(sht[i]) + carryOn) - 2)
                carryOn = 1
            else:
                ret += str(int(lon[i]) + int(sht[i]) + carryOn)
                carryOn = 0
        if carryOn:
            ret+='1'
        return ret[::-1]