59. Spiral Matrix II

Given an integer n, generate a square matrix filled with elements from 1 to n2 in spiral order.

For example,
Given n = 3,

You should return the following matrix:
[
 [ 1, 2, 3 ],
 [ 8, 9, 4 ],
 [ 7, 6, 5 ]
]

class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        mat = [[0 for i in range(n)] for j in range(n)]
        moves, go, num = [[0,1],[1,0],[0,-1],[-1,0]], 0, 1
        row, col = 0, -1
        while num <= n*n:            
            if row+moves[go][0] > - 1 and row+moves[go][0] < n and col+moves[go][1] > -1 and col+moves[go][1] < n and mat[row+moves[go][0]][col+moves[go][1]] == 0:
                row += moves[go][0]
                col += moves[go][1]
                mat[row][col] = num
                num += 1
            else:
                go += 1
                go %= 4
        return mat