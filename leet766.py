766. Toeplitz Matrix

A matrix is Toeplitz if every diagonal from top-left to bottom-right has the same element.

Now given an M x N matrix, return True if and only if the matrix is Toeplitz.
 

Example 1:

Input: matrix = [[1,2,3,4],[5,1,2,3],[9,5,1,2]]
Output: True
Explanation:
1234
5123
9512

In the above grid, the diagonals are "[9]", "[5, 5]", "[1, 1, 1]", "[2, 2, 2]", "[3, 3]", "[4]", and in each diagonal all elements are the same, so the answer is True.
Example 2:

Input: matrix = [[1,2],[2,2]]
Output: False
Explanation:
The diagonal "[1, 2]" has different elements.
Note:

matrix will be a 2D array of integers.
matrix will have a number of rows and columns in range [1, 20].
matrix[i][j] will be integers in range [0, 99].

class Solution(object):
    def isToeplitzMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: bool
        """
        # 判断所有的对角线是否都是相同的元素
        def check_digonal(matrix, i, j):
            M, N = len(matrix), len(matrix[0])
            value = matrix[i][j]
            while 0 <= i < M and 0 <= j < N:
                if matrix[i][j] != value:
                    return False
                i += 1
                j += 1
            return True
        M, N = len(matrix), len(matrix[0])
        for i in range(M):
            if not check_digonal(matrix, i, 0):
                return False
        for j in range(1, N):
            if not check_digonal(matrix, 0, j):
                return False
        return True