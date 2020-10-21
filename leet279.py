279. Perfect Squares

Given a positive integer n, find the least number of perfect square numbers (for example, 1, 4, 9, 16, ...) which sum to n.

For example, given n = 12, return 3 because 12 = 4 + 4 + 4; given n = 13, return 2 because 13 = 4 + 9.

class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        conN = [1]
        for nn in range(2,n+1):
            i, minN = 1, nn
            while i*i <= nn:
                if i*i == nn:
                    minN = 1
                    break
                else:
                    minN = min(minN, conN[nn-i*i-1]+1)
                    i+= 1
            conN.append(minN)
        return conN[n-1]