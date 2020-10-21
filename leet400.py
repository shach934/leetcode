400. Nth Digit

Find the nth digit of the infinite integer sequence 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, ...

Note:
n is positive and will fit within the range of a 32-bit signed integer (n < 231).

Example 1:

Input:
3

Output:
3
Example 2:

Input:
11

Output:
0

Explanation:
The 11th digit of the sequence 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, ... is a 0, which is part of the number 10.

class Solution:
    def findNthDigit(self, n):
        """
        :type n: int
        :rtype: int
        """
        accum, digits = 0, []
        for i in range(1,11):
            maxN = '9' * i
            minN = '1' + '0' *(i-1)
            rangeN = [int(minN), int(maxN)]
            if accum + (rangeN[1] - rangeN[0] + 1) * i > n:
                if (n-accum) % i == 0:
                    add = (n - accum) // i
                    targetN = rangeN[0] + add - 1
                    return int(str(targetN)[-1])
                else:
                    add = (n - accum) // i
                    order = (n - accum) % i
                    targetN = rangeN[0] + add
                    return int(str(targetN)[order-1])
            else:
                accum += (rangeN[1] - rangeN[0] + 1) * i