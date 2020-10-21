"""
54. Spiral Matrix

Given a matrix of m x n elements (m rows, n columns), return all elements of the matrix in spiral order.

For example,
Given the following matrix:

[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]
You should return [1,2,3,6,9,8,7,4,5].
"""

class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if len(matrix) == 0:
            return []
        mylist, dx, dy, M,N, row, col = [], 0, 1, len(matrix),len(matrix[0]), 0, -1
        path = [[1]*N for i in range(M)]
        while len(mylist) <= M*N - 1:
            if row + dx < M and row + dx >=0 and col + dy < N and col + dy >=0 and path[row+dx][col+dy]:
                row += dx
                col += dy
                path[row][col] = 0
                mylist.append(matrix[row][col])
            else:
                dx, dy = dy, -dx
        return mylist