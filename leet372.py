372. Super Pow

Your task is to calculate ab mod 1337 where a is a positive integer and b is 
an extremely large positive integer given in the form of an array.

Example1:

a = 2
b = [3]

Result: 8
Example2:

a = 2
b = [1,0]

Result: 1024

class Solution:
    def superPow(self,a, b):
        """
        :type a: int
        :type b: List[int]
        :rtype: int
        """
        p = 1337
        a = a%p
        if a==0 or a==1:
            return a
        index = 0
        for i in b:
            index = index*10 + i
        return self.modPow(a, index, p)
    def modPow(self,a, index, p):
        if index == 1:
            return a
        temp = self.modPow(a, index//2, p)
        if index % 2==0:
            return (temp*temp) % p 
        else:
            return (temp*temp*a)%p