62. Unique Paths

A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).

How many possible unique paths are there?


Above is a 3 x 7 grid. How many possible unique paths are there?

Note: m and n will be at most 100.

class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        board = [[0]*n for i in range(m)]
        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    board[i][j] = 1
                elif i == 0:
                    board[i][j] = board[i][j-1]
                elif j == 0:
                    board[i][j] = board[i-1][j]
                else:
                    board[i][j] = board[i-1][j] + board[i][j-1]
        return board[m-1][n-1]

更好的一个版本，这个利用了第一行和第一列只能是1，只有一个path

class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        board = [[1]*n for i in range(m)]
        for i in range(1,m):
            for j in range(1,n):
                board[i][j] = board[i-1][j] + board[i][j-1]
        return board[m-1][n-1]